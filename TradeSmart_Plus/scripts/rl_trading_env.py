import gym
from gym import spaces
import numpy as np

class TradingEnv(gym.Env):
    def __init__(self, data):
        super(TradingEnv, self).__init__()
        self.data = data
        self.current_step = 0
        self.balance = 10000
        self.position = 0

        # Define the action space: [Hold, Buy, Sell]
        self.action_space = spaces.Discrete(3)

        # Observation space will be stock prices and balance
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(len(data.columns),), dtype=np.float32)

    def step(self, action):
        # Implement trading logic
        pass

    def reset(self):
        # Reset the environment
        self.balance = 10000
        self.position = 0
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        return self.data.iloc[self.current_step].values
