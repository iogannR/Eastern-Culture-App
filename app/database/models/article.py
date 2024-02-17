import uuid
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from app.database.base import Base

# Articless ORM-model
class Article(Base):
    __tablename__ = "articles"
    
    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String(64), nullable=False)
    annotation = sa.Column(sa.Text, default="Info Article")
    content = sa.Column(sa.Text, nullable=False)
    image_id = sa.Column(sa.Integer)
    
    category_id = sa.Column(sa.UUID(as_uuid=True), sa.ForeignKey("categories.id"))
    category = sa_orm.relationship("Category", back_populates="article")