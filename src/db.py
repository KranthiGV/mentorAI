from pydantic import BaseModel

class Mentor(BaseModel):
    id: str
    name: str
    photo: str




class Database:
    def __init__(self):
        self.mentors = {
            'h9ghxb2': Mentor(id='h9ghxb2', name='John Doe', photo='https://example.com/john-doe.jpg'),
            'p2gb7f0': Mentor(id='p2gb7f0', name='Jane Bpi', photo='https://example.com/jane-doe.jpg'),
        }

    def get_mentors(self) -> list[Mentor]:
        return list(self.mentors.values())