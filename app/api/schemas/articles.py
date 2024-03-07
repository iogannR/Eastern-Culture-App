import uuid
from pydantic import BaseModel


class CreateArticle(BaseModel):
    title: str
    annotation: str
    content: str
    main_image_id: int
    single_image_id: int
    category_id: uuid.UUID


class SArticle(CreateArticle):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class UpdateArticle(BaseModel):
    title: str
    annotation: str
    content: str
    
    class Config:
        from_attributes = True

class PartialUpdateArticle(BaseModel):
    title: str | None
    annotation: str | None
    content: str | None
    
    class Config:
        from_attributes = True