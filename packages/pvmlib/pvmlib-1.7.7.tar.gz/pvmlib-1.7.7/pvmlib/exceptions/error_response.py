from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from pvmlib.responses.error_response import ErrorResponseException
from pvmlib.utils import Utils
import json

async def internal_server_error_exception_handler(request: Request, exc: Exception):
    error_message, error_info = await Utils.get_instance_exception(exc)
    response = ErrorResponseException(
        message=error_message,
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        dev_message=error_info
    )
    return JSONResponse(content=json.loads(response.detail), status_code=HTTP_500_INTERNAL_SERVER_ERROR)

async def validation_exception_handler(request: Request, exc: RequestValidationError): 
    error_details = Utils.get_error_details(exc.errors())
    error_message = "Validation error: " + ", ".join(error_details)
    response = ErrorResponseException(
        message=error_message,
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        dev_message=error_details
    )
    return JSONResponse(content=json.loads(response.detail), status_code=HTTP_422_UNPROCESSABLE_ENTITY)

async def not_found_exception_handler(request: Request, exc: HTTPException):
    error_message = "Resource not found"
    response = ErrorResponseException(
        message=error_message,
        status_code=HTTP_404_NOT_FOUND,
        dev_message=exc.detail
    )
    return JSONResponse(content=json.loads(response.detail), status_code=exc.status_code) 

async def method_not_allowed_exception_handler(request: Request, exc: HTTPException):   
    error_message = "Method not allowed."
    response = ErrorResponseException(
        message=error_message,
        status_code=HTTP_405_METHOD_NOT_ALLOWED,
        dev_message=exc.detail
    )
    return JSONResponse(content=json.loads(response.detail), status_code=exc.status_code)

async def bad_request_exception_handler(request: Request, exc: HTTPException):
    error_message = "Bad request."
    response = ErrorResponseException(
        message=error_message,
        status_code=HTTP_400_BAD_REQUEST,
        dev_message=exc.detail
    )
    return JSONResponse(content=json.loads(response.detail), status_code=exc.status_code)

async def error_exeption_handler(request: Request, exc: ErrorResponseException):
    return JSONResponse(content=json.loads(exc.detail), status_code=exc.status_code)