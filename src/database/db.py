from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://root:26182618m@localhost/CompanyDB")
'''
namse saported engine sql :
Firebird
Microsoft SQL Server
MySQL
Oracle
PostgreSQL
SQLite
Sybase


'''



base=declarative_base()



sessionlocal=sessionmaker(bind=engine,autoflush=False)

def get_db():
    global sessionlocal
    session=sessionlocal()
    try:
        yield session
    finally:
        session.close()