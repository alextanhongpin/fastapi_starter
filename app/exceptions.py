ALREADY_EXISTS = "already_exists"
BAD_REQUEST = "bad_request"
CONFLICT = "conflict"
FORBIDDEN = "forbidden"
INTERNAL = "internal"
NOT_FOUND = "not_found"
PRECONDITION_FAILED = "precondition_failed"
UNAUTHORIZED = "unauthorized"
UNKNOWN = "unknown"


class AppException(Exception):
    def __init__(self, *, code=UNKNOWN, reason, message="An error has occured"):
        self.name = self.__class__.__name__
        self.code = code
        self.reason = reason
        self.message = message
        super().__init__(self.message)


class AlreadyExistsError(AppException):
    """Exception that is raised when a given resource already exists"""

    def __init__(self, *, reason, message="The resource already exists"):
        super().__init__(code=ALREADY_EXISTS, reason=reason, message=message)


class BadRequestError(AppException):
    """Exception that is raised when the request does not fulfil the
    requirement"""

    def __init__(self, *, reason, message="Your input is invalid"):
        super().__init__(code=BAD_REQUEST, reason=reason, message=message)


class ConflictError(AppException):
    """Exception that is raised when the the application is unable to resolve
    the operation due to conflict in internal state, for example when the
    operation is already running"""

    def __init__(self, *, reason, message="Conflicting operation"):
        super().__init__(code=CONFLICT, reason=reason, message=message)


class InternalError(AppException):
    """Exception that is raised when the the errors are due to internal
    infrastructure or exception raised by external library that should not be
    exposed"""

    def __init__(self, *, reason, message="Oops, please try again later"):
        super().__init__(code=INTERNAL, reason=reason, message=message)


class NotFoundError(AppException):
    """Exception that is raised when the resource is not found, which can
    be either because it has not yet been created, or may have already been
    deleted"""

    def __init__(self, *, reason, message="Not found"):
        super().__init__(code=NOT_FOUND, reason=reason, message=message)


class PreconditionFailedError(AppException):
    """Exception that is raised when the operation is not allowed due to
    missing preconditions"""

    def __init__(self, *, reason, message="Unable to complete the operation"):
        super().__init__(code=PRECONDITION_FAILED, reason=reason, message=message)


class UnauthorizedError(AppException):
    """Exception that is raised when the end-user does not have access to
    perform the action or view a given resource"""

    def __init__(self, *, reason, message="You are not logged in"):
        super().__init__(code=UNAUTHORIZED, reason=reason, message=message)


class UnknownError(AppException):
    """Exception that is raised when the error is not handled, or should be
    handled at a later time. If your app returns this error in your error
    monitoring tools, update them to return any of the other exception
    above"""

    def __init__(self, *, reason, message="An unexpected error has occured"):
        super().__init__(code=UNKNOWN, reason=reason, message=message)
