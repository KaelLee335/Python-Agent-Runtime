"""Deterministic offline test double with a provisional, generic API."""

from collections import deque
from collections.abc import Iterable
from copy import deepcopy
from typing import Generic, TypeVar

RequestT = TypeVar("RequestT")
ResponseT = TypeVar("ResponseT")


class MockLLM(Generic[RequestT, ResponseT]):
    """Replay scripted responses or exceptions and record request snapshots."""

    def __init__(self, responses: Iterable[ResponseT | Exception]) -> None:
        self._responses = deque(responses)
        self._requests: list[RequestT] = []

    @property
    def requests(self) -> tuple[RequestT, ...]:
        return tuple(deepcopy(self._requests))

    def complete(self, request: RequestT) -> ResponseT:
        self._requests.append(deepcopy(request))
        if not self._responses:
            raise RuntimeError("Mock LLM response script exhausted")
        response = self._responses.popleft()
        if isinstance(response, Exception):
            raise response
        return response
