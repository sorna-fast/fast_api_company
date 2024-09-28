from pydantic import BaseModel

from database.schemas import human_schy




class Base_part(BaseModel):
    id:int
    part_name:str
    class Config:
        from_attributes = True

    
class show_part(BaseModel):
    id:int
    human:list[human_schy.base_human]

    class Config:
        from_attributes = True