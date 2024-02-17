import fastapi

from app.api.routers.articles \
    import router as router_articles
from app.api.routers.categories \
    import router as router_categories

app = fastapi.FastAPI(
    title="Information Portal App dedicated to Russian-Chinese cooperation"
)

app.include_router(router_articles)
app.include_router(router_categories)