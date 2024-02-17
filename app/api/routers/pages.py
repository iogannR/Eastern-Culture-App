import fastapi
import fastapi.templating
import fastapi.responses
from app.api.routers.articles import get_articles_by_category_name

from app.api.routers.categories import get_categories

router = fastapi.APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]    
)

templates = fastapi.templating.Jinja2Templates(
    directory="app/templates"
)

@router.get("", response_class=fastapi.responses.HTMLResponse)
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
    articles=fastapi.Depends(get_articles_by_category_name)
):
    return templates.TemplateResponse(
        "articles.html",
        context={
            "request": request,
            "articles": articles
        }
    )