"""Simplified Medical Care Pathway (MCP) recommendation logic."""

from typing import Sequence


def recommend_action(state: Sequence[float]) -> int:
    """Return a recommended action index for a given symptom state."""
    diarrhea, constipation = state[2], state[3]
    if diarrhea > constipation:
        return 1  # medication focus
    elif constipation > diarrhea:
        return 2  # lifestyle focus
    return 0  # observation
