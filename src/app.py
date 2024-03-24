import os
from modal import Stub, asgi_app, Secret
from fastapi import FastAPI
from db import Mentor, Database

stub = Stub('mentorAI', secrets=[Secret.from_name("mentorai")])

web_app = FastAPI()
db = Database()

@web_app.get("/")
def default():
    return "Oops! You are lost."

@web_app.get('/mentors')
def get_mentors() -> list[Mentor]:
    return db.get_mentors()

@web_app.get('/mentors/{mentor_id}')
def get_mentor(mentor_id: str) -> Mentor:
    return db.get_mentor(mentor_id)

@web_app.post("/chat")
def chat():
    return os.environ["ANTHROPIC_API_KEY"]

@stub.function()
@asgi_app()
def fastapi_app():
    return web_app

if __name__ == '__main__':
    stub.deploy()