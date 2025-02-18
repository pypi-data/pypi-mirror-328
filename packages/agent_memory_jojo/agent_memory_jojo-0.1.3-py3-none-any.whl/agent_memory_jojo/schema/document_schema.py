from typing import List, Dict
from pydantic import BaseModel
from .fact_schema import TradingFacts

class DocumentPayload(BaseModel):
    id: str
    user_id: str
    text: str
    document_type: str
    memory_type: str
    collection_name: str