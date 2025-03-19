import app.queries as query
from unittest.mock import MagicMock

def init_mock_db():
    mock_entries = []
    mock_entry_one = MagicMock()
    mock_entry_two = MagicMock()
    mock_entry_three = MagicMock()

    mock_entry_one.id = 1;mock_entry_two.id = 2;mock_entry_three.id = 3

    mock_entry_one.name = "entry_1";mock_entry_two.name = "entry_2";mock_entry_three.name = "entry_3"
    mock_entries.append(mock_entry_one);mock_entries.append(mock_entry_two);mock_entries.append(mock_entry_three)

    mock_db = MagicMock()
    mock_db.query().all.return_value = mock_entries
    return mock_db

def test_get_genres():
    mock_db = init_mock_db()
    entries = query.get_genres(mock_db)
    for _ in range(len(entries)):
        assert entries[_].id == _+1
        assert entries[_].name == f"entry_{_+1}"

def test_get_movies():
    mock_db = init_mock_db()
    entries = query.get_games(mock_db)
    for _ in range(len(entries)):
        assert entries[_].id == _+1
        assert entries[_].name == f"entry_{_+1}"

def test_get_connection_table():
    mock_db = init_mock_db()
    entries = query.get_connection_table(mock_db)
    for _ in range(len(entries)):
        assert entries[_].id == _+1
        assert entries[_].name == f"entry_{_+1}"
