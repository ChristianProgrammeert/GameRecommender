from app.queries import *
from sqlalchemy.orm import Session
from fastapi import Depends
from app.algorithm import *
from app import error_handling as error
from app import input_parser as parser

app = FastAPI()
@app.get("/recommendation")
def endpoint_recommender(answers = None,db: Session = Depends(get_db)):
    if not answers:
        error.raise_input_error()
    AnswerClass = parser.parse_input(answers)
    return {"Recommendations":link_games_genres(
        compute_games(get_games(db), AnswerClass.is_mature, AnswerClass.is_open_world, AnswerClass.is_multiplayer),
        compute_genres(get_genres(db), AnswerClass.is_rage_inducing, AnswerClass.is_action_packed, AnswerClass.is_skill_based),
        get_connection_table(db))
    }
@app.get("/genres")
def endpoint_genres(db: Session = Depends(get_db)):
    genres = get_genres(db)
    return {"data":genres}
@app.get("/games")
def endpoint_games(db: Session = Depends(get_db)):
    games = get_games(db)
    return {"data":games}
@app.get("/")
def show_online():
    return {"Welcome to GameRecommender API, see /docs for available endpoints."}
