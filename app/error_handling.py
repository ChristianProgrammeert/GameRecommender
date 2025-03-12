from fastapi import HTTPException

BOOL_ERROR_MESSAGE = "ValueError: boolean values expected [True,False,1,0]. rage_inducing | action_packed | skill_based | mature_themes | open_world | multiplayer"

def raise_request_error(message):
    raise HTTPException(status_code=422, detail=message)

def raise_boolean_error():
    raise HTTPException(status_code=422, detail=BOOL_ERROR_MESSAGE)