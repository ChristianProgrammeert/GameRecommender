import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI
import os
import dotenv

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")



app = FastAPI()
try:
    db_connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT

)
    print("Database connection established")
except Exception as e:
    print("we ran into a problem: " + str(e))

def get_genres():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM jouw_tabel_naam")
    data = cursor.fetchall()
    cursor.close()
    return {"data": data}
def get_games():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM jouw_tabel_naam")
    data = cursor.fetchall()
    cursor.close()
    return {"data": data}