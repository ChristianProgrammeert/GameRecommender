from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from database import SessionLocal
from models import Genre, Game


app = FastAPI()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/genres")
def get_genres(db):
    print("getting genres")
    genres = db.query(Genre).all()
    return{"data": genres}

@app.get("/games")
def get_games(db):
    games = db.query(Game).all()
    if len(games) == 0:
        print("data not found")
    return {"data": games}
