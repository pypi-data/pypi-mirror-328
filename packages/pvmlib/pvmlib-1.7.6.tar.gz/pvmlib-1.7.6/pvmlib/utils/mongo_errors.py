
from pymongo.errors import (
    ConnectionFailure, 
    OperationFailure, 
    ServerSelectionTimeoutError, 
    CollectionInvalid,
    ConfigurationError,
    DuplicateKeyError,
    InvalidURI,
    WriteError,
    WriteConcernError,
    NetworkTimeout,
    InvalidName,
    InvalidOperation,
)

class MongoDBConnectionError:
    EXCEPTION_MAP = {
        ConnectionFailure: "CONNECTION_FAILURE",
        OperationFailure: "OPERATION_FAILURE",
        ServerSelectionTimeoutError: "SERVER_SELECTION_TIME_OUT_ERROR",
        CollectionInvalid: "COLLECTION_INVALID",
        ConfigurationError: "CONFIGURATION_ERROR",
        DuplicateKeyError: "DUPLICATE_KEY_ERROR",
        InvalidURI: "INVALID_URI",
        WriteError: "WRITE_ERROR",
        WriteConcernError: "WRITE_CONCERN_ERROR",
        NetworkTimeout: "NETWORK_TIMEOUT",
        InvalidName: "INVALID_NAME",
        InvalidOperation: "INVALID_OPERATION",
    }

    @classmethod
    def get_exception_name(cls, exc: Exception) -> tuple:
        """Devuelve el nombre de la excepción de MongoDB y la excepción misma."""
        for exception_type, name in cls.EXCEPTION_MAP.items():
            if isinstance(exc, exception_type):
                return name, exc
        return "UNKNOWN_EXCEPTION", exc
