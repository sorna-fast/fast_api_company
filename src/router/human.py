from fastapi import APIRouter,Depends
from database.schemas import human_schy
from sqlalchemy.orm import Session
from database.db import get_db
from database.usersDB import humanDB
router=APIRouter(prefix="/human",tags=["human"])

@router.post("/create_human")
async def create_user_human(request:human_schy.base_human,db:Session=Depends(get_db)):
    return await humanDB.create_human(request=request,db=db)