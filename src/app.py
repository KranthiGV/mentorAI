import os
from modal import Stub, asgi_app, Secret, Image
from fastapi import FastAPI, Request
from db import Mentor, Message, Database
from anthropic import Anthropic
from fastapi.middleware.cors import CORSMiddleware

image = (
    Image.debian_slim()
    .pip_install(
        "anthropic",
    )
)


stub = Stub('mentorAI', image=image, secrets=[Secret.from_name("mentorai")])

web_app = FastAPI()
web_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


db = Database()

@web_app.get("/")
def default():
    return "Oops! You are lost."

@web_app.get('/mentors')
def get_mentors() -> list[Mentor]:
    return db.get_mentors()

@web_app.get('/mentors/{mentor_id}')
def get_mentor(mentor_id: str) -> Mentor:
    return db.mentors.get(mentor_id)

@web_app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    mentor_id = body['mentor_id']
    mentor_name = db.mentors.get(mentor_id).name
    question = body['msg']
    API_KEY = os.environ["ANTHROPIC_API_KEY"]

    client = Anthropic(api_key=API_KEY)

    message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"Hello, Claude. You are an expert role playing AI. You are now {mentor_name}. I have a question for you. Answer in less than 60 words. Do not mention any actions such as <actions>*clears throat* *puts on a persona* </actions>. The question is: {question}",
        }
    ],
    model="claude-3-opus-20240229",
    )



    return message.content

@stub.function()
@asgi_app()
def fastapi_app():
    return web_app

if __name__ == '__main__':
    stub.deploy()