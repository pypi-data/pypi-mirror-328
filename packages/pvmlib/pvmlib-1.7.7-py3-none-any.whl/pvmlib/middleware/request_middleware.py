from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from pvmlib.logs.logger import LoggerSingleton, LogType, Measurement
from pvmlib.context import RequestContext
import time
import logging
import uuid

class TracingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        tracing_id = request.headers.get("transaction_id", str(uuid.uuid4()))
        user_id = request.headers.get("user_id", "anonymous")
        session_id = request.headers.get("session_id", str(uuid.uuid4()))
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "unknown")
        request_path = request.url.path

        logger = LoggerSingleton().logger
        logger.set_tracing_id(tracing_id)

        context = RequestContext()
        context.set_start_time(start_time)
        context.set_tracing_id(tracing_id)
        context.set_user_id(user_id)
        context.set_session_id(session_id)
        context.set_client_ip(client_ip)
        context.set_user_agent(user_agent)
        context.set_request_path(request_path)

        request_info = await self._get_request_info(request)

        response = await call_next(request)
        time_elapsed = time.time() - start_time

        self._log_request(logger, tracing_id, request, request_info, time_elapsed)

        return response

    async def _get_request_info(self, request: Request) -> dict:
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

        return request_info

    def _log_request(self, logger, tracing_id, request, request_info, time_elapsed):
        context = RequestContext()
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
                "transaction_id": tracing_id,
                "user_id": context.get_user_id(),
                "session_id": context.get_session_id(),
                "client_ip": context.get_client_ip(),
                "user_agent": context.get_user_agent(),
                "request_path": context.get_request_path()
            }
        )