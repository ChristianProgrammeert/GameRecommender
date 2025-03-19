from fastapi import FastAPI
app = FastAPI()

def compute_genres(genres,rage,action_pack,skill_base):
    """Loops through genres and compares its characteristics with input. Returns matches."""
    result = []
    for  genre in genres:
        if genre.rage_inducing == rage and genre.action_packed == action_pack and genre.skill_based == skill_base:
            result.append(genre)
    return result

def compute_games(games,mature_themes,open_world_,multiplayer):
    """Loops through games and compares its characteristics with input. Returns matches."""
    result = []
    for game in games:
        if game.mature_themes == mature_themes and game.open_world == open_world_ and game.multiplayer == multiplayer:
            result.append(game)
    return result

def link_games_genres(titles, names, connection_table):
    """Links matching genres with matching games. Returns matches in a readable json format."""
    result = []
    for genre in names:
        genre_info = {
            "Name": genre.name,
            "Description": genre.description,
            "Games": []
        }
        for connection in connection_table:
            if connection.genre_id == genre.id:
                game_id = connection.game_id
                for game in titles:
                    if game.id == game_id:
                        game_info = {
                            "Name": game.name,
                            "Description": game.description,
                        }
                        genre_info["Games"].append(game_info)
        if len(genre_info["Games"]) == 0:
            genre_info["Games"].append("No games found")
        result.append(genre_info)
    return result
