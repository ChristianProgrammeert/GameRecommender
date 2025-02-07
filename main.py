from queries import *

app = FastAPI()






@app.get("/")
def read_root(db: Session = Depends(get_db)):
    genres = get_genres(db)
    games = get_games(db)
    return {"message": "Hello World",
            "genres": genres["data"],
            "games": games["data"]}