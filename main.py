from algorithm import *


@app.get("/")
def read_root():
    return {"message": "Welkom bij GameRecommender"}
@app.get("/get_data_from_db")
def genre_computing():
    return get_genres()
def get_game_data_from_db():
    return get_games()
