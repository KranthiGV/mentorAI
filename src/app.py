from modal import Stub, asgi_app
from fastapi import FastAPI, Response
from db import Mentor, Database

stub = Stub('mentorAI')

web_app = FastAPI()
db = Database()



@web_app.get("/")
def default():
    return "Oops! You are lost."


@web_app.get('/mentors')
def get_mentors() -> list[Mentor]:
    return db.get_mentors()



@stub.function()
@asgi_app()
def fastapi_app():
    return web_app

if __name__ == '__main__':
    stub.deploy()