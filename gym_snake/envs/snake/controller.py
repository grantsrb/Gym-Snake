from gym_snake.envs.snake import Snake
from gym_snake.envs.snake import Grid


class Controller:
    """
    This class combines the Snake, Food, and Grid classes to handle the game logic.
    """

    def __init__(self, grid_size=[30, 30], unit_size=10, unit_gap=1, snake_size=3, random_init=True):

        assert snake_size < grid_size[1]//2
        assert 0 <= unit_gap < unit_size

        self.grid = Grid(grid_size, unit_size, unit_gap)

        start_coord = [grid_size[0]//2, snake_size+1]
        self.snake = Snake(start_coord, snake_size)
        self.dead_snake = None
        color = [self.grid.HEAD_COLOR[0], 0, 0]
        self.snake.head_color = color
        self.grid.draw_snake(self.snake, color)

        if not random_init:
            start_coord = [grid_size[0]//2, grid_size[1]-5]
            self.grid.place_food(start_coord)
        else:
            self.grid.new_food()

    def move_snake(self, direction):
        """
        Moves the snake according to the game's rules dependent on the direction.
        Does not draw head and does not check for reward scenarios. See move_result for these
        functionalities.
        """

        snake = self.snake
        if snake is None:
            return

        # Cover old head position with body
        self.grid.cover(snake.head, self.grid.BODY_COLOR)
        # Erase tail without popping so as to redraw if food eaten
        self.grid.erase(snake.body[0])
        # Find and set next head position conditioned on direction
        snake.action(direction)

    def move_result(self):
        """
        Checks for food and death collisions after moving snake. Draws head of snake if
        no death scenarios.
        """

        snake = self.snake
        if snake is None:
            return 0

        # Check for death of snake
        if self.grid.check_death(snake.head):
            self.dead_snake = self.snake
            self.snake = None
            self.grid.cover(snake.head, snake.head_color)  # Avoid miscount of grid.open_space
            self.grid.connect(snake.body.popleft(), snake.body[0], self.grid.SPACE_COLOR)
            reward = -1
        # Check for reward
        elif self.grid.food_space(snake.head):
            self.grid.draw(snake.body[0], self.grid.BODY_COLOR) # Redraw tail
            self.grid.connect(snake.body[0], snake.body[1], self.grid.BODY_COLOR)
            self.grid.cover(snake.head, snake.head_color) # Avoid miscount of grid.open_space
            reward = 1
            self.grid.new_food()
        else:
            reward = 0
            empty_coord = snake.body.popleft()
            self.grid.connect(empty_coord, snake.body[0], self.grid.SPACE_COLOR)
            self.grid.draw(snake.head, snake.head_color)

        self.grid.connect(snake.body[-1], snake.head, self.grid.BODY_COLOR)
        return reward

    def kill_snake(self):
        """
        Deletes snake from game
        """
        assert self.dead_snake is not None
        self.grid.erase(self.dead_snake.head)
        self.grid.erase_snake_body(self.dead_snake)
        self.dead_snake = None

    def get_state(self):
        """
        Creates a state from game parameters
        """
        snake = self.snake
        if snake is None:
            return None
        head = snake.head
        body = snake.body
        food = self.grid.food_coord
        return head, body, food

    def step(self, direction):
        """
        Takes an action for snake in the specified direction and collects its reward.

        direction - integer direction for the snake.
        """

        # Ensure no more play until reset
        if (self.snake is None and self.dead_snake is not None) or self.grid.open_space < 1:
            return self.grid.grid.copy(), 0, True, None

        if self.snake is None and self.dead_snake is not None:
            self.kill_snake()
        self.move_snake(direction)
        reward = (self.move_result())

        done = reward == -1 or self.grid.open_space < 1
        return 0, reward, done, None
