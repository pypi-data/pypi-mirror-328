from fastapi import HTTPException
from pvmlib.schemas.errors_schema import ErrorMetaSchema, ErrorGeneralSchema
from pvmlib.logs.logger import LoggerSingleton
import json
from typing import Any

log = LoggerSingleton()

class ErrorResponseException(HTTPException):
    def __init__(
            self, 
            code: int = 0, 
            type: int = 0, 
            message: str = None, 
            data: Any = {},
            info: str = None, 
            time_elapsed: float = 0.0
        ):
       
        self.code = code
        self.type = type
        self.message = message
        self.data = data
        self.info = info

        response = ErrorGeneralSchema(
            code=self.code,
            type=self.type,
            message=self.message,
            data=self.data,
            meta=ErrorMetaSchema(
                error_code=self.code,
                id_transaction=log.logger.get_tracing_id(),
                info=self.info,
                time_elapsed=time_elapsed
            ).model_dump()
        )
        
        super().__init__(status_code=code, detail=json.dumps(response.model_dump()))