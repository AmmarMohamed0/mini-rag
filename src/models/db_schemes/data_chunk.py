from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    _id: Optional[ObjectId]    # _id by default mongodb created 
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)  # gt -> grater than
    chunk_project_id: ObjectId 
    
    
    class Config:
        arbitrary_types_allowed = True