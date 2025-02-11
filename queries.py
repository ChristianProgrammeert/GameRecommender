from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from database import SessionLocal
from models import Genre, Game

rage = False
multiplay = False
action_pack = True
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
    genres = db.query(Genre).all()
    return genres

@app.get("/games")
def get_games(db):
    games = db.query(Game).all()
    return games

def compute_genres(genres):
    result = []
    for  genre in genres:
        if genre.rage_inducing == rage and genre.multiplayer == multiplay and genre.action_packed == action_pack:
            genre.name = genre.name.lower()
            result.append(genre.name)
    return result
