from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import inspect

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

# Connection timeout is set to 60 seconds because it kept timing out
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require&connect_timeout=60"

try:
    engine = create_engine(DATABASE_URL)
    if engine is not None:
        print("Connected to database")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Created Tables:", tables)

except Exception as e:
    print("we ran into a problem: " + str(e))
