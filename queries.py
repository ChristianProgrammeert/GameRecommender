from fastapi import FastAPI
from database import SessionLocal
from models import Genre, Game, GameGenre

app = FastAPI()

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_genres(db):
    """Returns every entry from genres table"""
    genres = db.query(Genre).all()
    return genres

def get_games(db):
    """Returns every entry from games table"""
    games = db.query(Game).all()
    return games

def get_connection_table(db):
    """Returns the entire connection table"""
    connection_table = db.query(GameGenre).all()
    return connection_table

