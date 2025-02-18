from queries import *
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from algorithm import *
from app import input_parser as parser

app = FastAPI()

@app.get("/recommend/{answers}")
def endpoint_recommender(answers,db: Session = Depends(get_db)):
    AnswerClass = parser.parse_input(answers)
    result = compute_genres(get_genres(db),AnswerClass.is_rage_inducing,AnswerClass.is_multiplayer,AnswerClass.is_action_packed)





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

endpoint_recommender("110110")
