import logging
import os
import socket
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any
from colorama import Fore, Style, init
import uuid

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', datefmt=DATE_FORMAT)
logger = logging.getLogger("uvicorn")

init(autoreset=True)

class LogType:
    SYSTEM = "SYSTEM"
    TRANSACTION = "TRANSACTION"
    SECURITY = "SECURITY"
    RETRY = "RETRY"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    INTERNAL = "INTERNAL"

class LogLevelColors:
    DEBUG = Fore.BLUE
    INFO = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    CRITICAL = Fore.RED

class Application(BaseModel):
    name: str
    version: str
    env: str
    kind: str

class Measurement(BaseModel):
    method: str
    elapsedTime: float
    status: str

class DataLogger(BaseModel):
    level: str
    schemaVersion: str
    logType: str
    sourceIP: str
    status: str
    message: str
    logOrigin: str
    timestamp: str
    tracingId: str
    hostname: str
    eventType: str
    application: Application
    measurement: Measurement
    destinationIP: str
    additionalInfo: Optional[Dict[str, Any]] = None

class LogData:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LogData, cls).__new__(cls)
            cls._instance.__initialize(*args, **kwargs)
        return cls._instance

    def __initialize(self, origin: str = "INTERNAL"):
        self.logger = logger
        self.schema_version = os.getenv("VERSION_LOG", "1.0.0")
        self.log_origin = origin
        self.tracing_id = "N/A"
        self.hostname = socket.gethostname()
        self.appname = os.getenv("APP_NAME", )
        self.source_ip = socket.gethostbyname(socket.gethostname())
        self.destination_ip = "N/A"
        self.additional_info = {}
        self.app = Application(
            name=os.getenv("APP_NAME", "default"),
            version=os.getenv("API_VERSION", "default"),
            env=os.getenv("ENV", "default"),
            kind=os.getenv("APP_KIND", "default"))
        self.initialized = True

    def set_tracing_id(self, tracing_id: str):
        self.tracing_id = tracing_id

    def get_tracing_id(self):
        return self.tracing_id

    def log(
            self, 
            level: int, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "SUCCESS", 
            tracingId: str = None,
            destination_ip: str = None,
            measurement: Optional[dict] = None, 
            additional_info: Optional[dict] = None
        ) -> None:
        
        if destination_ip is not None:
            self.destination_ip = destination_ip

        if tracingId is None:
            tracingId = self.tracing_id
        
        log_entry = DataLogger(
            level=logging.getLevelName(level),
            schemaVersion=self.schema_version,
            logType=logType,
            sourceIP=self.source_ip,
            status=status,
            message=message,
            logOrigin=self.log_origin,
            timestamp=datetime.now().strftime(DATE_FORMAT),
            tracingId=tracingId,
            hostname=self.hostname,
            eventType=f"{logType}_{event_type.upper()}",
            application=self.app,
            measurement=measurement if measurement else Measurement(method="unknown", elapsedTime=0, status="unknown"),
            destinationIP=self.destination_ip,
            additionalInfo=additional_info or self.additional_info,
        )

        colored_date = f"{Fore.CYAN}{log_entry.timestamp}{Style.RESET_ALL}"
        color_status = getattr(LogLevelColors, log_entry.level, Fore.WHITE) + log_entry.status + Style.RESET_ALL

        log_message = f'{colored_date} - {self.appname} - {log_entry.model_dump()} - Status: {color_status}'
        self.logger.log(level, log_message)

    def info(
            self, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "SUCCESS", 
            tracingId: str = None, 
            destination_ip: str = None,
            measurement: dict = None, 
            additional_info: dict = None
        ):
        self.log(
            logging.INFO, 
            message, 
            logType, 
            event_type, 
            status, 
            tracingId, 
            destination_ip,
            measurement, 
            additional_info
            )

    def error(
            self, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "ERROR", 
            tracingId: str = None, 
            destination_ip: str = None,
            measurement: dict = None, 
            additional_info: dict = None
        ):
        self.log(
            logging.ERROR, 
            message, 
            logType, 
            event_type, 
            status, 
            tracingId, 
            destination_ip,
            measurement, 
            additional_info
            )

    def warning(
            self, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "WARNING", 
            tracingId: str = None, 
            destination_ip: str = None,
            measurement: dict = None, 
            additional_info: dict = None
            ):
        self.log(
            logging.WARNING, 
            message, 
            logType, 
            event_type, 
            status, 
            tracingId, 
            destination_ip,
            measurement, 
            additional_info
            )

    def debug(
            self, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "DEBUG", 
            tracingId: str = None, 
            destination_ip: str = None,
            measurement: dict = None, 
            additional_info: dict = None
            ):
        self.log(
            logging.DEBUG, 
            message, 
            logType, 
            event_type, 
            status, 
            tracingId,
            destination_ip,
            measurement, 
            additional_info
            )

    def critical(
            self, 
            message: str, 
            logType: str = LogType.RETRY, 
            event_type: str = "EVENT", 
            status: str = "CRITICAL", 
            tracingId: str = None, 
            destination_ip: str = None,
            measurement: dict = None, 
            additional_info: dict = None
            ):
        self.log(
            logging.CRITICAL, 
            message, 
            logType, 
            event_type, 
            status, 
            tracingId, 
            destination_ip,
            measurement, 
            additional_info
            )

class LoggerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._instance.__initialize(*args, **kwargs)
            cls._instance._id = str(uuid.uuid4())
        return cls._instance
            
    def __initialize(self, *args, **kwargs):
        self.logger = LogData()
    
    def get_instance_id(self):
        return self._id