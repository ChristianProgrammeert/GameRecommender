from unittest.mock import MagicMock
from app.algorithm import compute_genres, compute_games,link_games_genres



def test_compute_genres():
    mock_genres = []
    mock_genre1 = MagicMock()
    mock_genre2 = MagicMock()
    mock_genre3 = MagicMock()

    mock_genre1.name = "fps"
    mock_genre1.rage_inducing = True
    mock_genre1.action_packed = True
    mock_genre1.skill_based = True

    mock_genre2.name = "horror"
    mock_genre2.rage_inducing = True
    mock_genre2.action_packed = False
    mock_genre2.skill_based = False

    mock_genre3.name = "puzzle"
    mock_genre3.rage_inducing = False
    mock_genre3.action_packed = False
    mock_genre3.skill_based = True

    mock_genres.append(mock_genre1)
    mock_genres.append(mock_genre2)
    mock_genres.append(mock_genre3)


    mock_db = MagicMock()
    mock_db.query().all.return_value = mock_genres
    result = compute_genres(genres =  mock_genres, action_pack = True, skill_base = True, rage = True)

    assert result != []
    assert result == [mock_genre1]



def test_compute_games():
    mock_games = []
    mock_game1 = MagicMock()
    mock_game2 = MagicMock()
    mock_game3 = MagicMock()

    mock_game1.name = "Elden Ring"
    mock_game1.mature_themes = True
    mock_game1.open_world = True
    mock_game1.multiplayer = True

    mock_game2.name = "Halo"
    mock_game2.mature_themes = True
    mock_game2.open_world = False
    mock_game2.multiplayer = True

    mock_game3.name = "Tetris"
    mock_game3.mature_themes = False
    mock_game3.open_world = False
    mock_game3.multiplayer = False

    mock_games.append(mock_game1)
    mock_games.append(mock_game2)
    mock_games.append(mock_game3)

    mock_db = MagicMock()
    mock_db.query().all.return_value = mock_games
    result = compute_games(games = mock_games, mature_themes = True, open_world_ = True, multiplayer = True)

    assert result != []
    assert result == [mock_game1]

def test_link_games_genres():
    mock_game1 = MagicMock()
    mock_genre1 = MagicMock()
    mock_genre2 = MagicMock()
    mock_connection2 = MagicMock()
    mock_db = MagicMock()

    mock_connection1 = MagicMock()
    mock_game1.id = 1
    mock_game1.name = "Halo"
    mock_game1.description = "A game about shooting aliens"


    mock_genre1.id = 1
    mock_genre1.name = "fps"
    mock_genre1.description = "A genre about shooting things"


    mock_genre2.id = 2
    mock_genre2.name = "horror"
    mock_genre2.description = "A genre about being scared"

    mock_connection1.game_id = 1
    mock_connection1.genre_id = 1


    mock_connection2.game_id = 1
    mock_connection2.genre_id = 2

    mock_games = [mock_game1]
    mock_genres = [mock_genre1, mock_genre2]
    mock_links = [mock_connection1, mock_connection2]



    mock_db.query().all.side_effect = [mock_games, mock_genres, mock_links]
    result = link_games_genres(titles=mock_games, names=mock_genres, connection_table=mock_links)


    # Assertions
    assert result == [
        {
            "Name": "fps",
            "Description": "A genre about shooting things",
            "Games": [{"Name": "Halo", "Description": "A game about shooting aliens"}]
        },
        {
            "Name": "horror",
            "Description": "A genre about being scared",
            "Games": [{"Name": "Halo", "Description": "A game about shooting aliens"}]
        }
    ]

