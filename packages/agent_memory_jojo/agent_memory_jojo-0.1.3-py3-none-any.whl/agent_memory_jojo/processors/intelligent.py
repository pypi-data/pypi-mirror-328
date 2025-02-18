import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv(), override=True)
import uuid
from langchain_core.messages import HumanMessage, AIMessage
from ..client.qdrant_client import QdrantVectorDB
from ..agents.agent import Agent
from ..schema.fact_schema import TradingFacts
from ..schema.document_schema import DocumentPayload
from datetime import datetime as dt
from ..schema.search_schema import MatchAnyOrInterval
from ..utils.app_utils import AppUtil
from pathlib import Path
from pydantic import BaseModel
from typing import Dict, Optional, Union, Any, List
import json
from ..config.config_helper import Configuration
from ..config.logger import Logger

logger = Logger(__name__)

settings = Configuration().get_config('qdrant')

class MemoryFormatter:
    @staticmethod
    def create_payload(
        id: uuid.UUID,
        user_id: str,
        collection_name: str,
        data: Dict[str, Any]
    ) -> DocumentPayload:
        if not id:
            id=str(uuid.uuid4())
        
        return DocumentPayload(
            id=id,
            user_id=user_id,
            text=data,
            document_type="preference",
            memory_type="long_term_memory",
            collection_name=collection_name
        )


