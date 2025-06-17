import numpy as np
import pandas as pd
import gym
from gym import spaces


class MCPEnvironment(gym.Env):
    """Simple multi-core platform environment using time series tasks."""

    def __init__(self, task_csv: str, num_cores: int = 4):
        super().__init__()
        self.tasks = pd.read_csv(task_csv, parse_dates=['timestamp'])
        self.tasks.sort_values('timestamp', inplace=True)
        self.num_cores = num_cores
        self.current_index = 0
        self.core_load = np.zeros(self.num_cores, dtype=np.float32)

        self.observation_space = spaces.Box(
            low=0.0, high=np.finfo(np.float32).max, shape=(self.num_cores,), dtype=np.float32
        )
        self.action_space = spaces.Discrete(self.num_cores)

    def reset(self):
        self.current_index = 0
        self.core_load = np.zeros(self.num_cores, dtype=np.float32)
        return self.core_load.copy()

    def step(self, action):
        if not self.action_space.contains(action):
            raise ValueError("Invalid action")
        reward = 0.0
        done = False

        # assign next task to the chosen core
        if self.current_index < len(self.tasks):
            duration = float(self.tasks.iloc[self.current_index]['duration'])
            self.core_load[action] += duration
            # negative waiting time as reward (want to minimize latency)
            reward = -self.core_load[action]
            self.current_index += 1
        else:
            done = True

        # advance time by one unit for all cores
        self.core_load = np.maximum(0.0, self.core_load - 1.0)
        obs = self.core_load.copy()
        return obs, reward, done, {}
