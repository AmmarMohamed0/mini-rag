from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId     # datatype of id in monogdb

class Project(BaseModel):
    _id: Optional[ObjectId]
    project_id:str = Field(...,min_length=1)   # i don't be empty string
    
    @validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():     # isalnum that is all alphanumeric
            raise ValueError('project_id must be alphanumeric')
        
        return value   
    
    
    class Config:
        arbitrary_types_allowed = True   # cause pydantic does not support or understand the ObjectId
                            # so we have to allow it. anything not supported don't  raise ValueError