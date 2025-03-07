from fastapi import FastAPI
from app.models import Genre, Game, GameGenre

app = FastAPI()

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

def add_genres(db):
    genre = Genre(id=1, name='RPG', rage_inducing=False, action_packed=False, skill_based=False,
                  description="Role-playing games where players take on the roles of characters and engage in story-driven adventures.")
    db.add(genre)
    genre = Genre(id=2, name='Platformer', rage_inducing=True, action_packed=False, skill_based=True,
                  description="Games where players jump or climb on platforms to complete levels, often challenging and skill-based.")
    db.add(genre)
    genre = Genre(id=3, name='FPS', rage_inducing=True, action_packed=True, skill_based=True,
                  description="First-person shooter games where players engage in combat from a first-person perspective.")
    db.add(genre)
    genre = Genre(id=4, name='Horror', rage_inducing=True, action_packed=False, skill_based=False,
                  description="Games designed to create fear and suspense, often with psychological or supernatural elements.")
    db.add(genre)
    genre = Genre(id=5, name='Puzzle', rage_inducing=False, action_packed=False, skill_based=True,
                  description="Games that challenge players to solve puzzles, requiring logic and critical thinking.")
    db.add(genre)
    genre = Genre(id=6, name='Simulation', rage_inducing=False, action_packed=False, skill_based=True,
                  description="Games that simulate real-world activities, often with a focus on accuracy and strategy.")
    db.add(genre)
    genre = Genre(id=7, name='Fantasy', rage_inducing=False, action_packed=True, skill_based=False,
                  description="Games set in a fantastical world with magical elements and often epic storylines.")
    db.add(genre)
    genre = Genre(id=8, name='Roguelike', rage_inducing=True, action_packed=True, skill_based=False,
                  description="Games characterized by procedural generation, permadeath, and high difficulty.")
    db.add(genre)
    genre = Genre(id=9, name='Adventure', rage_inducing=False, action_packed=True, skill_based=True,
                  description="Games focused on exploration and solving puzzles, often with a strong narrative element.")
    db.add(genre)
    db.commit()
    db.refresh(genre)
    db.close()