import asyncio
import os
import uuid
from unittest.mock import MagicMock, create_autospec

import pytest
from huggingface_hub import (
    AsyncInferenceClient,
    ChatCompletionStreamOutput,
    ChatCompletionStreamOutputChoice,
    ChatCompletionStreamOutputDelta,
)
from openai import AsyncOpenAI
from openai.types.chat.chat_completion_chunk import (
    ChatCompletionChunk,
    Choice,
    ChoiceDelta,
)


def get_async_example_files() -> list[str]:
    """Get list of asynchronous example files to test

    Returns:
        list[str]: List of paths to asynchronous example files
    """
    examples_dir = "examples/models"
    if not os.path.exists(examples_dir):
        return []

    async_files = []
    for f in os.listdir(examples_dir):
        if not f.endswith(".py"):
            continue

        filepath = os.path.join(examples_dir, f)
        with open(filepath) as file:
            content = file.read()
            if "stream=True" in content:
                async_files.append(filepath)

    return async_files


@pytest.fixture
def mock_clients(monkeypatch):
    """Fixture providing mocked API clients"""

    # Add async mock client
    async def async_openai_fake_return(*args, **kwargs):
        async def async_iter():
            yield ChatCompletionChunk(
                id=str(uuid.uuid4()),
                choices=[
                    Choice(
                        index=0,
                        delta=ChoiceDelta(
                            content="chunk0",
                        ),
                    )
                ],
                model="gpt-4o",
                usage={
                    "prompt_tokens": 10,
                    "completion_tokens": 10,
                    "total_tokens": 20,
                },
                created=1727238800,
                system_fingerprint=None,
                object="chat.completion.chunk",
            )

        return async_iter()

    async_base_mock = create_autospec(AsyncOpenAI, spec_set=False, instance=True)
    async_base_mock.chat = MagicMock()
    async_base_mock.chat.completions = MagicMock()
    async_base_mock.chat.completions.create = MagicMock(
        side_effect=async_openai_fake_return
    )

    monkeypatch.setattr("openai.AsyncOpenAI", lambda *args, **kwargs: async_base_mock)

    # Add HF mock client
    async def hf_fake_return(*args, **kwargs):
        async def async_iter():
            yield ChatCompletionStreamOutput(
                id=str(uuid.uuid4()),
                choices=[
                    ChatCompletionStreamOutputChoice(
                        index=0,
                        delta=ChatCompletionStreamOutputDelta(
                            content="chunk0",
                            role="assistant",
                        ),
                    )
                ],
                model="gpt2",
                usage={
                    "prompt_tokens": 10,
                    "completion_tokens": 10,
                    "total_tokens": 20,
                },
                created=1727238800,
                system_fingerprint=None,
            )

        return async_iter()

    hf_base_mock = create_autospec(AsyncInferenceClient, spec_set=False, instance=True)
    hf_base_mock.chat = MagicMock()
    hf_base_mock.chat.completions = MagicMock()
    hf_base_mock.chat.completions.create = MagicMock(side_effect=hf_fake_return)

    monkeypatch.setattr(
        "huggingface_hub.AsyncInferenceClient", lambda *args, **kwargs: hf_base_mock
    )


@pytest.mark.parametrize("example_path", get_async_example_files())
@pytest.mark.asyncio
async def test_async_example_files(example_path, mock_clients):
    """Test that async example files execute without errors"""
    print(f"Executing async example: {os.path.basename(example_path)}")

    with open(example_path) as f:
        content = f.read()

    exec_globals = {}
    exec(content, exec_globals)
    async_functions = [
        f
        for f in exec_globals.values()
        if callable(f) and asyncio.iscoroutinefunction(f)
    ]
    if async_functions:
        await async_functions[0]()
    else:
        pytest.fail(f"No async functions found in {os.path.basename(example_path)}")
