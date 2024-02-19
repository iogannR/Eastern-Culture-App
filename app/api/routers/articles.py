import fastapi
import sqlalchemy.ext.asyncio as sa_ext_asyncio

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
    return result


@router.get("/get-articles")
async def get_articles(
    session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> list[SArticle]:
    articles_service = ArticlesService(Article)
    result = await articles_service.get_all_instances(session=session)
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