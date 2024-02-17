import uuid
from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: str
    description: str


class SCategory(CreateCategory):
    id: uuid.UUID


class UpdateCategory(BaseModel):
    ...    