import pytest

from adapters.llm_mock import MockLLM


def test_replays_tool_request_then_final_answer() -> None:
    tool_request = {"tool": "server_status"}
    final_answer = {"text": "Server is healthy."}
    model = MockLLM[str, dict[str, str]]([tool_request, final_answer])

    assert model.complete("Check server.") == tool_request
    assert model.complete("Tool result: healthy.") == final_answer
    assert model.requests == ("Check server.", "Tool result: healthy.")


def test_raises_scripted_error_then_reports_exhaustion() -> None:
    model = MockLLM[str, str]([TimeoutError("model timed out"), "recovered"])

    with pytest.raises(TimeoutError, match="model timed out"):
        model.complete("first")
    assert model.complete("retry") == "recovered"
    with pytest.raises(RuntimeError, match="response script exhausted"):
        model.complete("extra")
    assert model.requests == ("first", "retry", "extra")


def test_records_independent_request_snapshots() -> None:
    model = MockLLM[list[str], str](["answer"])
    request = ["original"]

    model.complete(request)
    request.append("changed")
    model.requests[0].append("changed again")

    assert model.requests == (["original"],)
