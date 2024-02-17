import sqlalchemy as sa
import sqlalchemy.ext.asyncio as sa_ext_asyncio

from app.api.schemas.articles import (
    CreateArticle, PartialUpdateArticle, SArticle, UpdateArticle
)
from app.database.models.article import Article
from app.database.models.category import Category
from app.database.service.base import BaseService


# Service class for articles model
class ArticlesService(BaseService[SArticle, CreateArticle, UpdateArticle, PartialUpdateArticle]):
    
    async def get_articles_by_category_name(
        self, session: sa_ext_asyncio.AsyncSession, category_name: str
    ) -> list[SArticle]:
        query = sa.select(Article).join(Category).where(Category.name == category_name)
        result = await session.execute(query)
        return result.scalars().all()