class IntelligentMemoryManager:
    BASE_DIR = Path(__file__).resolve().parent.parent
    PROMPT_DIR = BASE_DIR / "agents" / "prompt" / "templates"
    keys_to_ignore = ['user_id', 'document_type', 'memory_type', 'collection_name']

    def __init__(self, user_id: str, collection_name: str = os.environ.get("COLLECTION_NAME")) -> None:
        self.collection_name = collection_name
        self.vectordb = QdrantVectorDB(collection_name=self.collection_name)
        self.limit = self.vectordb.limit
        self.returned_memories = []
        self.user_id = user_id
        self.threshold = 0.21
        self.initialize_system_messages()
        self.initialize_agents()
    
    def initialize_agents(self) -> None:
        """Initializes the fact agent with the specified schema and system prompt."""
        self.generate_fact_agent = self.create_agent(
            Agent,
            name="Personal Information Organizer",
            system_message=self.fact_system_prompt,
            schema=TradingFacts
        )
        self.fact_retrieval_agent=Agent(
            name="smart memory manager",
            schema=None,
            system_message=self.fact_retrieval_system_prompt
        )
        self.generate_fact_agent.set(current_date=dt.now().strftime("%Y-%m-%d"))
        self.generate_fact_agent = self.generate_fact_agent.get_agent()
    
    def initialize_system_messages(self) -> None:
        """Loads system prompts from specified files."""
        self.fact_system_prompt = AppUtil.load_file(
            self.PROMPT_DIR / 'fact_system_prompt.txt'
        )
        self.fact_retrieval_system_prompt = AppUtil.load_file(
            self.PROMPT_DIR / 'fact_retrieval_system_prompt.txt'
        )
        
    def create_agent(
        self,
        agent_class,
        name: str,
        system_message: str,
        schema: Optional[BaseModel] = None,
        **kwargs
    ) -> Agent:
        """
        Creates an instance of the specified agent.

        Args:
            agent_class: The agent class to instantiate.
            name (str): The name of the agent.
            system_message (str): The system message指导 agent behavior.
            schema (Optional[BaseModel], optional): The schema for structuring agent outputs.
                Defaults to None.

        Returns:
            Agent: An instance of the specified agent.
        """
        return agent_class(
            name=name,
            system_message=system_message,
            schema=schema,
            **kwargs
        )
    
    def get_document(self, data: Dict[str, Any], id=None) -> List[Dict[str, Any]]:
        """
        Creates and returns a document based on the input data.

        Args:
            data (Dict[str, Any]): Data to be used in document creation.

        Returns:
            List[Dict[str, Any]]: A list containing the formatted document.
        """
        payload = MemoryFormatter.create_payload(
            id=id,
            user_id=self.user_id,
            collection_name=self.collection_name,
            data=data
        )
        formatted_content = payload.text
        return [{"page_content": formatted_content,"metadata": payload.model_dump(exclude_none=True)}]
    
    def add(self, raw_memory: Dict[str, Any]) -> None:
        """
        Adds a new memory to the vector database after processing through the fact agent.

        Args:
            memory_data (Dict[str, Any]): The memory data to be stored.
        """
        try:
            parsed_messages = AppUtil.parse_messages(raw_memory)
            # Generate facts based on the conversation between the user and the agent
            facts = self.generate_fact_agent.invoke({
                "messages": [HumanMessage(content=parsed_messages)]
            }).model_dump()['facts']
            self.vectordb.get_or_create_collection()

            retrieved_old_memory = []
            for new_mem in facts:
                # Get the related memory based on the newly generated facts
                new_generated_search_facts = [document['page_content'] for document in self.get_document(data=new_mem)][0]
                existing_memories = self.search(
                    query=new_generated_search_facts
                )
            ## Stopped
            retrieved_old_memory.extend(
                {"id": mem["id"], "text": mem["text"]} for mem in existing_memories
            )
            logger.info(f"Total existing memories: {len(retrieved_old_memory)}")

            # mapping UUIDs with integers for handling UUID hallucinations
            temp_uuid_mapping = {}
            for idx, item in enumerate(retrieved_old_memory):
                temp_uuid_mapping[str(idx)] = item["id"]
                retrieved_old_memory[idx]["id"] = str(idx)

            self.fact_retrieval_agent.set(retrieved_old_memory_dict=retrieved_old_memory)
            self.fact_retrieval_agent.set(response_content=facts)
            self.fact_retrieval_active = self.fact_retrieval_agent.get_agent()

            new_memories_with_actions = self.fact_retrieval_active.invoke(
                {
                    "messages":[
                        HumanMessage(
                            content="what is the New Memory Element with their respective event, the event is a must for each element, this output must be in JSON format"
                        )
                    ]
                }
            ).content
            new_memories_with_actions = AppUtil.remove_code_blocks(new_memories_with_actions)
            try:
                new_memories_with_actions = json.loads(new_memories_with_actions)
            except json.JSONDecodeError as ex:
                logger.error(f"Error decoding JSON: {ex}")
                new_memories_with_actions = []
            
            try:
                for result in new_memories_with_actions["memory"]:
                    logger.info(result)
                    output = result
                    try:
                        if output["event"] == "ADD":
                            memory_id = self._create_memory(
                                data=output['text']
                            )
                            self.returned_memories.append(
                                {
                                    "id": memory_id,
                                    "memory": output['text'],
                                    "event": output['event']
                                }
                            )
                        elif output["event"] == "UPDATE":
                            old_memory = self._update_memory(
                                memory_id=temp_uuid_mapping[output["id"]],
                                data=output
                            )
                            self.returned_memories.append(
                                {
                                    "id": temp_uuid_mapping[output["id"]],
                                    "memory": output['text'],
                                    "event": output['event'],
                                    "previous_memory": old_memory
                                }
                            )
                        elif output["event"] == "DELETE":
                            self._delete_memory(memory_id=temp_uuid_mapping[output["id"]])
                            self.returned_memories.append(
                                {
                                    "id": temp_uuid_mapping[output["id"]],
                                    "memory": output['text'],
                                    "event": output['event']
                                }
                            )
                        elif output["event"] == "NONE":
                            logger.info("NOOP for Memory.")
                    except Exception as e:
                        logger.error(f"Error in new_memories_with_actions: {e}")
            except Exception as e:
                logger.error(f"Error in new_memories_with_actions: {e}")
            
        except Exception as e:
            logger.error(f"Error adding memory: {str(e)}")
            raise

    def _update_memory(self, memory_id, data):
        logger.info(f"Updating memory with {data=}")
        try:
            existing_memory = self.get(memory_id)
        except Exception:
            raise ValueError(f"Error getting memory with ID {memory_id}. Please provide a valid 'memory_id'")

        new_metadata = {}
        new_metadata["data"] = data
        for exist_mem in existing_memory:
            if "id" in exist_mem:
                #Prevent resetting the id
                new_metadata['data']['id'] = exist_mem['id']
            if "user_id" in exist_mem:
                #Prevent resetting the user id
                new_metadata['data']['user_id'] = exist_mem['user_id']
        
        id = new_metadata['data'].pop('id', None)
        new_metadata['data'].pop('id', None)
        to_embed = self.get_document(data=new_metadata['data'], id=id)
        self.vectordb.inject(to_embed)

        old_memory = [{
            k: v for k, v in obj.items() if k not in self.keys_to_ignore
        } for obj in [
            document for document in existing_memory
        ]]

        return old_memory
    
    def get_relevant_operation(self):
        return {"result": self.returned_memories}

    def _create_memory(self, data):
        data_document = self.get_document(data=data)
        self.vectordb.inject(data_document, is_batch=False)
        memory_id = [document['metadata'] for document in data_document][0]['id']
        
        return memory_id
    
    def _delete_memory(self, memory_id):
        self.vectordb.delete_one([memory_id])
        return {"message": f"Memory with id {memory_id} deleted successfully!"}
    
    def get(self, id):
        records = self.vectordb.get(id)
        keys_to_ignore = [key for key in keys_to_ignore if key != 'user_id']
        # Remove specified keys from each metadata dictionary
        metadata = [
            {k: v for k, v in metadata['metadata'].items() if k not in keys_to_ignore}
            for metadata in [record.payload for record in records]
        ]
        return metadata
    
    def query(self, query: str, limit=5) -> List[Dict[str, Any]]:
        """
        Retrieves memories from the vector database based on the provided query.

        Args:
            query (str): The search query to filter memories.

        Returns:
            List[Dict[str, Any]]: List of retrieved memories.
        """
        filters = {
            'user_id': MatchAnyOrInterval(any=[str(self.user_id)])
        }
        return self.vectordb.search(query, limit=limit, filters=filters)
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        documents = self.query(query)
        filtered_documents = filter(lambda doc: doc.score['value'] >= self.threshold, documents)

        metadata_list = [{
            k: v for k, v in metadata.items() if k not in self.keys_to_ignore
        } for metadata in [document.metadata for document in list(filtered_documents)]]

        return metadata_list