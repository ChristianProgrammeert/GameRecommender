from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool


if not os.getenv("TEST_DATABASE_URL"):
    load_dotenv()

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')

test_engine = create_engine(
    TEST_DATABASE_URL
)

if test_engine is not None:
    print("Connected to Test Database")
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
def override_get_db():

    db = TestSessionLocal()
    try:
        print("Using test db")
        yield db
    finally:
        db.close()
