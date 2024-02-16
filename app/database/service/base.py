from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.database.base import Base


# Declaration of basic model and schemas annotations
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

# Base Service class
class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model: Type[ModelType] = None
    

    # Getting all instances
    async def get_all_instances(self, session: AsyncSession) -> list[ModelType]:
        query = await session.execute(select(self.model))
        return query.scalars().all()
    
    # Getting instance by id
    async def get_instance_by_id(self, session: AsyncSession, instance_id: uuid.UUID) -> ModelType | None:
        return await session.get(self.model, instance_id)
    
    # Creating a new instance
    async def create_instance(self, session: AsyncSession, payload: CreateSchemaType) -> ModelType:
        new_instance = self.model(**payload.model_dump())
        session.add(new_instance)
        await session.commit()
        return new_instance
    
    # Updating instance data
    async def update_instance(
        self, 
        session: AsyncSession, 
        instance: ModelType, 
        payload: UpdateSchemaType
    ) -> ModelType:
        for name, value in payload.model_dump().items():
            setattr(instance, name, value)
        await session.commit()
        return instance