from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/")
async def root():
    return {"message": "Hello LIG-27"}

