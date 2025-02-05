from fastapi import FastAPI
import psycopg2
app = FastAPI()

try:
    db_connection = psycopg2.connect(
    database="game_recommender_db",
    user="do_admin",
    password="AVNS_Z8a5xRd6XwRSreQr7QI",
    host="game-recommender-api-do-user-18910148-0.l.db.ondigitalocean.com",
    port="25060"

)
    print("Database connection established")
except Exception as e:
    print("we ran into a problem: " + str(e))



@app.get("/")
def read_root():
    return {"message": "Welkom bij GameRecommender"}
