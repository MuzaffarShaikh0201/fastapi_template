from typing import Dict, List, Literal
from pydantic import BaseModel


class SuccessfulResponse(BaseModel):
    success: bool = True
    message: str = "This is initial route"
    data: None
    error: None
    meta: None


class CreatedResponse(BaseModel):
    success: bool = True
    message: str = "Created"
    data: None
    error: None
    meta: None


class UnauthorizedErrorResponse(BaseModel):
    success: bool = False
    message: str = "Unauthorized"
    data: None
    error: Dict[str, str] = {
        "code": "UNAUTHORIZED",
        "details": "Authentication required",
    }
    meta: None


class ForbiddenErrorResponse(BaseModel):
    success: bool = False
    message: str = "Forbidden"
    data: None
    error: Dict[str, str] = {
        "code": "FORBIDDEN",
        "details": "You are not authorized to access this resource.",
    }
    meta: None


class NotFoundErrorResponse(BaseModel):
    success: bool = False
    message: str = "Not Found"
    data: None
    error: Dict[str, str] = {
        "code": "NOT_FOUND",
        "details": "The requested resource could not be found.",
    }
    meta: None


class ConflictErrorResponse(BaseModel):
    success: bool = False
    message: str = "Conflict Error"
    data: None
    error: Dict[str, str] = {
        "code": "CONFLICT_ERROR",
        "details": "The resource you are trying to access is already in use.",
    }
    meta: None


class ValidationErrorDetails(BaseModel):
    field: str
    error: str


class ValidationErrorError(BaseModel):
    code: Literal["VALIDATION_ERROR"]
    details: List[ValidationErrorDetails]


class ValidationErrorResponse(BaseModel):
    success: bool = False
    message: Literal["Validation Error"]
    data: None
    error: ValidationErrorError
    meta: None


class TooManyRequestsError(BaseModel):
    success: bool = False
    message: str = "Too Many Requests"
    data: None
    error: Dict[str, str] = {
        "code": "TOO_MANY_REQUESTS",
        "details": "Rate limit exceeded. Try again later.",
    }
    meta: None


class BackendError(BaseModel):
    code: Literal["INTERNAL_SERVER_ERROR"]
    details: Literal[
        "Something went wrong. Please contact developers if issue persists."
    ]


class BackendErrorResponse(BaseModel):
    success: bool = False
    message: str = "Internal Server Error"
    data: None
    error: BackendError
    meta: None


HOME_RESPONSE_MODEL = {
    200: {"model": SuccessfulResponse},
    500: {"model": BackendErrorResponse},
}
