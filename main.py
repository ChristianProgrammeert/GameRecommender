from queries import *
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from algorithm import *
from app import input_parser as parser

app = FastAPI()
@app.get("/test")
def test_endpoint():
    return {"message": "Test route works"}

@app.get("/recommend/{answers}")
def endpoint_recommender(answers,db: Session = Depends(get_db)):
    AnswerClass = parser.parse_input(answers)
    genre_names = compute_genres(get_genres(db),AnswerClass.is_rage_inducing,AnswerClass.is_skill_based,AnswerClass.is_action_packed)
    game_names = compute_games(get_games(db),AnswerClass.is_open_world, AnswerClass.is_mature,AnswerClass.is_multiplayer)
    recommendation = link_games_genres(game_names,genre_names,get_connection_table(db))
    return {"Recommendations:":recommendation}

@app.get("/genres")
def endpoint_genres(db: Session = Depends(get_db)):
    genres = get_genres(db)
    return {"data":genres}
@app.get("/games")
def endpoint_games(db: Session = Depends(get_db)):
    games = get_games(db)
    return {"data":games}

@app.get("/")

def read_root(db: Session = Depends(get_db)):
    genres = get_genres(db)
    games = get_games(db)
    names = compute_genres(genres)
    titles = compute_games(games)
    connections = get_connection_table(db)
    connie = link_games_genres(titles, names, connections)
    return {"pairs": connie}
