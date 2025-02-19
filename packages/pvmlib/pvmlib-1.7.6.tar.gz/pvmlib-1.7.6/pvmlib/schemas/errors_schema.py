from pydantic import BaseModel
from typing import Any, Dict

class ErrorMetaSchema(BaseModel):
    error_code: int
    info: str
    id_transaction: str

class ErrorGeneralSchema(BaseModel):
    code: int = 0
    type: int = 0
    message: str = "ERROR"
    data: Dict[str, Any]
    meta: ErrorMetaSchema

type_content = "application/json"

error_general_schema = {
    "definitions": {
        "ErrorGeneralSchema": {
            "type": "object",
            "properties": {
                "code": {"type": "integer"},
                "type": {"type": "integer"},
                "message": {"type": "string"},
                "data": {"type": "object"},
                "meta": {
                    "type": "object",
                    "properties": {
                        "error_code": {"type": "integer"},
                        "info": {"type": "string"},
                        "id_transaction": {"type": "string"},
                    }
                }
            }
        }
    }
}

error_response_general_405 = {
    "description": "Method Not Allowed",
    "content": {
        type_content: {
            "schema": error_general_schema["definitions"]["ErrorGeneralSchema"],
            "examples": {
                "MethodNotAllowed": {
                    "value": ErrorGeneralSchema(
                        data={"user_message": "Method Not Allowed"},
                        meta=ErrorMetaSchema(
                            error_code=405,
                            info="Method Not Allowed",
                            id_transaction="unknown"
                        )
                    ).model_dump()
                }
            }
        }
    }
}