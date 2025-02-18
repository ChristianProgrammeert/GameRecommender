from fastapi import FastAPI
from models import Genre, Game, GameGenre
from database import SessionLocal

app = FastAPI()

action_pack = True
rage = True
multiplay = False
open_world = True
mature = True
skill_based = False
length = 100


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def compute_genres(genres,rage,multiplayer,action_pack):
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

def link_games_genres(titles, names, connection_table):
    result = {}
    for genre in names:
        game_list = []
        for connection in connection_table:
            if connection.genre_id == genre.id:
                game_id = connection.game_id
                for game in titles:
                    if game.id == game_id:
                        game_list.append(game.name)
        result[genre.name] = game_list
    return result
