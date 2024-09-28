
from database.models import Recruitment
from database.schemas import Recruitment_sche
from sqlalchemy.orm import Session



async def crate_Recruitment(request:Recruitment_sche.Recruitment,db:Session):
    user=Recruitment(
        human_id=request.human_id,
        part_id=request.part_id,
        date=request.date
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user





