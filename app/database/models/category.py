import uuid
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from app.database.base import Base

# Articles category ORM-model
class Category(Base):
    __tablename__ = "categories"
    
    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(64), unique=True, nullable=False)
    description = sa.Column(sa.String)
    
    article = sa_orm.relationship("Article", back_populates="category")