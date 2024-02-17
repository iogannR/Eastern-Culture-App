import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.categories import CreateCategory, SCategory, UpdateCategory
from app.database.service.category import CategoryService

from app.database.session import get_session


router = APIRouter(
    prefix="/categories",
    tags=["Категории"]
)


@router.post("/create-category")
async def create_category(
    payload: CreateCategory, 
    session: AsyncSession = Depends(get_session)
) -> SCategory:
    category_service = CategoryService()
    result = await category_service.create_instance(
        session=session, 
        payload=payload
    )
    return result


@router.get("/get-categories")
async def get_categories(session: AsyncSession = Depends(get_session)) -> list[SCategory]:
    category_service = CategoryService()
    result = await category_service.get_all_instances(session=session)
    return result