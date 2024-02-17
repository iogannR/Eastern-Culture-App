from app.api.schemas.categories import (
    CreateCategory, SCategory, UpdateCategory, PartialUpdateCategory
)
from app.database.service.base import BaseService


class CategoryService(
    BaseService[SCategory, CreateCategory, UpdateCategory, PartialUpdateCategory]
):
    ...