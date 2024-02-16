import uuid
from pydantic import BaseModel


class CreateArticle(BaseModel):
    title: str
    annotation: str
    content: str
    image_id: int
    category_id: uuid.UUID


class SArticle(CreateArticle):
    id: uuid.UUID


class UpdateArticle(BaseModel):
    ...    
