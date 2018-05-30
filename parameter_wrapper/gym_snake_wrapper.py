import gym
import gym_snake
import math


def calc_dist(x, y):
    d = math.sqrt(x ** 2 + y ** 2)
    return d


def calc_angle(x, y):
    return math.atan2(x, y)


def direction_2_angle(d):
    return math.pi*(((d-1)*-1) % 4)


class GymSnake:
    def __init__(self):
        # Construct environment
        self.env = gym.make('snake-v0')
        self.env.reset()  # Constructs an instance of the game
        # Controller
        self.game_controller = self.env.controller
        # Grid
        self.grid_object = self.game_controller.grid
        # Snake(s)
        self.snake = self.game_controller.snakes[0]

    def _find_collision_distance(self, position, direction_x, direction_y):
        i = 0
        while True:
            i += 1
            position = (position[0] + direction_x, position[1] + direction_y)
            if self.grid_object.off_grid(position) or self.grid_object.snake_space(position):
                return i

    def _rotate_radial_collisions(self, c):
        # TODO: Check whether this rotates it backwards...
        d = self.snake.direction
        c = c[-d:] + c[:-d]
        del c[3]  # Remove backwards facing direction as the snek cannot go backwards
        return c

    def _get_radial_collisions(self):
        directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
        collisions = []
        for (x, y) in directions:
            collisions.append(self._find_collision_distance(self.snake.head, x, y))
        collisions = self._rotate_radial_collisions(collisions)
        return collisions

    def _get_state(self):
        food_rel_x = self.snake.head[0] - self.grid_object.food_coord[0]
        food_rel_y = self.snake.head[1] - self.grid_object.food_coord[1]
        f_dist = calc_dist(food_rel_x, food_rel_y)
        f_angle = (calc_angle(food_rel_x, food_rel_y) - direction_2_angle(self.snake.direction)) % (2*math.pi)
        coll = self._get_radial_collisions()
        return f_dist, f_angle, coll

    def reset(self):
        self.env.reset()
        state = self._get_state()
        return state, 0, False, None

    def step(self, action):
        _, rewards, done, info = self.game_controller.step(action)
        obs = self._get_state()
        return obs, rewards, done, info

    def render(self):
        self.env.render()
