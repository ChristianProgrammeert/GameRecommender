from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy import inspect
from app.models import Base

#Only loads dotenv if variables aren't local yet. Local variables add extra safety to docker containers. this makes sure it still runs local.
if not os.getenv("DATABASE_URL"):
    load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL
)
if engine is not None:
    print("Connected to database")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Existing Tables:", tables)

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

