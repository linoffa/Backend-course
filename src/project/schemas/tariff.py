from pydantic import BaseModel, Field, ConfigDict

class TariffCreateUpdateSchema(BaseModel):
    clas: str
    discount: int | None = Field(default=0)
    baggage: bool | None = Field(default=False)

class TariffSchema(TariffCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int