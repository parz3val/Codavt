# Settign up with with sql alchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sprovide the sqlite db url for mac
ALK_DB_URL = "sqlite:///./todo_app.db"

# create the db engine in the path
engine = create_engine(
    ALK_DB_URL, connect_args={"check_same_thread": False}
)
# Create a sesssion
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 
Base = declarative_base()

