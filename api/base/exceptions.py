from fastapi import status

from app import exceptions

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


def get_status_code_by_error_code(code: str) -> int:
    default_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return status_code_by_error_code.get(code, default_status_code)
