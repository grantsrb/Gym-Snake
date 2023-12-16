import os, subprocess, time, signal
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_snake.envs.snake import Controller, Discrete
from gym_snake.envs.snake_env import SnakeEnv

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: see matplotlib documentation for installation https://matplotlib.org/faq/installing_faq.html#installation".format(e))

class SnakeExtraHardEnv(SnakeEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self, grid_size=[25,25], unit_size=10, unit_gap=1, snake_size=5, n_snakes=3, n_foods=2, random_init=True):
        super().__init__(
            grid_size=grid_size,
            unit_size=unit_size,
            unit_gap=unit_gap,
            snake_size=snake_size,
            n_snakes=n_snakes,
            n_foods=n_foods,
            random_init=random_init)
