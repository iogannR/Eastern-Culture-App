import fastapi
import sqlalchemy.ext.asyncio as sa_ext_asyncio
import sqlalchemy.exc as sa_exc

from app.api.schemas.categories import (
    CreateCategory, SCategory, UpdateCategory, PartialUpdateCategory
)
from app.database.models.category import Category
from app.database.service.category import CategoryService

from app.database.session import get_session


router = fastapi.APIRouter(
    prefix="/categories",
    tags=["Категории"]
)


@router.post("/create-category")
async def create_category(
    payload: CreateCategory, session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)
) -> SCategory:
    category_service = CategoryService(Category)
    try:
        result = await category_service.create_instance(
            session=session, 
            payload=payload
        )
    except sa_exc.IntegrityError as error:
        raise fastapi.HTTPException(status_code=409, detail="Conflict of unique names!")
    return result


@router.get("/get-categories")
async def get_categories(session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)) -> list[SCategory]:
    category_service = CategoryService(Category)
    result = await category_service.get_all_instances(session=session)
    return result


@router.patch("/")
async def update_categories(session: sa_ext_asyncio.AsyncSession = fastapi.Depends(get_session)):
    ...