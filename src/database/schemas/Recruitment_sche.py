from pydantic import BaseModel
from datetime import datetime
from fastapi import Path 
class Recruitment(BaseModel):
    human_id:int
    part_id:int
    date:datetime=datetime.now()
    class Config:
        from_attributes = True