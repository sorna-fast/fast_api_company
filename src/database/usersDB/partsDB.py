from database.models import Part
from database.schemas import parts_sche
from sqlalchemy.orm import Session

async def create_part(request:parts_sche.Base_part,db:Session):
    user=Part(id=request.id,
        part_name=request.part_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user