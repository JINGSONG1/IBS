from .ibs_env import IBSPatientEnv
from ..explanation.real_mcp_engine import recommend_action


class IBSPatientEnvUpgraded(IBSPatientEnv):
    """Environment that integrates MCP suggestions."""

    def step(self, action: int):
        # if agent chooses a special action (-1), use MCP recommendation
        if action == -1:
            action = recommend_action(self.state)
        return super().step(action)
