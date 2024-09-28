from fastapi import FastAPI
from router import human,parts,Recruitment
from database.db import engine
from database.models import base
app =FastAPI()

app.include_router(human.router)
app.include_router(parts.router)
app.include_router(Recruitment.router)

base.metadata.create_all(engine)



# programmer masud gasemi
# email:masudpythongit@gmail.com
# phone number: 09010361944