# Response Envelope

FastAPI doesn't envelope the data by default. In order to return the response in an envelope, we need to write our own custom response model with generic payload.


```python
from typing import Generic, TypeVar

from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Error(BaseModel):
    code: str
    message: str


class Response(GenericModel, Generic[DataT]):
    data: DataT | None
    error: Error | None

    @validator("error", always=True)
    def check_consistency(cls, v, values):
        if v is not None and values["data"] is not None:
            raise ValueError("must not provided both data and error")
        if v is None and values.get("data") is None:
            raise ValueError("must provide data or error")
        return v
```

Usage:

```python
Response(data=YourModel)
```

For error handling, we can define a generic error handling:

```python
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .base.response import Response, Error


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            Response(error=Error(code="bad_unicorn", message=exc.name))
        ),
    )
```


This will return the errors in the desired format:

```json
{
  "data": null,
  "error": {
    "code": "bad_unicorn",
    "message": "hello world"
  }
}
```

For defining custom errors, we will define it in another chapter.
