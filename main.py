from queries import *
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

app = FastAPI()

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
    connections = get_connectiontbl(db)
    connie = link_gamesgenres(titles, names, connections, db)
    return {"pairs": connie}

