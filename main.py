import app.queries as queries
from sqlalchemy.orm import Session
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from functools import wraps
from app.database import get_db
from fastapi import Depends
from fastapi import FastAPI
import app.algorithm as algorithm
from app import error_handling as error
from app import input_parser as parser

# Prometheus metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Summary("http_request_latency_seconds", "Request latency in seconds")
app = FastAPI()

@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Decorator for tracking Prometheus metrics
def track_metrics(endpoint: str):
    def decorator(func):
        @wraps(func)  # Preserve the original function's signature
        async def wrapper(*args, **kwargs):
            REQUEST_COUNT.labels(method="GET", endpoint=endpoint, status="200").inc()
            with REQUEST_LATENCY.time():
                return await func(*args, **kwargs)
        return wrapper
    return decorator

@app.get("/recommendation")
@track_metrics("/recommendation")
def endpoint_recommender(answers = None,db: Session = Depends(get_db)):
    if not answers:
        error.raise_input_error()
    AnswerClass = parser.parse_input(answers)
    return {"Recommendations":algorithm.link_games_genres(
        algorithm.compute_games(queries.get_games(db), AnswerClass.is_mature, AnswerClass.is_open_world, AnswerClass.is_multiplayer),
        algorithm.compute_genres(queries.get_genres(db), AnswerClass.is_rage_inducing, AnswerClass.is_action_packed, AnswerClass.is_skill_based),
        queries.get_connection_table(db))
    }
@app.get("/genres")
@track_metrics("/genres")
def endpoint_genres(db: Session = Depends(get_db)):
    genres = queries.get_genres(db)
    return {"data":genres}
@app.get("/games")
@track_metrics("/games")
def endpoint_games(db: Session = Depends(get_db)):
    games = queries.get_games(db)
    return {"data":games}

@app.get("/")
def show_online():
    return {"Welcome to GameRecommender API, see /docs for available endpoints."}

