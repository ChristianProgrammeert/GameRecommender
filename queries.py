from fastapi import FastAPI
from database import SessionLocal
from models import Genre, Game, GameGenre

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

def get_connectiontbl(db):
    connectiontbl = db.query(GameGenre).all()
    return connectiontbl

