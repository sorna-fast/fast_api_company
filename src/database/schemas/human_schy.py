from pydantic import BaseModel
from datetime import datetime

class base_human(BaseModel):
    name:str
    family:str
    class Config:
        from_attributes = True

    
    
class Recruitment_base(BaseModel):
    human_id:int
    part_human:int
    date:datetime=datetime.now()
        

        
class Recruitment_show(BaseModel):
    part_human:int
    date:datetime
    class Config:
        from_attributes = True