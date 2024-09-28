from fastapi import APIRouter,Depends
from database.schemas import parts_sche
from sqlalchemy.orm import Session
from database.db import get_db
from database.usersDB import partsDB
router=APIRouter(prefix="/part",tags=["part"])

@router.post("/create_part")
async def create_part(request:parts_sche.Base_part,db:Session=Depends(get_db)):
    return await partsDB.create_part(request=request,db=db)