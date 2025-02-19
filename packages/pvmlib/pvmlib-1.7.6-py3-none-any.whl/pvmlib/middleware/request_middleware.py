from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from pvmlib.logs.logger import LoggerSingleton, LogType, Measurement
import time
import logging

class TracingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        start_time = time.time()
        tracing_id = request.headers.get("transaction_id", "N/A")
        logger = LoggerSingleton().logger
        logger.set_tracing_id(tracing_id)

        request_info = {
            "url": str(request.url),
            "method": request.method,
            "headers": dict(request.headers),
            "query_params": dict(request.query_params),
            "path_params": request.path_params,
            "cookies": request.cookies,
            "client": {
                "host": request.client.host,
                "port": request.client.port
            }
        }

        if request.method in ["POST", "PUT", "PATCH"]:
            request_body = await request.body()
            request_info["body"] = request_body.decode("utf-8") if request_body else None

        response = await call_next(request)
        time_elapsed = time.time() - start_time

        logger.log(
            level=logging.INFO,
            message="Request processed",
            logType=LogType.SYSTEM,
            event_type="REQUEST",
            status="INFO",
            tracingId=tracing_id,
            destination_ip=request.client.host,
            measurement=Measurement(
                method=f"{self.__class__.__name__}.{self.dispatch.__name__}",
                elapsedTime=time_elapsed,
                status="PROCESSED"
            ),
            additional_info={
                "request_info": request_info,
                "time_elapsed": time_elapsed,
                "transaction_id": tracing_id
            }
        )

        return response