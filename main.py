from queries import *
from sqlalchemy.orm import Session

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
datab = SessionLocal()
try:
    games = datab.query(Game).all()
    genres = datab.query(Genre).all()
    print(f"Games: {games}")
    print(f"Genres: {genres}")
finally:
    datab.close()

@app.get("/genres")
def get_genres(db: Session = Depends(get_db)):
    print("getting genres")
    genres = db.query(Genre).all()
    return{"data": genres}

@app.get("/games")
def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    if len(games) == 0:
        print("data not found")
    return {"data": games}
@app.get("/")
def read_root(db: Session = Depends(get_db)):
    genres = db.query(Genre).all()
    games = db.query(Game).all()
    return {"message": "Hello World",
            "genres": genres,
            "games": games}