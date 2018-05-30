import math
import gym_snake_wrapper as snek

def disc_dist(d):
    if d <= 1:
        return 0
    elif d <= 3:
        return 1
    elif d <= 5:
        return 2
    return 3


def disc_angle(a):
    return round(a/(math.pi/4))


def disc_state(s):
    food_d, food_a, dists = s
    food_d = disc_dist(food_d)
    food_a = disc_angle(food_a)
    dists = list(map(lambda d: disc_dist(d), dists))
    return food_d, food_a, dists


class GymSnake:
    def __init__(self):
        self.snek = snek.GymSnake()

    def reset(self):
        obs, rewards, done, info = self.snek.reset()
        obs = disc_state(obs)
        return obs, rewards, done, info

    def step(self, action):
        obs, rewards, done, info = self.snek.step(action)
        obs = disc_state(obs)
        return obs, rewards, done, info

    def render(self):
        self.snek.render()
