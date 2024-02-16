from fastapi import FastAPI

from app.api.routers.articles_router \
    import router as router_articles
from app.api.routers.categories_router \
    import router as router_categories

app = FastAPI(
    title="Information Portal App dedicated to Russian-Chinese cooperation"
)

app.include_router(router_articles)
app.include_router(router_categories)