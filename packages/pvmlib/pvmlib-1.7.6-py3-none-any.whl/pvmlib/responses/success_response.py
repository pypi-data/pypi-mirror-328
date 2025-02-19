from pvmlib.schemas.success_schema import ResponseGeneralSchema, ResponseMetaSchema, success_general_schema
from pvmlib.logs import LoggerSingleton
from typing import Any, Dict

log = LoggerSingleton()

class SuccessResponse(ResponseGeneralSchema):
    
    def __init__(
            self,
            code: int = 0, 
            type: int = 0, 
            message: str = "OK", 
            data: Any = {},
        ):
        super().__init__(
            code=code, 
            type=type, 
            message=message, 
            data=data, 
            meta=ResponseMetaSchema(
                id_transaction=log.logger.get_tracing_id(), 
                status="SUCCESS", 
                time_elapsed=0.0)
            )

    def to_response(self, time_elapsed: float):
        return ResponseGeneralSchema(
            code=self.code,
            type=self.type,
            message=self.message,
            data=self.data,
            meta=ResponseMetaSchema(
                id_transaction=log.logger.get_tracing_id(),
                status="SUCCESS",
                time_elapsed=time_elapsed   
            )
        )