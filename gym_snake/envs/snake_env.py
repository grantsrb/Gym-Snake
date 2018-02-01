import os, subprocess, time, signal
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake import Controller

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: see matplotlib documentation for installation https://matplotlib.org/faq/installing_faq.html#installation".format(e))

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, grid_size=[30,30], unit_size=10, snake_size=3, n_snakes=1, n_foods=1):
        self.grid_size = grid_size
        self.unit_size = unit_size
        self.snake_size = snake_size
        self.n_snakes = n_snakes
        self.n_foods = n_foods
        self.viewer = None

    def _step(self, action):
        return self.controller.step(action)

    def _reset(self):
        self.controller = Controller(self.grid_size, self.unit_size, self.snake_size, self.n_snakes, self.n_foods)
        self.last_obs = self.controller.grid.grid
        return self.last_obs

    def _render(self, mode='human', close=False):
        if self.viewer is None:
            self.viewer = plt.imshow(self.last_obs)
        else:
            self.viewer.set_data(self.last_obs)
        plt.pause(0.1)
        plt.draw()
