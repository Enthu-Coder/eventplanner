from email.mime import image
from msilib import schema
from turtle import title
from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book launch",
                "image": "hppts://linktomyimage.com/image.png",
                "description": "we will be discussing the contents of the FastAPi book in this event. Ensure to come with your own copy of gifts. !",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
