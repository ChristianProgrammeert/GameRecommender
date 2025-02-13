from fastapi import FastAPI
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

def get_connectiontbl(db):
    connectiontbl = db.query(GameGenre).all()
    return connectiontbl

def compute_genres(genres):
    result = []
    for  genre in genres:
        if genre.rage_inducing == rage and genre.multiplayer == multiplay and genre.action_packed == action_pack:
            genre.name = genre.name.lower()
            result.append(genre)
    return result

def compute_games(games):
    result = []
    for game in games:
        if game.open_world == open_world and game.mature_themes == mature and game.skill_based == skill_based and game.length_in_hours <= length:
            game.name = game.name.lower()
            result.append(game)
    return result

def link_gamesgenres(titles, names, connectiontbl, db):
    result = {}
    for genre in names:
        game_list = []
        for connection in connectiontbl:
            if connection.genre_id == genre.id:
                game_id = connection.game_id
                for game in titles:
                    if game.id == game_id:
                        game_list.append(game.name)
        result[genre.name] = game_list
    return result


