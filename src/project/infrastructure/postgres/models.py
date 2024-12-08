from sqlalchemy.orm import Mapped, mapped_column

from project.infrastructure.postgres.database import Base


class Passenger(Base):
    __tablename__ = "passenger"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    patronymic: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=False)
    sex: Mapped[str] = mapped_column(nullable=False)

class Tariff(Base):
    __tablename__ = "tariff"

    id: Mapped[int] = mapped_column(primary_key=True)
    clas: Mapped[str] = mapped_column(nullable=False)
    discount: Mapped[int] = mapped_column(nullable=True)
    baggage: Mapped[bool] = mapped_column(nullable=True)