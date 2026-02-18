import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_PATH=os.getenv("DB_PATH")
engine=create_engine(DB_PATH,echo=True)
Sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
    
