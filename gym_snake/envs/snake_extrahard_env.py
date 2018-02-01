import os, subprocess, time, signal
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_snake.envs.snake import Controller

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: see matplotlib documentation for installation https://matplotlib.org/faq/installing_faq.html#installation".format(e))

class SnakeExtraHardEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, grid_size=[15,15], unit_size=10, snake_size=5, n_snakes=1, n_foods=1):
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

    def _seed(self, x):
        pass

    @property
    def action_space(self):
        return self._action_space
