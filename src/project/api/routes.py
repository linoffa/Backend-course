from fastapi import APIRouter

from project.infrastructure.postgres.repository.passenger_repo import PassengerRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.passenger import PassengerSchema


router = APIRouter()


@router.get("/all_passengers", response_model=list[PassengerSchema])
async def get_all_passengers() -> list[PassengerSchema]:
    passenger_repo = PassengerRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await passenger_repo.check_connection(session=session)
        all_passengers = await passenger_repo.get_all_passengers(session=session)

    return all_passengers
