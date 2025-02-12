from pickle import FALSE

from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from database import SessionLocal
from models import Genre, Game, GameGenre

action_pack = True
rage = False
multiplay = False
open_world = True
mature = True
skill_based = False
length = 100
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

def compute_games(games):
    result = []
    for game in games:
        if game.open_world == open_world and game.mature_themes == mature and game.skill_based == skill_based and game.length_in_hours <= length:
            game.name = game.name.lower()
            result.append(game.name)
    return result
