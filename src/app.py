from pydantic import BaseModel
from modal import Stub, asgi_app
from fastapi import FastAPI


stub = Stub('mentorAI')

web_app = FastAPI()


class Mentor(BaseModel):
    id: str
    name: str
    photo: str

@web_app.get("/")
def default():
    return "Oops! You are lost."


@web_app.get('/mentors')
def get_mentors() -> list[Mentor]:
    return [
        Mentor(id='h9ghxb2', name='John Doe', photo='https://example.com/john-doe.jpg'),
        Mentor(id='p2gb7f0', name='Jane Doe', photo='https://example.com/jane-doe.jpg'),
    ]



@stub.function()
@asgi_app()
def fastapi_app():
    return web_app

if __name__ == '__main__':
    stub.deploy()