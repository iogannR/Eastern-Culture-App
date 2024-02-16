import uuid
from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship
from app.database.base import Base

# Articles category ORM-model
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(String)
    
    article = relationship("Article", back_populates="category")