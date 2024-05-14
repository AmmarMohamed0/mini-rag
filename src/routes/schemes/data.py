from pydantic import BaseModel
from typing import Optional

class processRequest(BaseModel):
    # form of data to make a request
    file_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: Optional[int] = 0  # => added do to reset to explain that do action 
    