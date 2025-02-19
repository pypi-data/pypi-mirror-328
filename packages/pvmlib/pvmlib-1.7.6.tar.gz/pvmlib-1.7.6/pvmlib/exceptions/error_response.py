from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from tenacity import RetryError
from pydantic import BaseModel
from pvmlib.schemas.errors_schema import ErrorGeneralSchema, ErrorMetaSchema
from pvmlib.logs.logger import LoggerSingleton, LogType, Measurement
from pvmlib.utils import MongoDBConnectionError
from pvmlib.utils import Utils
from pvmlib.responses.error_response import ErrorResponseException
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
import json

class DataError(BaseModel):
    user_message: str

log = LoggerSingleton()

async def internal_server_error_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, ErrorResponseException):
        return await error_exeption_handler(request, exc)
    
    tracing_id = log.logger.get_tracing_id()
    exception_name, exception_instance = MongoDBConnectionError.get_exception_name(exc)
    
    if exception_name != "UNKNOWN_EXCEPTION":
        error_message = f"MongoDB error occurred: {exception_name}"
        error_info = str(exception_instance)

    error_message, error_info = await Utils.get_instance_exception(exc)

    error_response = ErrorGeneralSchema(
        code=HTTP_500_INTERNAL_SERVER_ERROR,
        type=5,
        message=error_message,
        data=DataError(user_message=error_message).model_dump(),
        meta=ErrorMetaSchema(
            info="An unexpected error occurred.",
            error_code=HTTP_500_INTERNAL_SERVER_ERROR,
            id_transaction=tracing_id,
        )
    )
    log.logger.error(
        message=error_message,
        logType=LogType.INTERNAL,
        event_type="SERVER_ERROR",
        status="ERROR",
        tracingId=tracing_id,
        measurement=Measurement(method="internal_server_error_exception_handler", elapsedTime=0.0, status="ERROR"),
        additional_info={"code": HTTP_500_INTERNAL_SERVER_ERROR, "info": error_info, "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_500_INTERNAL_SERVER_ERROR)

async def parameter_exception_handler(request: Request, exc: RequestValidationError):
    if isinstance(exc, ErrorResponseException):
        return await error_exeption_handler(request, exc)
    
    tracing_id = log.logger.get_tracing_id()
    error_details = Utils.get_error_details(exc.errors())
    error_response = ErrorGeneralSchema(
        code=HTTP_422_UNPROCESSABLE_ENTITY,
        type=0,
        message="Invalid parameter.",
        data=DataError(user_message=", ".join(error_details)).model_dump(),
        meta=ErrorMetaSchema(
            info=", ".join(error_details),
            error_code=HTTP_422_UNPROCESSABLE_ENTITY,
            id_transaction=tracing_id,
        )
    )
    log.logger.warning(
        message="Invalid parameter.",
        logType=LogType.FAILED,
        event_type="REQUEST_VALIDATION",
        status="WARNING",
        tracingId=tracing_id,
        measurement=Measurement(method="parameter_exception_handler", elapsedTime=0.0, status="WARNING"),
        additional_info={"code": HTTP_422_UNPROCESSABLE_ENTITY, "info": ", ".join(error_details), "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_422_UNPROCESSABLE_ENTITY)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if isinstance(exc, ErrorResponseException):
        return await error_exeption_handler(request, exc)

    tracing_id = log.logger.get_tracing_id()
    error_details = Utils.get_error_details(exc.errors())
    error_response = ErrorGeneralSchema(
        code=HTTP_422_UNPROCESSABLE_ENTITY,
        type=0,
        message="Validation error.",
        data=DataError(user_message=str(error_details)).model_dump(),
        meta=ErrorMetaSchema(
            error_code=HTTP_422_UNPROCESSABLE_ENTITY,
            info=str(error_details),
            id_transaction=tracing_id,
        )
    )
    log.logger.warning(
        message="Validation error.",
        logType=LogType.FAILED,
        event_type="VALIDATION_ERROR",
        status="BAD_REQUEST",
        tracingId=tracing_id,
        measurement=Measurement(method="validation_exception_handler", elapsedTime=0.0, status="BAD_REQUEST"),
        additional_info={"code": HTTP_422_UNPROCESSABLE_ENTITY, "info": str(error_details), "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_422_UNPROCESSABLE_ENTITY)

async def not_found_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc, ErrorResponseException):
        return await error_exeption_handler(request, exc)

    tracing_id = log.logger.get_tracing_id()
    error_response = ErrorGeneralSchema(
        code=HTTP_404_NOT_FOUND,
        type=0,
        message="Resource not found.",
        data=DataError(user_message=exc.detail).model_dump(),
        meta=ErrorMetaSchema(
            error_code=HTTP_404_NOT_FOUND,
            info="Resource not found.",
            id_transaction=tracing_id
        )
    )
    log.logger.error(
        message=f"Resource not found: {exc.detail}",
        logType=LogType.FAILED,
        event_type="NOT_FOUND",
        status="NOT_FOUND",
        tracingId=tracing_id,
        measurement=Measurement(method="not_found_exception_handler", elapsedTime=0.0, status="NOT_FOUND"),
        additional_info={"code": HTTP_404_NOT_FOUND, "info": exc.detail, "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_404_NOT_FOUND)

async def method_not_allowed_exception_handler(request: Request, exc: HTTPException):
    tracing_id = log.logger.get_tracing_id()
    error_response = ErrorGeneralSchema(
        code=HTTP_405_METHOD_NOT_ALLOWED,
        type=0,
        message="Method not allowed.",
        data=DataError(user_message="Method not allowed.").model_dump(),
        meta=ErrorMetaSchema(
            error_code=HTTP_405_METHOD_NOT_ALLOWED,
            info="Method not allowed.",
            id_transaction=tracing_id,
        )
    )
    log.logger.warning(
        message=f"Method not allowed",
        logType=LogType.FAILED,
        event_type="METHOD_NOT_ALLOWED",
        status="METHOD_NOT_ALLOWED",
        tracingId=tracing_id,
        measurement=Measurement(method="method_not_allowed_exception_handler", elapsedTime=0.0, status="METHOD_NOT_ALLOWED"),
        additional_info={"code": HTTP_405_METHOD_NOT_ALLOWED, "info": exc.detail, "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_405_METHOD_NOT_ALLOWED)

async def bad_request_exception_handler(request: Request, exc: HTTPException):

    if isinstance(exc, ErrorResponseException):
        return await error_exeption_handler(request, exc)

    tracing_id = log.logger.get_tracing_id()
    error_response = ErrorGeneralSchema(
        code=HTTP_400_BAD_REQUEST,
        type=0,
        message="Bad request.",
        data=DataError(user_message="Bad request.").model_dump(),
        meta=ErrorMetaSchema(
            error_code=HTTP_400_BAD_REQUEST,
            info="Bad request.",
            id_transaction=tracing_id
        )
    )
    log.logger.warning(
        message=f"Bad request",
        logType=LogType.FAILED,
        event_type="BAD_REQUEST",
        status="BAD_REQUEST",
        tracingId=tracing_id,
        measurement=Measurement(method="bad_request_exception_handler", elapsedTime=0.0, status="BAD_REQUEST"),
        additional_info={"code": HTTP_400_BAD_REQUEST, "info": exc.detail, "instance_id": log.get_instance_id()}
    )
    return JSONResponse(content=error_response.model_dump(), status_code=HTTP_400_BAD_REQUEST)

async def error_exeption_handler(request: Request, exc: ErrorResponseException):
    return JSONResponse(content=json.loads(exc.detail), status_code=exc.status_code)