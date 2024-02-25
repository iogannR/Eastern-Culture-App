import fastapi
import sqlalchemy.ext.asyncio as sa_ext_asyncio

import uuid

from app.api.schemas.articles import CreateArticle, SArticle
from app.database.models.article import Article
from app.database.service.article import ArticlesService

from app.database.session import get_session


router = fastapi.APIRouter(
    prefix="/articles",
    tags=["Статьи"]
)


@router.get("/get-articles-by-category-name/{category_name}")
async def get_articles_by_category_name(
    category_name, session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> list[SArticle]:
    articles_service = ArticlesService(Article)
    result = await articles_service.get_articles_by_category_name(
        session=session,
        category_name=category_name
    )
    if result == []:
        raise fastapi.HTTPException(status_code=404, detail="Articles not found!")
    else:
        return result


@router.get("/get-articles")
async def get_articles(
    session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> list[SArticle]:
    articles_service = ArticlesService(Article)
    result = await articles_service.get_all_instances(session=session)
    return result


@router.get("/get-article-by-id/{article_id}")
async def get_article_by_id(
    article_id: uuid.UUID, 
    session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> SArticle:
    articles_service = ArticlesService(Article)
    result = await articles_service.get_instance_by_id(
        session=session, 
        instance_id=article_id
    )
    return result
    

@router.post("/create-article")
async def create_article(
    payload: CreateArticle, 
    session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> SArticle:
    articles_service = ArticlesService(Article)
    result = await articles_service.create_instance(
        session=session, 
        payload=payload
    )
    return result

