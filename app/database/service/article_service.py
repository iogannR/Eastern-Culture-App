from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.articles_schemas import SArticle

from app.database.models.article import Article
from app.database.models.category import Category
from app.database.service.base import BaseService

# Service class for articles model
class ArticlesService(BaseService):
    model = Article
    
    async def get_articles_by_category_name(self, session: AsyncSession, category_name: str) -> list[SArticle]:
        stmt = select(Article).join(Category).where(Category.name == category_name)
        result = await session.execute(stmt)
        return result.scalars().all()
