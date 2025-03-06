from unittest.mock import MagicMock
from app.algorithm import compute_games

def test_compute_games():
    mock_games = []
    mock_game1 = MagicMock()
    mock_game2 = MagicMock()
    mock_game3 = MagicMock()
    mock_game1.name = "Elden Ring"
    mock_game2.name = "Halo"
    mock_game3.name = "Tetris"
    mock_game1.mature_themes = True
    mock_game2.mature_themes = True
    mock_game3.mature_themes = False
    mock_game1.open_world = True
    mock_game2.open_world = False
    mock_game3.open_world = False
    mock_game1.multiplayer = True
    mock_game2.multiplayer = True
    mock_game3.multiplayer = False
    mock_games.append(mock_game1)
    mock_games.append(mock_game2)
    mock_games.append(mock_game3)

    mock_db = MagicMock()
    mock_db.query().all.return_value = mock_games
    result = compute_games(games = mock_games, mature_themes = True, open_world_ = True, multiplayer = True)

    assert result != []
    assert result == [mock_game1]