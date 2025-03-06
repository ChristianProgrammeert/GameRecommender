from unittest.mock import MagicMock
from app.algorithm import compute_genres



def test_compute_genres():
    mock_genres = []
    mock_genre1 = MagicMock()
    mock_genre2 = MagicMock()
    mock_genre3 = MagicMock()
    mock_genre1.name = "fps"
    mock_genre2.name = "horror"
    mock_genre3.name = "puzzle"
    mock_genre1.rage_inducing = True
    mock_genre2.rage_inducing = True
    mock_genre3.rage_inducing = False
    mock_genre1.action_packed = True
    mock_genre2.action_packed = False
    mock_genre3.action_packed = False
    mock_genre1.skill_based = True
    mock_genre2.skill_based = False
    mock_genre3.skill_based = True
    mock_genres.append(mock_genre1)
    mock_genres.append(mock_genre2)
    mock_genres.append(mock_genre3)


    mock_db = MagicMock()
    mock_db.query().all.return_value = mock_genres
    result = compute_genres(genres =  mock_genres, action_pack = True, skill_base = True, rage = True)

    assert result != []
    assert result == [mock_genre1]

