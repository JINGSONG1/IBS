import numpy as np
import gym
from gym import spaces

class IBSPatientEnv(gym.Env):
    """A simple environment simulating IBS patient symptom progression."""

    def __init__(self, max_steps: int = 10):
        super().__init__()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=10, shape=(5,), dtype=np.float32)
        self.max_steps = max_steps
        self.state = None
        self.current_step = 0

    def reset(self):
        self.state = np.random.randint(low=0, high=7, size=5).astype(np.float32)
        self.current_step = 0
        return self.state

    def step(self, action: int):
        assert self.action_space.contains(action), "Invalid Action"
        # reward encourages lower symptom values
        reward = -float(np.sum(self.state))
        # apply action effects (very simplified)
        if action == 1:  # medication
            self.state = np.maximum(0, self.state - np.random.randint(1, 3, size=5))
        elif action == 2:  # lifestyle change
            self.state = np.maximum(0, self.state - np.random.randint(0, 2, size=5))
        else:  # no treatment
            self.state = np.minimum(10, self.state + np.random.randint(0, 2, size=5))
        self.current_step += 1
        done = bool(self.current_step >= self.max_steps or np.sum(self.state) == 0)
        return self.state, reward, done, {}
