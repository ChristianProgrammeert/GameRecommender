import pytest
from fastapi.testclient import TestClient
from sqlalchemy import inspect
from app.database import get_db
from app.queries import add_genres
from app.models import Base, Game, Genre
from main import app
from test.test_database import test_engine, override_get_db, TestSessionLocal


test = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    print("Setting up")
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    print("Existing test Tables:", tables)

    yield
    print("Tearing down")
    Base.metadata.drop_all(test_engine)

def test_endpoint_recommendation():
    # Arrange
    with TestSessionLocal() as db:
        game = Game(id=1, name='Grand Theft Auto V', mature_themes= True, open_world=True, multiplayer=True,
        length_in_hours=80, description='An open-world crime game with multiple protagonists.')
        db.add(game)
        db.commit()
        game = Game(id=2, name='The Division 2', mature_themes=True, open_world=True, multiplayer=True,length_in_hours=60, description='A third-person shooter set in an open-world, focusing on cooperative play and combat.')
        db.add(game)
        db.commit()

        games = db.query(Game).all()
        print(games)

        db.close()

    #Act
    response = test.get("/recommendation?answers=111111")

    #Assert
    assert response.status_code == 200
    assert response.json() == { "Recommendations": [
        {
            "Games": [
                {
                    "Name": "Grand Theft Auto V",
                    "Description": "An open-world crime game with multiple protagonists."
                },
                {
                    "Name": "The Division 2",
                    "Description": "A third-person shooter set in an open-world, focusing on cooperative play and combat."
                }
            ]
        }
    ]
}

def test_endpoint_genres():
    #Arrange
    add_genres(TestSessionLocal)

    with TestSessionLocal() as db:
        genres = db.query(Genre).all()
        print(genres)

    # Act
    response = test.get('/genres')

    # Assert
    assert response.status_code == 200
    assert response.json() == {
    "data": [
        {
            "action_packed": True,
            "id": 7,
            "description": "Games set in a fantastical world with magical elements and often epic storylines.",
            "rage_inducing": False,
            "name": "Fantasy",
            "skill_based": False
        },
        {
            "action_packed": False,
            "id": 5,
            "description": "Games that challenge players to solve puzzles, requiring logic and critical thinking.",
            "rage_inducing": False,
            "name": "Puzzle",
            "skill_based": True
        },
        {
            "action_packed": False,
            "id": 4,
            "description": "Games designed to create fear and suspense, often with psychological or supernatural elements.",
            "rage_inducing": True,
            "name": "Horror",
            "skill_based": False
        },
        {
            "action_packed": False,
            "id": 6,
            "description": "Games that simulate real-world activities, often with a focus on accuracy and strategy.",
            "rage_inducing": False,
            "name": "Simulation",
            "skill_based": True
        },
        {
            "action_packed": True,
            "id": 3,
            "description": "First-person shooter games where players engage in combat from a first-person perspective.",
            "rage_inducing": True,
            "name": "FPS",
            "skill_based": True
        },
        {
            "action_packed": False,
            "id": 1,
            "description": "Role-playing games where players take on the roles of characters and engage in story-driven adventures.",
            "rage_inducing": False,
            "name": "RPG",
            "skill_based": False
        },
        {
            "action_packed": False,
            "id": 2,
            "description": "Games where players jump or climb on platforms to complete levels, often challenging and skill-based.",
            "rage_inducing": True,
            "name": "Platformer",
            "skill_based": True
        },
        {
            "action_packed": True,
            "id": 8,
            "description": "Games characterized by procedural generation, permadeath, and high difficulty.",
            "rage_inducing": True,
            "name": "Roguelike",
            "skill_based": False
        },
        {
            "action_packed": True,
            "id": 9,
            "description": "Games focused on exploration and solving puzzles, often with a strong narrative element.",
            "rage_inducing": False,
            "name": "Adventure",
            "skill_based": True
        }
    ]
}

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

    with TestSessionLocal() as db:
        genres = db.query(Genre).all()
        print(genres)  # Should show the inserted book

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
    response = test.get("/recommendation?answer=101111")
    assert response.status_code == 200
    assert response.json() == {"Recommendations":
        [
            {
                "Name": "platformer",
                "Description": "Games where players jump or climb through platforms to complete levels, often challenging and skill-based.",
                "Games": [
                    "No games found"
                ]
            }
        ]
    }

