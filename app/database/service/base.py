import typing
import pydantic
import sqlalchemy as sa
import sqlalchemy.ext.asyncio as sa_ext_asyncio
import uuid

from app.database.base import Base


# Declaration of basic model and schemas annotations
ModelType = typing.TypeVar("ModelType", bound=Base)
CreateSchemaType = typing.TypeVar("CreateSchemaType", bound=pydantic.BaseModel)
UpdateSchemaType = typing.TypeVar("UpdateSchemaType", bound=pydantic.BaseModel)
PartialUpdateSchemaType = typing.TypeVar(
    "PartialUpdateSchemaType", 
    bound=pydantic.BaseModel
)

# Base Service class
class BaseService(typing.Generic[ModelType, CreateSchemaType, UpdateSchemaType, PartialUpdateSchemaType]):
    def __init__(self, model: typing.Type[ModelType]) -> None:
        self.model = model   

    # Getting all instances
    async def get_all_instances(
        self, session: sa_ext_asyncio.AsyncSession
    ) -> list[ModelType]:
        query = await session.execute(sa.select(self.model))
        return query.scalars().all()
    
    # Getting instance by id
    async def get_instance_by_id(
        self, session: sa_ext_asyncio.AsyncSession, instance_id: uuid.UUID
    ) -> ModelType | None:
        return await session.get(self.model, instance_id)
    
    # Creating a new instance
    async def create_instance(
        self, session: sa_ext_asyncio.AsyncSession, payload: CreateSchemaType
    ) -> ModelType:
        new_instance = self.model(**payload.model_dump())
        session.add(new_instance)
        await session.commit()
        return new_instance
    
    # Full/partial updating instance data 
    async def update_instance(
        self, 
        session: sa_ext_asyncio.AsyncSession, 
        instance: ModelType, 
        payload: UpdateSchemaType | PartialUpdateSchemaType,
        partial: bool = False
    ) -> ModelType:
        for name, value in payload.model_dump(exclude_unset=partial).items():
            setattr(instance, name, value)
        await session.commit()
        return instance