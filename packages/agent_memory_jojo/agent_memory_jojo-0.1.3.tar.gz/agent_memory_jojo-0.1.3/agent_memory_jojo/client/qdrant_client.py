import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv(), override=True)
from ..schema.search_schema import MatchAnyOrInterval
from qdrant_client import QdrantClient
from qdrant_client.models import (
    UpdateStatus,
    models,
    Distance,
    PointStruct,
    Filter,
    FieldCondition, 
    MatchAny, 
    DatetimeRange,
    Batch
)
from tenacity import retry, stop_after_attempt, wait_fixed
from ..custom.documents import Document
import numpy as np
from datetime import datetime as dt
import time
from tqdm import tqdm
import uuid
from typing import List, Dict, Any, Union, Optional

os.environ["TOKENIZERS_PARALLELISM"] = "false"
from sentence_transformers import SentenceTransformer

from ..config.config_helper import Configuration
from ..config.logger import Logger

logger = Logger(__name__)

settings = Configuration().get_config('qdrant')

class QdrantVectorDB:
    def __init__(
            self,
            model_name: str = os.environ.get("EMBEDDING_MODEL"),
            collection_name: str = os.environ.get("COLLECTION_NAME"),
            max_attempts: int = settings['max_attempts'], 
            wait_time_seconds: int = settings['wait_time_seconds'],
            default_segment_number: int = settings['default_segment_number'],
            indexing_threshold: int = settings['indexing_threshold'],
            batch_size: int = settings['batch_size'],
            content_payload_key: str = settings['content_payload_key'],
            metadata_payload_key: str = settings['metadata_payload_key'],
            score_key: str = settings['score_key'],
            limit: int = int(os.environ.get("LIMIT")),
            # is_batch: bool = settings['is_batch']
        ):
        self.__model_name = model_name
        self.__collection_name = collection_name
        self.client = QdrantClient(
            url=os.getenv('QDRANT_URL'),
            api_key=os.getenv('QDRANT_CLUSTER')
        )
        self.__sentence_model = SentenceTransformer(self.__model_name, device="cpu", trust_remote_code=True)
        # self.is_batch = is_batch
        self.limit = limit
        self.__default_segment_number = default_segment_number
        self.__indexing_threshold = indexing_threshold
        self.__batch_size = batch_size
        self.__max_attempts = max_attempts
        self.__wait_time_seconds = wait_time_seconds
        self.__content_payload_key = content_payload_key
        self.__metadata_payload_key = metadata_payload_key
        self.__score_key = score_key

    def encode(self, docs: List[str]) -> np.ndarray:
        """
        Encode a list of documents in batches using the Ember model.

        :param docs: The list of documents to encode.
        :return: The embeddings for the documents as a NumPy array.
        """
        @retry(stop=stop_after_attempt(self.__max_attempts), wait=wait_fixed(self.__wait_time_seconds))
        def encode_batch(batch_docs: List[str]) -> np.ndarray:
            try:
                return self.__sentence_model.encode([doc.page_content for doc in batch_docs])
            except Exception:
                return self.__sentence_model.encode(batch_docs)
        
        embeddings = []
        try:
            for i in tqdm(range(0, len(docs), self.__batch_size)):
                batch_docs = docs[i:i+self.__batch_size]
                batch_embeddings = encode_batch(batch_docs)
                embeddings.append(batch_embeddings)

            if embeddings:
                embeddings = np.concatenate(embeddings)
            else:
                raise ValueError("No embeddings were generated.")

            if self.__sentence_model.get_sentence_embedding_dimension() == embeddings.shape[1]:
                return embeddings
            else:
                raise logger.error(f"The embeddings have an incorrect dimension of {embeddings.shape[1]}.")
        except Exception as ex:
            raise logger.error(f"Attempt failed. Retrying Batch... Error: {str(ex)}")
        
    def generate_points(self, docs: List[str]) -> List[Dict[str, Any]]:
        """
        Generate a list of points by encoding the documents using the Ember model and combining the embeddings with the metadata.

        :param docs: The list of documents to encode.
        :return: A list of points with the embeddings and metadata.
        """
        # Encode the documents in batches
        embeddings = self.encode([doc.get('page_content') for doc in docs])
        logger.info("Embedding Completed")

        # Combine the embeddings with the metadata
        points_list = [
            {
                "id": doc.get('metadata')["id"],
                "vector": content_embedding,
                "payload": {
                    self.__metadata_payload_key: doc.get('metadata'),
                    self.__content_payload_key: doc.get('page_content'),
                },
            }
            for (doc, content_embedding) in zip(docs, embeddings)
        ]
        logger.info("Generating points")

        return points_list

    def get_or_create_collection(self):
        try:
            self.client.get_collection(collection_name=self.__collection_name)
            logger.info(f"Collection '{self.__collection_name}' already exists----- Using {self.__collection_name} collection.")
            
        except Exception:
            is_created = self.client.create_collection(
                collection_name=self.__collection_name,
                vectors_config=models.VectorParams(
                    size=self.__sentence_model.get_sentence_embedding_dimension(), 
                    distance=Distance.COSINE
                ),
                optimizers_config=models.OptimizersConfigDiff(
                    default_segment_number=self.__default_segment_number,
                    indexing_threshold=self.__indexing_threshold,
                ),
                quantization_config=models.BinaryQuantization(
                    binary=models.BinaryQuantizationConfig(always_ram=True),
                )
            )
            
            if is_created:
                logger.info(f"Collection '{self.__collection_name}' does not exist. Creating {self.__collection_name} collection.")
            else:
                logger.error(f"{self.__collection_name}' Collection was not created.")
            
    def delete_collection(self):
        self.client.delete_collection(collection_name=self.__collection_name)
        logger.info(f"Deleted '{self.__collection_name}' Collection.")

    def delete_one(self, id: List[str]):
        """Delete one item from the vector database"""
        if not isinstance(id, list):
            id=[id]
            logger.warning(f" '{id}' Must be in a list to be able to delete it.")
        
        self.client.delete(
            collection_name=self.__collection_name,
            points_selector=models.PointIdsList(points=id)
        )
        logger.info(f"Deleted '{id}' '{self.__collection_name}' Collection.")
    
    # New method for batch updates
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(0.7))
    def batch_update(self, update_operations: List[Dict[str, Any]]) -> None:
        """
        Perform batch updates on the collection, including updating vectors and payload.

        :param update_operations: List of dictionaries specifying the update operations. Each operation can be:
            - Update vectors for specific points.
            - Set payload for specific points.
        
            update_operations = [
                {
                    'type': 'update_vectors',
                    'data': [(point_id, new_vector), ...]
                },
                {
                    'type': 'set_payload',
                    'payload': {'key': 'value', ...},
                    'points': [point_id1, point_id2, ...]
                }
            ]
        """
        try:
            operations = []
            for operation in update_operations:
                if operation['type'] == 'update_vectors':
                    points = [
                        models.PointVectors(
                            id=point_id,
                            vector=vector
                        )
                        for point_id, vector in operation['data']
                    ]
                    operations.append(
                        models.UpdateVectorsOperation(
                            points=points
                        )
                    )
                elif operation['type'] == 'set_payload':
                    operations.append(
                        models.SetPayloadOperation(
                            payload=operation['payload'],
                            points=operation['points']
                        )
                    )
                else:
                    logger.warning(f"Unsupported operation type: {operation['type']}")

            if not operations:
                logger.info("No valid operations to perform.")
                return

            # Execute batch operations
            response = self.client.batch(
                collection_name=self.__collection_name,
                operations=operations
            )

            if response.status == UpdateStatus.COMPLETED:
                logger.info("Batch update completed successfully.")
            else:
                logger.error(f"Batch update failed with status: {response.status}")

        except Exception as ex:
            logger.error(f"Batch update failed due to error: {str(ex)}")
            raise

    def upsert_points(self, points_list: List[Dict[str, Any]], is_batch: bool) -> None:
        """
        Upsert a list of points into the specified collection with retry.

        :param points_list: The list of points to upsert.
        """
        @retry(stop=stop_after_attempt(self.__max_attempts), wait=wait_fixed(self.__wait_time_seconds))
        def upsert_batch(batch_data: List[Dict[str, Any]]) -> None:
            """
            Upsert a batch of points into the specified collection.

            :param batch_data: The batch of points to upsert.
            """
            try:
                batch_ids = [point['id'] for point in batch_data]
                batch_vectors = [point['vector'] for point in batch_data]
                batch_payloads = [point['payload'] for point in batch_data]

                upserted = self.client.upsert(
                    collection_name=self.__collection_name,
                    points=Batch(
                        ids=batch_ids,
                        vectors=batch_vectors,
                        payloads=batch_payloads
                    )
                )
                return upserted
            except Exception as ex:
                raise ValueError(f"Attempt failed. Retrying Batch... Error: {str(ex)}")

        @retry(stop=stop_after_attempt(self.__max_attempts), wait=wait_fixed(self.__wait_time_seconds))
        def upsert(points_list: List[Dict[str, Any]]) -> None:
            """
            Upsert a list of points into the specified collection.

            :param points_list: The list of points to upsert.
            """
            try:
                points = [PointStruct(**point) for point in points_list]
                upserted = self.client.upsert(collection_name=self.__collection_name, points=points)
                return upserted
            except Exception as ex:
                raise logger.error(f"Attempt failed. Retrying... {str(ex)}")
        
        if is_batch:
            for i in tqdm(range(0, len(points_list), self.__batch_size)):
                batch_data = points_list[i:i+self.__batch_size]
                upserted = upsert_batch(batch_data)
                if upserted.status == UpdateStatus.COMPLETED:
                    logger.info("Bulk Records inserted successfully.")
        else:
            upserted = upsert(points_list)
            if upserted.status == UpdateStatus.COMPLETED:
                logger.info("Records inserted successfully.")

    def get(self, id: Optional[Union[str, uuid.UUID]] = None, retries: int = 3, delay: int = 2) -> Optional[List[dict]]:
        if id is None:
            logger.warning("No ID provided. Nothing to retrieve.")
            return None

        if not isinstance(id, list):
            id = [id]
            logger.warning(f"ID '{id}' must be in a list to be able to retrieve it.")

        for attempt in range(retries):
            try:
                output = self.client.retrieve(
                    collection_name=self.__collection_name,
                    ids=id,
                    with_payload=True
                )
                return output
            except Exception as ex:
                logger.error(f"Error retrieving data on attempt {attempt + 1}: {ex}")
                if attempt < retries - 1:
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    logger.error("Max retries exceeded. Failed to retrieve data.")
                    return None
    
    def refine(self, filters: Dict[str, MatchAnyOrInterval] = None):
        if filters is None:
            filter_obj = None
            return filter_obj
        else:
            filter_conds = []
            for field, value in filters.items():
                if value.any is not None:
                    filter_conds.append(FieldCondition(key=f"{self.__metadata_payload_key}.{field}", match=MatchAny(any=value.any)))
                elif any([value.gt, value.gte, value.lt, value.lte]):
                    gt_value = value.gt or value.gte
                    lt_value = value.lt or value.lte
                    filter_conds.append(
                        FieldCondition(
                            key=field,
                            range=DatetimeRange(
                                gt=gt_value,
                                gte=(value.gte if gt_value == value.gte else None),
                                lt=lt_value,
                                lte=(value.lte if lt_value == value.lte else None),
                            ),
                        )
                    )
            filter_obj = Filter(must=filter_conds)

            return filter_obj
        
    def search(self, query, limit=None, filters: Dict[str, MatchAnyOrInterval] = None):
        if limit is None:
            limit = self.limit
        
        query_vector = self.__sentence_model.encode(query)
        query_filter = self.refine(filters)

        hits = self.client.search(
            collection_name= self.__collection_name,
            query_vector= query_vector,
            query_filter= query_filter,
            with_payload= True,
            with_vectors= False,
            limit= limit,
            search_params=models.SearchParams(
                    quantization=models.QuantizationSearchParams(
                        ignore=False,
                        rescore=False,
                        oversampling=2.0,
                    ),
                    exact=True,
                )
        )

        # Convert the search results to a list of Document objects
        results = [
            Document(
                page_content=hit.payload[self.__content_payload_key],
                metadata=hit.payload[self.__metadata_payload_key],
                score={self.__score_key: hit.score},
            )
            for hit in hits
        ]

        return results

    def inject(self, docs: List[str], is_batch = False):
        self.get_or_create_collection()
        points_list = self.generate_points(docs)
        self.upsert_points(points_list, is_batch)