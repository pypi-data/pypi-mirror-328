import ctypes
import json
import os
import sys
import platform
from typing import Any, Dict
import atexit
from importlib.util import find_spec

# instrumentation imports
from agentuity.instrumentation.crewai import CrewAIInstrumentation
from agentuity.instrumentation.litellm import LiteLLMInstrumentation
from agentuity.instrumentation import getAgentuityLogger

logger = getAgentuityLogger(__name__)


def dict_to_json(data: Dict[str, Any], skip_if_not_jsonable: bool = False) -> Any:
    obj = {}
    for key, value in data.items():
        if isinstance(value, dict):
            obj[key] = dict_to_json(value)
        elif is_jsonable(value):
            obj[key] = value
        else:
            if not skip_if_not_jsonable:
                obj[key] = str(value)
    return obj


def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False


class Agentuity(object):
    _instance = None

    def __new__(cls):
        """Ensures that only one instance of the class exists."""
        if cls._instance is None:
            cls._instance = super(Agentuity, cls).__new__(cls)
        return cls._instance

    def init(self, lib_path: str = None):
        if lib_path is None:
            # Try to find the library in common locations
            system = platform.system().lower()
            arch = platform.machine().lower()

            if arch == "aarch64":
                arch = "arm64"

            if system == "windows":
                lib_name = "libagentuity.dll"
            elif system == "darwin":
                lib_name = "libagentuity.dylib"
            else:
                lib_name = "libagentuity.so"

            logger.debug(f"System: {system}, Arch: {arch}")

            # Default paths to search for the library
            search_paths = [
                os.path.dirname(os.path.abspath(__file__)),
                os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "dist", system, arch
                ),
                os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "../../dist",
                    system,
                    arch,
                ),
            ]

            for path in search_paths:
                full_path = os.path.join(path, lib_name)
                logger.debug(f"Searching for library in {full_path}")
                if os.path.exists(full_path):
                    lib_path = full_path
                    logger.debug(f"Found library in {full_path}")
                    break

            if lib_path is None:
                raise RuntimeError(f"Could not find agentuity library: {lib_name}")

        self.lib = ctypes.cdll.LoadLibrary(lib_path)

        # Define function prototype
        self.lib.Execute.argtypes = [
            ctypes.c_char_p,  # command
            ctypes.c_char_p,  # json_data
        ]
        self.lib.Execute.restype = ctypes.c_char_p

        module_names = {"crewai": "crewai", "litellm": "litellm"}
        module_instances = {
            "crewai": lambda: CrewAIInstrumentation(),
            "litellm": lambda: LiteLLMInstrumentation(),
        }

        modules = []

        for name in module_names:
            if self.__module_exists(module_names[name]):
                logger.debug(f"Instrumenting {name}")
                instance = module_instances[name]()
                logger.debug(f"Created instance of {name}")
                instance.instrument()
                logger.info(f"Instrumented {name}")
                modules.append(name)

        if len(modules) == 0:
            logger.warning("No modules found to instrument")
            return

        atexit.register(self.__exit_handler)
        logger.debug("Executing startup command")
        self.__execute(
            command="startup",
            data={
                "language": "python",
                "version": sys.version,
                "modules": modules,
                "env": dict_to_json(
                    os.environ, skip_if_not_jsonable=True
                ),  # send along the env in case the env is loaded by the agent through something like dotenv
            },
        )
        logger.debug("Startup command executed")

    def __module_exists(self, module_name):
        parts = module_name.split(".")
        for i in range(1, len(parts) + 1):
            logger.debug(f"Checking if .{parts[:i]} exists")
            if find_spec(".".join(parts[:i])) is None:
                return False
        return True

    def __exit_handler(self):
        self.__execute("shutdown")

    def __execute(self, command: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        # Convert data to JSON string, use None for optional parameter
        json_data = json.dumps(data) if data is not None else None
        json_bytes = json_data.encode("utf-8") if json_data is not None else None
        command_bytes = command.encode("utf-8")

        # Call the Go function
        logger.debug(f"Executing command: {command} with data: {json_data}")
        result = self.lib.Execute(command_bytes, json_bytes)
        logger.debug(f"After execute command: {command}, returned result: {result}")
        if not result:
            raise RuntimeError("Agent execution failed")

        # Parse response
        response = json.loads(result.decode("utf-8"))
        if "error" in response:
            raise RuntimeError(response["error"])

        return response["result"]

    def version(self) -> str:
        result = self.__execute("version")
        return result["version"]

    def event(self, data: Dict[str, Any]) -> None:
        self.__execute("event", data)

    def echo(self, data: Dict[str, Any] = None) -> Dict[str, Any]:
        return self.__execute("echo", data)
