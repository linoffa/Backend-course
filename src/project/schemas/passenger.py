from pydantic import BaseModel, Field, ConfigDict


class PassengerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    patronymic: str | None = Field(default=None)
    age: int
    sex: str