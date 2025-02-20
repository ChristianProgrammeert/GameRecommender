from fastapi import HTTPException

unexpected_input_error_message = "Please input your answers with ?answers={Your Answers}"

def raise_input_error():
    raise HTTPException(status_code=400, detail = unexpected_input_error_message)

def raise_request_error(message):
    raise HTTPException(status_code=422, detail=message)