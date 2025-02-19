"""
Cocoindex is a framework for building and running indexing pipelines.
"""
import json
import os
import sys
from typing import Callable, Self
from dataclasses import dataclass

from . import _engine
from . import flow, query, sources, transforms, storages, cli
from .flow import FlowBuilder, DataScope, DataSlice, Flow, flow_def
from .vector import VectorSimilarityMetric
from ._engine import OpArgSchema

__all__ = ["flow", "query", "sources", "transforms", "storages", "cli", "op",
           "FlowBuilder", "DataScope", "DataSlice", "Flow", "flow_def", "OpArgSchema",
           "VectorSimilarityMetric"]

@dataclass
class Settings:
    """Settings for the cocoindex library."""
    database_url: str
    server: str = "127.0.0.1:8080"
    ui_cors_origin: str | None = None

    @classmethod
    def from_env(cls) -> Self:
        """Load settings from environment variables."""
        kwargs = dict()

        def load_field(name: str, env_name: str, required: bool = False):
            nonlocal kwargs
            value = os.getenv(env_name)
            if value is None:
                if required:
                    raise ValueError(f"{env_name} is not set")
            else:
                kwargs[name] = value

        load_field("database_url", "COCOINDEX_DATABASE_URL", required=True)
        load_field("server", "COCOINDEX_SERVER")
        load_field("ui_cors_origin", "UI_CORS_ORIGIN")

        return cls(**kwargs)


def init(settings: Settings):
    """Initialize the cocoindex library."""
    _engine.init(json.dumps(settings.__dict__))

def start_server():
    """Start the cocoindex server."""
    flow.ensure_all_flows_built()
    query.ensure_all_handlers_built()
    _engine.start_server()

def stop():
    """Stop the cocoindex library."""
    _engine.stop()

def cli_main(settings: Settings | None = None, cmd: str = 'cocoindex') -> Callable[[Callable], Callable]:
    """
    A decorator to wrap the main function.
    If the python binary is called with the given command, it yields control to the cocoindex CLI.

    If the settings are not provided, they are loaded from the environment variables.
    """
    def _main_wrapper(fn: Callable) -> Callable:

        def _inner(*args, **kwargs):
            effective_settings = settings or Settings.from_env()
            init(effective_settings)
            try:
                if len(sys.argv) > 1 and sys.argv[1] == cmd:
                    return cli.cli.main(sys.argv[2:], prog_name=f"{sys.argv[0]} {sys.argv[1]}")
                else:
                    return fn(*args, **kwargs)
            finally:
                stop()

        _inner.__name__ = fn.__name__
        return _inner

    return _main_wrapper
