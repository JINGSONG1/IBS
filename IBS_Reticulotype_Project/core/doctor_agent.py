from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from .ibs_env import IBSPatientEnv

class DoctorAgent:
    """Reinforcement learning agent that interacts with the IBS environment."""

    def __init__(self, env: IBSPatientEnv | None = None):
        self.env = env or IBSPatientEnv()
        self.model = PPO("MlpPolicy", make_vec_env(lambda: self.env, n_envs=1), verbose=0)

    def train(self, timesteps: int = 1000):
        self.model.learn(total_timesteps=timesteps)

    def act(self, observation):
        action, _ = self.model.predict(observation, deterministic=True)
        return int(action)
