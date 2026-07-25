from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BriefBase(BaseModel):
    title: str
    description: Optional[str] = None

class BriefCreate(BriefBase):
    pass

class Brief(BriefBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class IntentBase(BaseModel):
    intent_text: str

class IntentCreate(IntentBase):
    brief_id: int

class Intent(IntentBase):
    id: int
    brief_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class QueryBase(BaseModel):
    query_text: str

class QueryCreate(QueryBase):
    brief_id: int

class Query(QueryBase):
    id: int
    brief_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class EvidenceBase(BaseModel):
    content: str
    source: Optional[str] = None

class EvidenceCreate(EvidenceBase):
    query_id: int

class Evidence(EvidenceBase):
    id: int
    query_id: int
    created_at: datetime

    class Config:
        from_attributes = True