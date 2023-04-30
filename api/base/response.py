from typing import Generic, TypeVar

from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Error(BaseModel):
    code: str
    reason: str
    message: str


class Response(GenericModel, Generic[DataT]):
    data: DataT | None
    error: Error | None

    # Validates the field `error`.
    @validator("error", always=True)
    def check_consistency(cls, v, values):
        if v is not None and values["data"] is not None:
            raise ValueError("must not provided both data and error")
        if v is None and values.get("data") is None:
            raise ValueError("must provide data or error")
        return v
