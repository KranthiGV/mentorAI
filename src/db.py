from pydantic import BaseModel

class Mentor(BaseModel):
    id: str
    name: str
    photo: str

class Message(BaseModel):
    mentor_id: str
    msg: str


class Database:
    def __init__(self):
        self.mentors = {
            'h9ghxb2': Mentor(id='h9ghxb2', name='Elon Musk', photo='https://example.com/john-doe.jpg'),
            'p2gb7f0': Mentor(id='p2gb7f0', name='Taylor Swift', photo='https://example.com/jane-doe.jpg'),
        }

    def get_mentors(self) -> list[Mentor]:
        return list(self.mentors.values())