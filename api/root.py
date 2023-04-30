from .user import router as user_router
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .base.response import Response, Error
from fastapi.encoders import jsonable_encoder
from app import exceptions
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


status_code_by_error_code = {
    exceptions.ALREADY_EXISTS: status.HTTP_409_CONFLICT,
    exceptions.BAD_REQUEST: status.HTTP_400_BAD_REQUEST,
    exceptions.CONFLICT: status.HTTP_409_CONFLICT,
    exceptions.FORBIDDEN: status.HTTP_403_FORBIDDEN,
    exceptions.INTERNAL: status.HTTP_500_INTERNAL_SERVER_ERROR,
    exceptions.NOT_FOUND: status.HTTP_404_NOT_FOUND,
    exceptions.PRECONDITION_FAILED: status.HTTP_412_PRECONDITION_FAILED,
    exceptions.UNAUTHORIZED: status.HTTP_401_UNAUTHORIZED,
    exceptions.UNKNOWN: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    status_code = status_code_by_error_code.get(
        exc.code, status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    error = Error(code=exc.code, reason=exc.reason, message=exc.message)

    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(Response(error=error)),
    )


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/health")
def read_health():
    return {"success": True}


app.include_router(user_router)
