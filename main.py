from queries import *
from sqlalchemy.orm import Session

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
    titles = compute_genres(genres)
    return {"message": "ello World",
            "genres": genres,
            "games": games,
            "names": titles}

