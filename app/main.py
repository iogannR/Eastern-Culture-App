import fastapi
import fastapi.staticfiles as fa_staticfiles

from app.api.routers.articles \
    import router as router_articles
from app.api.routers.categories \
    import router as router_categories
from app.api.routers.pages \
    import router as router_pages
from app.api.routers.images \
    import router as router_images

app = fastapi.FastAPI(
    title="Information Portal App dedicated to Russian-Chinese cooperation"
)

app.include_router(router_articles)
app.include_router(router_categories)
app.include_router(router_pages)
app.include_router(router_images)

app.mount(
    "/static", fa_staticfiles.StaticFiles(directory="app/static"), "static"
)