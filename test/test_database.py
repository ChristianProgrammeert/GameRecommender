from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Genre


def add_genres(db):
    # Create a list of Genre instances
    genres = [
        Genre(id=1, name='RPG', rage_inducing=False, action_packed=False, skill_based=False,
              description="Role-playing games where players take on the roles of characters and engage in story-driven adventures."),
        Genre(id=2, name='Platformer', rage_inducing=True, action_packed=False, skill_based=True,
              description="Games where players jump or climb on platforms to complete levels, often challenging and skill-based."),
        Genre(id=3, name='FPS', rage_inducing=True, action_packed=True, skill_based=True,
              description="First-person shooter games where players engage in combat from a first-person perspective."),
        Genre(id=4, name='Horror', rage_inducing=True, action_packed=False, skill_based=False,
              description="Games designed to create fear and suspense, often with psychological or supernatural elements."),
        Genre(id=5, name='Puzzle', rage_inducing=False, action_packed=False, skill_based=True,
              description="Games that challenge players to solve puzzles, requiring logic and critical thinking."),
        Genre(id=6, name='Simulation', rage_inducing=False, action_packed=False, skill_based=True,
              description="Games that simulate real-world activities, often with a focus on accuracy and strategy."),
        Genre(id=7, name='Fantasy', rage_inducing=False, action_packed=True, skill_based=False,
              description="Games set in a fantastical world with magical elements and often epic storylines."),
        Genre(id=8, name='Roguelike', rage_inducing=True, action_packed=True, skill_based=False,
              description="Games characterized by procedural generation, permadeath, and high difficulty."),
        Genre(id=9, name='Adventure', rage_inducing=False, action_packed=True, skill_based=True,
              description="Games focused on exploration and solving puzzles, often with a strong narrative element.")
    ]

    # Add all genres at once
    db.add_all(genres)
    db.commit()
    db.close()
    print("Genres added successfully")

# For testing purposes, set a file-based SQLite database
DATABASE_URL = "sqlite:///./test.db"


print("Using SQLite in-memory database for testing")
test_engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Base.metadata.create_all(test_engine)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

inspector = inspect(test_engine)
tables = inspector.get_table_names()
print("Existing Test Tables:", tables)
# Controleer of er rijen in de tabellen staan

def override_get_db():
    print("Using test db")
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()



