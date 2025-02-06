from dotenv import load_dotenv
from fastapi import FastAPI, Depends
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from models import Base, Genre, Game
from database import SessionLocal

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/genres")
def get_genres(db: Session = Depends(get_db)):
    genres = db.query(Genre).all()
    return {"data": genres}

@app.get("/games")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    return {"data": games}
