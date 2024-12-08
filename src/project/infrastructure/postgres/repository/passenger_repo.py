from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from project.schemas.passenger import PassengerSchema, PassengerCreateUpdateSchema
from project.infrastructure.postgres.models import Passenger
from project.core.exceptions import PassengerNotFound
from project.core.config import settings
from sqlalchemy import text, select, insert, update, delete

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
        query = f"select * from {settings.POSTGRES_SCHEMA}.passenger;"

        passengers = await session.execute(text(query))

        return [PassengerSchema.model_validate(obj=passenger) for passenger in passengers.mappings().all()]

    async def get_passenger_by_id(
        self,
        session: AsyncSession,
        passenger_id: int,
    ) -> PassengerSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == passenger_id)
        )

        passenger = await session.scalar(query)

        if not passenger:
            raise PassengerNotFound(_id=passenger_id)

        return PassengerSchema.model_validate(obj=passenger)

    async def create_passenger(
        self,
        session: AsyncSession,
        passenger: PassengerCreateUpdateSchema,
    ) -> PassengerSchema:
        query = (
            insert(self._collection)
            .values(passenger.model_dump())
            .returning(self._collection)
        )

        created_passenger = await session.scalar(query)
        await session.flush()

        return PassengerSchema.model_validate(obj=created_passenger)

    async def delete_passenger(
        self,
        session: AsyncSession,
        passenger_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == passenger_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise PassengerNotFound(_id=passenger_id)

    async def update_passenger(
        self,
        session: AsyncSession,
        passenger_id: int,
        passenger: PassengerCreateUpdateSchema,
    ) -> PassengerSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == passenger_id)
            .values(passenger.model_dump())
            .returning(self._collection)
        )

        updated_passenger = await session.scalar(query)

        if not updated_passenger:
            raise PassengerNotFound(_id=passenger_id)

        return PassengerSchema.model_validate(obj=updated_passenger)