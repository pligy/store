import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

PGPOOL_URLS = [os.getenv("PGPOOL_URL"), os.getenv("PGPOOL_URL_1")]
SELECTED_PGPOOL_URL = random.choice(PGPOOL_URLS)

#engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))
engine = create_engine(SELECTED_PGPOOL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

get_db()
