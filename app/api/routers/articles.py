import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.articles import CreateArticle, SArticle
from app.database.service.article import ArticlesService

from app.database.session import get_session


router = APIRouter(
    prefix="/articles",
    tags=["Статьи"]
)


@router.get("/{category_name}")
async def get_articles_by_category_name(category_name, session: AsyncSession = Depends(get_session)) -> list[SArticle]:
    articles_service = ArticlesService()
    result = await articles_service.get_articles_by_category_name(
        session=session,
        category_name=category_name
    )
    return result


@router.get("/get-articles")
async def get_articles(session: AsyncSession = Depends(get_session)) -> list[SArticle]:
    articles_service = ArticlesService()
    result = await articles_service.get_all_instances(session=session)
    return result


@router.post("/create-articles")
async def create_article(
    payload: CreateArticle, 
    session: AsyncSession = Depends(get_session)
) -> SArticle:
    articles_service = ArticlesService()
    result = await articles_service.create_instance(
        session=session, 
        payload=payload
    )
    return result