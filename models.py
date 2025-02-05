from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String(35), nullable=False, unique=True)
    mature_themes = Column(Boolean, default=False)
    open_world = Column(Boolean, default=False)
    skill_based = Column(Boolean, default=False)
    length_in_hours = Column(Integer)
    description = Column(String(255), nullable=True)

    genres = relationship("Genre", secondary="games_genre", back_populates="games")

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    rage_inducing = Column(Boolean, default=False)
    action_packed = Column(Boolean, default=False)
    multiplayer = Column(Boolean, default=False)
    description = Column(String(255), nullable=True)

    games = relationship("Game", secondary="games_genre", back_populates="genres")

class GameGenre(Base):
    __tablename__ = 'games_genre'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id', ondelete='CASCADE'))
    genre_id = Column(Integer, ForeignKey('genres.id', ondelete='CASCADE'))