from dotenv import load_dotenv
from fastapi import FastAPI, Depends
import os
from algorithm import *

app = FastAPI()

def get_genres(db: Session = Depends(get_db)):
    genres = db.query(Genre).all()
    return {"data": genres}

@app.get("/games")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    return {"data": games}
