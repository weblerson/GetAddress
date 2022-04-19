from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/states")
def get_states():
    with open("States.json", "r", encoding = "utf8") as states:
        return json.loads(states.read())

@app.get('/cities')
def get_cities():
    with open("Cities.json", "r", encoding = "utf8") as cities:
        return json.loads(cities.read())
