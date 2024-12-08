from pydantic import BaseModel, Field, ConfigDict

class PassengerCreateUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    patronymic: str | None = Field(default=None)
    age: int
    sex: str

class PassengerSchema(PassengerCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int