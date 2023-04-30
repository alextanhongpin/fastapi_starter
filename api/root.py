from .user import router as user_router
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .base.response import Response, Error
from .base.exceptions import get_status_code_by_error_code
from fastapi.encoders import jsonable_encoder
from app.exceptions import AppException

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    error = Error(code=exc.code, reason=exc.reason, message=exc.message)

    return JSONResponse(
        status_code=get_status_code_by_error_code(exc.code),
        content=jsonable_encoder(Response(error=error)),
    )


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/health")
def read_health():
    return {"success": True}


app.include_router(user_router)
