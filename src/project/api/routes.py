from fastapi import APIRouter, HTTPException, status
from project.schemas.healthcheck import HealthCheckSchema

from project.infrastructure.postgres.repository.passenger_repo import PassengerRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.passenger import PassengerSchema, PassengerCreateUpdateSchema
from project.core.exceptions import PassengerNotFound
from project.api.depends import database, passenger_repo


router = APIRouter()

@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await passenger_repo.check_connection(session=session)

    return HealthCheckSchema(
        db_is_ok=db_is_ok,
    )

@router.get("/passengers", response_model=list[PassengerSchema], tags=["Passengers"])
async def get_all_passengers() -> list[PassengerSchema]:
    passenger_repo = PassengerRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await passenger_repo.check_connection(session=session)
        all_passengers = await passenger_repo.get_all_passengers(session=session)

    return all_passengers

@router.get("/passengers/{passenger_id}", response_model=PassengerSchema, status_code=status.HTTP_200_OK, tags=["Passengers"])
async def get_passenger_by_id(
    passenger_id: int,
) -> PassengerSchema:
    try:
        async with database.session() as session:
            passenger = await passenger_repo.get_passenger_by_id(session=session, passenger_id=passenger_id)
    except PassengerNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return passenger

@router.post("/passengers", response_model=PassengerSchema, status_code=status.HTTP_201_CREATED, tags=["Passengers"])
async def add_passenger(
    passenger_dto: PassengerCreateUpdateSchema,
) -> PassengerSchema:
    async with database.session() as session:
        new_passenger = await passenger_repo.create_passenger(session=session, passenger=passenger_dto)

    return new_passenger


@router.delete("/passengers/{passenger_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Passengers"])
async def delete_passenger(
    passenger_id: int,
) -> None:
    try:
        async with database.session() as session:
            passenger = await passenger_repo.delete_passenger(session=session, passenger_id=passenger_id)
    except PassengerNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return passenger

@router.put(
    "/passengers/{passenger_id}",
    response_model=PassengerSchema,
    status_code=status.HTTP_200_OK,
    tags=["Passengers"]
)
async def update_passenger(
    passenger_id: int,
    passenger_dto: PassengerCreateUpdateSchema,
) -> PassengerSchema:
    try:
        async with database.session() as session:
            updated_passenger = await passenger_repo.update_passenger(
                session=session,
                passenger_id=passenger_id,
                passenger=passenger_dto,
            )
    except PassengerNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_passenger