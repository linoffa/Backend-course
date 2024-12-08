from project.infrastructure.postgres.repository.passenger_repo import PassengerRepository
from project.infrastructure.postgres.database import PostgresDatabase


passenger_repo = PassengerRepository()
database = PostgresDatabase()
