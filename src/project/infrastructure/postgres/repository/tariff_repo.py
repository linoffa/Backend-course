from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from project.infrastructure.postgres.models import Tariff

class TariffRepository:
    _collection: Type[Tariff] = Tariff

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False