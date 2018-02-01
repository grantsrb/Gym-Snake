from gym_snake.envs.snake import Snake
from gym_snake.envs.snake import Grid
import numpy as np

class Controller():
    """
    This class combines the Snake, Food, and Grid classes to handle the game logic.
    """

    def __init__(self, grid_size=[30,30], unit_size=10, snake_size=3, n_snakes=1, n_foods=1):

        assert n_snakes < grid_size[0]//3
        assert snake_size < grid_size[1]//2

        self.done = False
        unit_size = np.maximum(4, unit_size)
        self.grid = Grid(grid_size, unit_size)

        self.snakes = []
        for i in range(1,n_snakes+1):
            start_coord = [i*grid_size[0]//(n_snakes+1), snake_size+1]
            self.snakes.append(Snake(start_coord, snake_size))
            color = [self.grid.HEAD_COLOR[0], (i-1)*255//n_snakes, 0]
            self.snakes[-1].head_color = color
            self.grid.draw_snake(self.snakes[-1], color)

        for i in range(n_foods):
            self.grid.new_food()

    def action(self, direction, snake_idx=0):
        """
        Moves the specified snake according to the game's rules dependent on the direction.
        Checks for food and death collisions.
        """

        snake = self.snakes[snake_idx]
        assert type(snake) != type(None)

        # Cover old head position with body
        self.grid.draw(snake.head, self.grid.BODY_COLOR)
        # Find next head position conditioned on direction
        snake.action(direction)

        # Check for death of snake
        new_coord = snake.head
        if self.grid.check_death(new_coord):
            self.grid.erase_snake(snake)
            self.snakes[snake_idx] = None
            return -1

        # Check for reward
        if self.grid.food_space(new_coord):
            reward = 1
            self.grid.new_food()
        else:
            reward = 0
            empty_coord = snake.body.get()
            self.grid.draw(empty_coord, self.grid.SPACE_COLOR)

        # Draw new head position
        self.grid.draw(snake.head, snake.head_color)

        return reward

    def step(self, directions):
        """
        Takes an action for each snake in the specified direction and collects their rewards
        and dones.

        directions - tuple, list, or ndarray of directions corresponding to each snake.
        """

        # Ensure no more play until reset
        if self.done:
            return self.grid.grid, [0]*len(directions), done, {"snakes_left":snakes_left}

        done = True
        rewards = []
        snakes_left = 0

        if type(directions) == type(int()):
            directions = [directions]
        for i, direction in enumerate(directions):
            if type(self.snakes[i]) != type(None):
                done = False
                rewards.append(self.action(direction, i))
                snakes_left += 1
            else:
                rewards.append(0)

        self.done = done
        if len(rewards) is 1:
            return self.grid.grid, rewards[0], done, {"snakes_left":snakes_left}
        else:
            return self.grid.grid, rewards, done, {"snakes_left":snakes_left}
