import uuid
from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: str
    description: str


class SCategory(CreateCategory):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class UpdateCategory(BaseModel):
    name: str
    description: str
    
    class Config:
        from_attributes = True
        
        
class PartialUpdateCategory(BaseModel):
    name: str | None
    description: str | None
    
    class Config:
        from_attributes = True