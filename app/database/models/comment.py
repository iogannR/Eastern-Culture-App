import datetime
import uuid
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from app.database.base import Base

#  Articles comments ORM-model
class Comment(Base):
    __tablename__ = "comments"
    
    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = sa.Column(sa.Text)
    created_at = sa.Column(
        sa.DateTime(timezone=True), 
        default=datetime.datetime.utcnow() \
            + datetime.timedelta(hours=3)
    )
    
    article_id = sa.Column(sa.UUID(as_uuid=True), sa.ForeignKey("articles.id"))
    article = sa_orm.relationship("Article", back_populates="comments")