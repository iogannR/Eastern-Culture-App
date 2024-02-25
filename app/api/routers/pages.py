import fastapi
import fastapi.templating
import fastapi.responses

import uuid

from app.api.routers.articles import get_articles_by_category_name, get_article_by_id
from app.api.routers.categories import get_categories

router = fastapi.APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]    
)

templates = fastapi.templating.Jinja2Templates(
    directory="app/templates"
)

@router.get("/home-page", response_class=fastapi.responses.HTMLResponse)
async def home_page(
    request: fastapi.Request, 
    categories=fastapi.Depends(get_categories)
):
    return templates.TemplateResponse(
        "home.html", 
        context={
            "request": request, 
            "categories": categories
        }
    )
    
@router.get("/articles/{category_name}", response_class=fastapi.responses.HTMLResponse)
async def get_articles_by_category_name_on_page(
    request: fastapi.Request,
    category_name: str,
    articles=fastapi.Depends(get_articles_by_category_name)
):
    return templates.TemplateResponse(
        "articles.html",
        context={
            "request": request,
            "articles": articles,
            "category_name": category_name
        }
    )
    
@router.get(
    "/articles/{category_name}/article/{article_id}", 
    response_class=fastapi.responses.HTMLResponse
)
async def read_article(
    request: fastapi.Request,
    category_name: str,
    article_id: uuid.UUID,
    article = fastapi.Depends(get_article_by_id)
):
    return templates.TemplateResponse(
        "single_article.html",
        context={
            "request": request,
            "category_name": category_name,
            "article_id": article_id,
            "article": article
        }
    )