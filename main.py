import app.queries as queries
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends
from fastapi import FastAPI, Request
import app.algorithm as algorithm
from fastapi.exceptions import RequestValidationError
from app import error_handling as error
from app import input_parser as parser

app = FastAPI()

@app.exception_handler(RequestValidationError)
def boolean_validation_exception_handler(request: Request, err: RequestValidationError):
    for _ in err.errors():
        if _['type'] == 'bool_parsing':
            error.raise_boolean_error()
    raise err
@app.get("/recommendation")
def endpoint_recommender(rage_inducing:bool = None,action_packed:bool = None, skill_based:bool = None,mature_themes:bool = None,open_world:bool = None,multiplayer:bool = None,db: Session = Depends(get_db)):
    AnswerClass = parser.parse_input([bool_value for var_name, bool_value in locals().items() if var_name != 'db'])
    # Makes a list from all the input booleans, excluding the db variable.
    return {"Recommendations":algorithm.link_games_genres(
        algorithm.compute_games(queries.get_games(db), AnswerClass.is_mature, AnswerClass.is_open_world, AnswerClass.is_multiplayer),
        algorithm.compute_genres(queries.get_genres(db), AnswerClass.is_rage_inducing, AnswerClass.is_action_packed, AnswerClass.is_skill_based),
        queries.get_connection_table(db))
    }
@app.get("/genres")
def endpoint_genres(db: Session = Depends(get_db)):
    genres = queries.get_genres(db)
    return {"data":genres}
@app.get("/games")
def endpoint_games(db: Session = Depends(get_db)):
    games = queries.get_games(db)
    return {"data":games}
@app.get("/")
def show_online():
    return {"Welcome to GameRecommender API, see /docs for available endpoints."}
