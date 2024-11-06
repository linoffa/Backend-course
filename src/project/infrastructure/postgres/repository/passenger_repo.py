from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.passenger import PassengerSchema
from project.infrastructure.postgres.models import Passenger

from project.core.config import settings


class PassengerRepository:
    _collection: Type[Passenger] = Passenger

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_passengers(
        self,
        session: AsyncSession,
    ) -> list[PassengerSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.passengers;"

        passengers = await session.execute(text(query))

        return [PassengerSchema.model_validate(obj=passenger) for passenger in passengers.mappings().all()]

