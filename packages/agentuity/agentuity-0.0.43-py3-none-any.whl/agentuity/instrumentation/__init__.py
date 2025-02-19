import os
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict
from wrapt import wrap_function_wrapper
import json
import base64

logger = logging.getLogger(__name__)
log_level = os.getenv("LOG_LEVEL", "").upper()
numeric_level = 0
if log_level != "":
    # Convert the string to a logging level
    numeric_level = getattr(logging, log_level, None)
    logger.setLevel(level=numeric_level)


class BaseInstrumentation(ABC):
    _instance = None
    _is_instrumented_by_agentuity = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    @property
    def is_instrumented_by_agentuity(self):
        return self._is_instrumented_by_agentuity

    @abstractmethod
    def _instrument(self, **kwargs: Any):
        pass

    def _uninstrument(self, **kwargs: Any):
        pass

    def instrument(self, **kwargs: Any):
        """Instrument the library"""
        if self._is_instrumented_by_agentuity:
            logger.warning("Attempting to instrument while already instrumented")
            return None
        result = self._instrument(**kwargs)
        self._is_instrumented_by_agentuity = True
        return result

    def uninstrument(self, **kwargs: Any):
        """Uninstrument	the library"""
        if self._is_instrumented_by_agentuity:
            result = self._uninstrument(**kwargs)
            self._is_instrumented_by_agentuity = False
            return result

        logger.warning("Attempting to uninstrument while already uninstrumented")

        return None

    def _wrap(self, module, fn, before=None, after=None):
        def wrapper(wrapped, instance, args, kwargs):
            if before is not None:
                before(kwargs)
            response = wrapped(*args, **kwargs)
            if after is not None:
                after(kwargs, response)
            return response

        wrap_function_wrapper(module, fn, wrapper)
        return wrapper

    def has_overridden_input(self):
        return "AGENTUITY_SDK_INPUT_FILE" in os.environ

    def has_output(self):
        return "AGENTUITY_SDK_OUTPUT_FILE" in os.environ

    def read_input(self):
        with open(os.environ.get("AGENTUITY_SDK_INPUT_FILE")) as f:
            res = json.load(f)
            buf = res["payload"]
            if res["contentType"] == "application/json":
                if type(buf) is str:
                    base64_decoded = base64.b64decode(buf).decode("utf-8")
                    return json.loads(base64_decoded)
                else:
                    return buf
            else:
                return buf

    def write_output(
        self, content_type: str, data: str, metadata: Dict[str, Any] = None
    ):
        with open(os.environ.get("AGENTUITY_SDK_OUTPUT_FILE"), "w") as f:
            json.dump(
                {
                    "contentType": content_type,
                    "payload": base64.b64encode(data.encode("utf-8")).decode("utf-8"),
                    "trigger": "agent",
                    "metadata": metadata,
                },
                f,
            )


def getAgentuityLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=numeric_level)
    return logger


__all__ = ["BaseInstrumentor", "getAgentuityLogger"]
