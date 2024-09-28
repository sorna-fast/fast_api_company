from database.models import Human_Resources,Recruitment
from database.schemas import human_schy
from sqlalchemy.orm import Session

async def create_human(request:human_schy.base_human,db:Session):
    user=Human_Resources(
        name=request.name,
        family=request.family)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


