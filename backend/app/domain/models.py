from pydantic import BaseModel
from typing import List

class TagResult(BaseModel):
    tags: List[str]
