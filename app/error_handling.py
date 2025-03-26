from fastapi import HTTPException

BOOL_ERROR_MESSAGE = "ValueError: boolean values expected [True,False,1,0]. rage_inducing | action_packed | skill_based | mature_themes | open_world | multiplayer"

def raise_request_error(message):
    """Raises HTTPError with code 400 for bad input with a custom message."""
    raise HTTPException(status_code=400, detail=message)

def raise_boolean_error():
    """Raises HTTPError with code 400 for when input values aren't booleans."""
    raise HTTPException(status_code=400, detail=BOOL_ERROR_MESSAGE)