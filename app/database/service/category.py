from app.api.schemas.categories import CreateCategory, SCategory, UpdateCategory
from app.database.models.category import Category
from app.database.service.base import BaseService


class CategoryService(BaseService[SCategory, CreateCategory, UpdateCategory]):
    model = Category