import pytest
from fastapi.testclient import TestClient
from app.database import get_db
from test.test_database import add_genres, override_get_db, test_engine, TestSessionLocal
from app.models import Base, Game, Genre
from sqlalchemy import inspect
from main import app

# Override get_db for test client
app.dependency_overrides[get_db] = override_get_db

test = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    print("Setting up")
    Base.metadata.drop_all(bind=test_engine)  # Clean up database
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    print("Existing Test Tables:", tables)
    if db.query(Genre).count() == 0:
        print("Adding genres to Test Database")
        add_genres(db)
    db.commit()
    print(db)

    yield

    print("Tearing down")
    db.close()
    Base.metadata.drop_all(bind=test_engine)


def test_endpoint_recommendation():
    # Arrange: Set up a test database session
    db = TestSessionLocal()

    # Fetch the FPS genre (ID 3) from the database
    fps_genre = db.query(Genre).filter(Genre.id == 3).first()

    if not fps_genre:
        raise ValueError("FPS genre with ID 3 not found!")

    # Create Game instances
    game1 = Game(id=1, name='The Division 2', mature_themes=True, open_world=True, multiplayer=True,
                 length_in_hours=60,
                 description="A third-person shooter set in an open-world, focusing on cooperative play and combat.")
    game2 = Game(id=2, name='Grand Theft Auto V', mature_themes=True, open_world=True, multiplayer=True,
                 length_in_hours=80, description="An open-world crime game with multiple protagonists.")

    # Link the games to the FPS genre
    game1.genres.append(fps_genre)  # Grand Theft Auto V -> FPS
    game2.genres.append(fps_genre)  # The Division 2 -> FPS

    # Add and commit to the session
    db.add(game1)
    db.add(game2)
    db.commit()
    db.close()

    # Act
    response = test.get("/recommendation?rage_inducing=1&action_packed=1&skill_based=1&mature_themes=1&open_world=1&multiplayer=1")

    # Assert
    assert response.status_code == 200
    response_data = response.json()

    # Define two valid expected orders
    expected_response_1 = {
        "Recommendations": [
            {
                "Name": "FPS",
                "Description": "First-person shooter games where players engage in combat from a first-person perspective.",
                "Games": [
                    {"Name": "Grand Theft Auto V",
                     "Description": "An open-world crime game with multiple protagonists."},
                    {"Name": "The Division 2",
                     "Description": "A third-person shooter set in an open-world, focusing on cooperative play and combat."}
                ]
            }
        ]
    }

    expected_response_2 = {
        "Recommendations": [
            {
                "Name": "FPS",
                "Description": "First-person shooter games where players engage in combat from a first-person perspective.",
                "Games": [
                    {"Name": "The Division 2",
                     "Description": "A third-person shooter set in an open-world, focusing on cooperative play and combat."},
                    {"Name": "Grand Theft Auto V",
                     "Description": "An open-world crime game with multiple protagonists."}
                ]
            }
        ]
    }

    # Assert that the response matches either of the expected responses
    assert response_data == expected_response_1 or response_data == expected_response_2

def test_endpoint_genres():
    #Arrange
    db = TestSessionLocal()
    genres = db.query(Genre).all()
    print(genres)

    # Act
    response = test.get('/genres')

    # Assert
    assert response.status_code == 200
    assert response.json() == {"data":[{"rage_inducing":False,"name":"RPG","skill_based":False,"id":1,"action_packed":False,"description":"Role-playing games where players take on the roles of characters and engage in story-driven adventures."},{"rage_inducing":True,"name":"Platformer","skill_based":True,"id":2,"action_packed":False,"description":"Games where players jump or climb on platforms to complete levels, often challenging and skill-based."},{"rage_inducing":True,"name":"FPS","skill_based":True,"id":3,"action_packed":True,"description":"First-person shooter games where players engage in combat from a first-person perspective."},{"rage_inducing":True,"name":"Horror","skill_based":False,"id":4,"action_packed":False,"description":"Games designed to create fear and suspense, often with psychological or supernatural elements."},{"rage_inducing":False,"name":"Puzzle","skill_based":True,"id":5,"action_packed":False,"description":"Games that challenge players to solve puzzles, requiring logic and critical thinking."},{"rage_inducing":False,"name":"Simulation","skill_based":True,"id":6,"action_packed":False,"description":"Games that simulate real-world activities, often with a focus on accuracy and strategy."},{"rage_inducing":False,"name":"Fantasy","skill_based":False,"id":7,"action_packed":True,"description":"Games set in a fantastical world with magical elements and often epic storylines."},{"rage_inducing":True,"name":"Roguelike","skill_based":False,"id":8,"action_packed":True,"description":"Games characterized by procedural generation, permadeath, and high difficulty."},{"rage_inducing":False,"name":"Adventure","skill_based":True,"id":9,"action_packed":True,"description":"Games focused on exploration and solving puzzles, often with a strong narrative element."}]}

def test_endpoint_games():
    # Arrange
    db = TestSessionLocal()
    game = Game(id=0, name="Elden Ring", mature_themes=True, multiplayer=True,
                description="An open-world action RPG with punishing combat and deep lore.", open_world=True,
                length_in_hours=120)
    db.add(game)
    game = Game(id=1, name="Red Dead Redemption 2", mature_themes=True, multiplayer=False,
                description="A vast open-world western game with deep storytelling and realism.", open_world=True,
                length_in_hours=150)
    db.add(game)
    game = Game(id=2, name="The Witcher 3", mature_themes=True, multiplayer=False,
                description="An open-world RPG with rich storytelling, deep choices, and immersive combat.",
                open_world=True, length_in_hours=100)
    db.add(game)
    db.commit()
    db.close()


    # Act
    response = test.get('/games')

    # Assert
    assert response.status_code == 200
    assert response.json() == { "data": [
    {
        "id": 0,
        "mature_themes": True,
        "multiplayer": True,
        "description": "An open-world action RPG with punishing combat and deep lore.",
        "open_world": True,
        "name": "Elden Ring",
        "length_in_hours": 120
    },
    {
        "id": 1,
        "mature_themes": True,
        "multiplayer": False,
        "description": "A vast open-world western game with deep storytelling and realism.",
        "open_world": True,
        "name": "Red Dead Redemption 2",
        "length_in_hours": 150
    },
    {
        "id": 2,
        "mature_themes": True,
        "multiplayer": False,
        "description": "An open-world RPG with rich storytelling, deep choices, and immersive combat.",
        "open_world": True,
        "name": "The Witcher 3",
        "length_in_hours": 100
    }
]
}


def test_no_games():
    response = test.get("/recommendation?rage_inducing=1&action_packed=0&skill_based=1&mature_themes=1&open_world=true&multiplayer=1")
    assert response.status_code == 200
    assert response.json() == {"Recommendations":[{"Name":"Platformer","Description":"Games where players jump or climb on platforms to complete levels, often challenging and skill-based.","Games":["No games found"]}]}

