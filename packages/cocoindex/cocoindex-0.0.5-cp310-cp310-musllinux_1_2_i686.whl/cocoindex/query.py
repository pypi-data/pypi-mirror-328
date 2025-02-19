from typing import Callable
from threading import Lock
import json

from . import flow
from . import vector
from . import _engine

_handlers_lock = Lock()
_handlers: dict[str, _engine.SimpleSemanticsQueryHandler] = {}

class SimpleSemanticsQueryHandler:
    """
    A query handler that uses simple semantics to query the index.
    """
    _lazy_query_handler: Callable[[], _engine.SimpleSemanticsQueryHandler]

    def __init__(
        self,
        name: str,
        fl: flow.Flow,
        target_name: str,
        query_transform_flow: Callable[..., flow.DataSlice],
        default_similarity_metric: vector.VectorSimilarityMetric = vector.VectorSimilarityMetric.COSINE_SIMILARITY) -> None:

        engine_handler = None
        lock = Lock()
        def _lazy_handler() -> _engine.SimpleSemanticsQueryHandler:
            nonlocal engine_handler, lock
            if engine_handler is None:
                with lock:
                    if engine_handler is None:
                        engine_handler = _engine.SimpleSemanticsQueryHandler(
                            fl.internal_flow(), target_name,
                            flow.TransientFlow(query_transform_flow, [str]).internal_flow(),
                            json.dumps(default_similarity_metric.value))
                        engine_handler.register_query_handler(name)
            return engine_handler
        self._lazy_query_handler = _lazy_handler

        with _handlers_lock:
            _handlers[name] = self

    def internal_handler(self) -> _engine.SimpleSemanticsQueryHandler:
        """
        Get the internal query handler.
        """
        return self._lazy_query_handler()

def ensure_all_handlers_built() -> None:
    """
    Ensure all handlers are built.
    """
    with _handlers_lock:
        for handler in _handlers.values():
            handler.internal_handler()
