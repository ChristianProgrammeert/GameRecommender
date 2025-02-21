from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import time
from sqlalchemy.exc import OperationalError
from sqlalchemy import inspect
from app.models import Base

#Only loads dotenv if variables aren't local yet. Local variables add extra safety to docker containers. this makes sure it still runs local.
if not os.getenv("DB_USER"):
    load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

# Connection timeout is set to 60 seconds because it kept timing out
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require&connect_timeout=60"

# try:
#     engine = create_engine(
#     DATABASE_URL,
#     poolclass=QueuePool,
#     pool_size=10,  # Active connections in the pool
#     max_overflow=20,  # Extra connections allowed beyond the pool size
#     pool_timeout=30  # Wait time before throwing a timeout error
#     )
#
#     MAX_RETRIES = 5
#
#     for attempt in range(MAX_RETRIES):
#         try:
#             with engine.connect() as conn:
#                 print("Connected successfully!")
#                 break  # Success, exit loop
#         except OperationalError:
#             print(f"Retrying connection attempt: ({attempt + 1}/{MAX_RETRIES})")
#             time.sleep(2)  # Wait before retrying
#     else:
#         raise Exception("Database connection failed after multiple attempts")
#
#     if engine is not None:
#         SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#         Base.metadata.create_all(engine)
#
#         inspector = inspect(engine)
#         tables = inspector.get_table_names()
#         print("Existing Tables:", tables)
#
#
#
# except Exception as e:
#     print("We ran into a problem: " + str(e))

# Maak de engine buiten de try-except zodat het altijd beschikbaar is
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60
)
Base.metadata.create_all(engine)

inspector = inspect(engine)
tables = inspector.get_table_names()
print("Existing Tables:", tables)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

