from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welkom bij GameRecommender"}

# class Genre(BaseModel):
# name: str
# price: float
# is_in_stock: bool = True

