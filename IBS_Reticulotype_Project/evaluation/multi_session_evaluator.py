import numpy as np
from typing import Any

from ..core.agent_orchestrator import AgentOrchestrator


class MultiSessionEvaluator:
    """Evaluate an agent across multiple simulated patient sessions."""

    def __init__(self, orchestrator: AgentOrchestrator | None = None):
        self.orchestrator = orchestrator or AgentOrchestrator()

    def evaluate(self, episodes: int = 5) -> dict[str, Any]:
        rewards = []
        for _ in range(episodes):
            reward = self.orchestrator.run_episode()
            rewards.append(reward)
        return {
            "mean_reward": float(np.mean(rewards)),
            "std_reward": float(np.std(rewards)),
            "episodes": episodes,
        }

if __name__ == "__main__":
    evaluator = MultiSessionEvaluator()
    print(evaluator.evaluate())
