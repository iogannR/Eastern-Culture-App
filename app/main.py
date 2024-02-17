from fastapi import FastAPI
import fastapi.staticfiles

from app.api.routers.articles \
    import router as router_articles
from app.api.routers.categories \
    import router as router_categories
from app.api.routers.pages \
    import router as router_pages

app = FastAPI(
    title="Information Portal App dedicated to Russian-Chinese cooperation"
)

app.mount(
    "/static", 
    fastapi.staticfiles.StaticFiles(directory="app/static"), 
    "static"
)

app.include_router(router_articles)
app.include_router(router_categories)
app.include_router(router_pages)