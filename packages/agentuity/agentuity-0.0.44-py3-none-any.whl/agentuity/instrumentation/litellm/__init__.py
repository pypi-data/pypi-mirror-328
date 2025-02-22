from agentuity.instrumentation import BaseInstrumentation
from agentuity.instrumentation import getAgentuityLogger
import agentuity
import importlib.metadata
from datetime import datetime
import uuid

logger = getAgentuityLogger(__name__)
module = "litellm"
module_version = importlib.metadata.version(module)

version = "1"  # change this to change the format of the events


def to_messages(msg):
    result = []
    for m in msg:
        result.append({"role": m["role"], "content": m["content"]})
    return result


def to_usage(usage):
    result = {}
    result["prompt_tokens"] = usage["prompt_tokens"]
    result["completion_tokens"] = usage["completion_tokens"]
    result["total_tokens"] = usage["total_tokens"]
    return result


def to_choices(choices):
    result = []
    for c in choices:
        result.append(
            {
                "message": {"role": c.message["role"], "content": c.message["content"]},
                "index": c.index,
                "finish_reason": c.finish_reason,
            }
        )
    return result


def to_request(req):
    result = {}
    result["model"] = req["model"]
    result["stop"] = req["stop"] if "stop" in req else None
    result["stream"] = True if req["stream"] == "True" else False
    result["messages"] = to_messages(req["messages"])
    return result


def to_response(res):
    result = {}
    result["id"] = res["id"]
    result["model"] = res["model"]
    result["created"] = datetime.fromtimestamp(res["created"]).isoformat()
    result["usage"] = to_usage(res["usage"])
    result["object"] = res["object"]
    result["system_fingerprint"] = res["system_fingerprint"]
    result["service_tier"] = res["service_tier"]
    result["choices"] = to_choices(res["choices"])
    return result


class LiteLLMInstrumentation(BaseInstrumentation):
    def _instrument(self):
        logger.info("Instrumenting LiteLLM")
        self._wrap(module, "completion", self._before, self._after)

    def _before(self, kwargs):
        self.request_id = str(uuid.uuid4())
        agentuity.event(
            {
                "id": self.request_id,
                "version": version,
                "module": module,
                "module_version": module_version,
                "action": "completion",
                "stage": "before",
                "request": to_request(kwargs),
            }
        )

    def _after(self, kwargs, response):
        agentuity.event(
            {
                "id": self.request_id,
                "version": version,
                "module": module,
                "module_version": module_version,
                "action": "completion",
                "stage": "after",
                "response": to_response(response),
            }
        )
        self.request_id = None
