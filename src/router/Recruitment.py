
from fastapi import APIRouter,Depends
from database.schemas import Recruitment_sche
from sqlalchemy.orm import Session
from database.db import get_db
from database.usersDB import RecruitmentDB
router=APIRouter(prefix="/Recruitment",tags=["Recruitment"])


@router.post("/create_Recruitment")
async def cerate_Recruitment(request:Recruitment_sche.Recruitment ,db:Session=Depends(get_db)):
    return await RecruitmentDB.crate_Recruitment(request=request,db=db)