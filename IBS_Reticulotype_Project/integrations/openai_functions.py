"""Utilities for interacting with OpenAI ChatCompletion using function calling."""
from typing import Any, Dict, List
import openai


def chat_with_functions(messages: List[Dict[str, str]], functions: List[Dict[str, Any]]) -> Any:
    """Call OpenAI ChatCompletion with function definitions."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
        )
        return response
    except Exception as e:
        return {"error": str(e)}
