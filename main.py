from dotenv import load_dotenv
from fastapi import FastAPI
import psycopg2
import dotenv
import os
app = FastAPI()
load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

try:
    db_connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port= DB_PORT

)
    print("Database connection established")
except Exception as e:
    print("we ran into a problem: " + str(e))



@app.get("/")
def read_root():
    return {"message": "Welkom bij GameRecommender"}
