from .doctor_agent import DoctorAgent
from .ibs_env import IBSPatientEnv


class AgentOrchestrator:
    """Manages training and evaluation of the DoctorAgent."""

    def __init__(self, env: IBSPatientEnv | None = None):
        self.env = env or IBSPatientEnv()
        self.agent = DoctorAgent(self.env)

    def train(self, timesteps: int = 1000):
        self.agent.train(timesteps)

    def run_episode(self):
        obs = self.env.reset()
        done = False
        total_reward = 0.0
        while not done:
            action = self.agent.act(obs)
            obs, reward, done, _ = self.env.step(action)
            total_reward += reward
        return total_reward
