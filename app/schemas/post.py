from pydantic import BaseModel
from datetime import datetime

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    image: str | None
    likes: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostUpdate(BaseModel):
    title: str | None
    content: str | None