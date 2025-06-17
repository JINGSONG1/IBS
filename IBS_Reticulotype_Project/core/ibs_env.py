import gym
import numpy as np
import pandas as pd

class IBSEnv(gym.Env):
    """Simple RL environment for IBS patient simulation."""
    metadata = {"render_modes": ["human"]}

    def __init__(self, patient_df: pd.DataFrame):
        super().__init__()
        self.patient_df = patient_df
        # action: 0=diet, 1=medication, 2=probiotic
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=0.0, high=10.0, shape=(5,), dtype=np.float32)
        self.state = None
        self.steps = 0

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        super().reset(seed=seed)
        sample = self.patient_df.sample(1, random_state=seed).iloc[0]
        self.state = sample[['anxiety','sleep_quality','diarrhea_freq','constipation_freq','bloating_freq']].astype(np.float32).to_numpy()
        self.steps = 0
        return self.state, {}

    def step(self, action: int):
        assert self.state is not None, "Call reset before step"
        self.steps += 1
        if action == 0:
            self.state[0] = max(0.0, self.state[0] - np.random.rand())
        elif action == 1:
            self.state[2] = max(0.0, self.state[2] - np.random.rand())
            self.state[3] = max(0.0, self.state[3] - np.random.rand())
        elif action == 2:
            self.state[4] = max(0.0, self.state[4] - np.random.rand())
        reward = -float(self.state.sum())
        done = self.steps >= 10
        return self.state, reward, done, False, {}

    def render(self):
        print(f"Current state: {self.state}")
