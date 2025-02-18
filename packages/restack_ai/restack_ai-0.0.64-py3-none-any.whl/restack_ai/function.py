import json
from typing import Any

import websockets
from temporalio import activity
from temporalio.exceptions import ApplicationError

from .observability import log_with_context, logger

activity.logger.logger = logger


class ActivityLogger:
    """Wrapper for activity logger that ensures proper context and formatting."""

    def __init__(self) -> None:
        self._logger = activity.logger

    def _log(self, level: str, message: str, **kwargs: Any) -> None:
        try:
            activity.info()
            getattr(self._logger, level)(
                message,
                extra={"extra_fields": {**kwargs, "client_log": True}},
            )
        except RuntimeError:
            log_with_context(level.upper(), message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        self._log("debug", message, **kwargs)

    def info(self, message: str, **kwargs: Any) -> None:
        self._log("info", message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        self._log("warning", message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        self._log("error", message, **kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:
        self._log("critical", message, **kwargs)

    def exception(self, message: str, **kwargs: Any) -> None:
        """Log an exception with traceback (equivalent to `logging.exception`)."""
        kwargs["exc_info"] = True
        self._log("exception", message, **kwargs)


log = ActivityLogger()

FunctionFailure = ApplicationError
function_info = activity.info
heartbeat = activity.heartbeat
function = activity

__all__ = [
    "FunctionFailure",
    "function_info",
    "heartbeat",
    "log",
]


def current_workflow() -> Any:
    return activity.Context.current().info


async def stream_to_websocket(api_address: str, data: Any) -> Any:
    """Stream data to Restack Engine WebSocket API endpoint.

    Args:
        api_address (str): The address of the Restack Engine API.
        data (Any): The streamed data from an OpenAI-compatible API or a JSON dict.

    Returns:
        str: The final combined response as a string.

    """
    info = {
        "activityId": activity.info().activity_id,
        "workflowId": activity.info().workflow_id,
        "runId": activity.info().workflow_run_id,
        "activityType": activity.info().activity_type,
        "taskQueue": activity.info().task_queue,
    }

    protocol = "ws" if api_address.startswith("localhost") else "wss"
    websocket_url = f"{protocol}://{api_address}/stream/ws/workflow/history?workflowId={info['workflowId']}&runId={info['runId']}"

    try:
        async with websockets.connect(websocket_url) as websocket:
            try:
                # Send initial message
                await websocket.send(str(info))
                heartbeat(info)

                collected_messages = []

                # Check if module name is openai (so we don't have to import openai package in our library)
                if data.__class__.__module__.startswith("openai"):
                    for chunk in data:
                        content = (
                            chunk.choices[0].delta.content
                            if chunk.choices[0].delta
                            else None
                        )
                        if content:
                            collected_messages.append(content)
                            chunk_info = {
                                **info,
                                "chunk": chunk.model_dump(
                                    exclude_unset=True, exclude_none=True, mode="json"
                                ),
                            }

                            json_message = json.dumps(chunk_info)

                            await websocket.send(message=str(json_message), text=True)
                            heartbeat(json_message)

                    return "".join(collected_messages)
                if isinstance(data, dict):
                    event_info = {
                        **info,
                        "data": data,
                    }

                    json_message = json.dumps(event_info)
                    await websocket.send(message=str(json_message), text=True)
                    heartbeat(json_message)
                    return data
            finally:
                # Ensure the WebSocket connection is closed
                await websocket.close()
    except Exception as e:
        error_message = f"Error with restack stream to websocket: {e}"
        log.exception(error_message)
        raise ApplicationError(error_message) from e
