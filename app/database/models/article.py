from uuid import uuid4
from sqlalchemy import Column, ForeignKey, Integer, String, UUID, Text
from sqlalchemy.orm import relationship

from app.database.base import Base

# Articless ORM-model
class Article(Base):
    __tablename__ = "articles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(64), nullable=False)
    annotation = Column(Text, default="Info Article")
    content = Column(Text, nullable=False)
    image_id = Column(Integer)
    
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
    category = relationship("Category", back_populates="article")