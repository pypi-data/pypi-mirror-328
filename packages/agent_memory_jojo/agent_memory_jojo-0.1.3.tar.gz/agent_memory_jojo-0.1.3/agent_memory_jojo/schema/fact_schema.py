from pydantic import BaseModel, Field
from typing import List

class TradingFacts(BaseModel):
    facts: List[str] = Field(default_factory=list, description="A list of trading-related facts extracted from the conversation.")