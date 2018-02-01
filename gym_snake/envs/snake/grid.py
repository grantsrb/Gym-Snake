import numpy as np
from snake import Snake
from food import Food

class Grid():

    """
    This class contains all data related to the grid in which the game is contained.
    The information is stored as a numpy array of pixels.
    The grid is treated as a cartesian [x,y] plane in which [0,0] is located at
    the upper left most pixel and [max_x, max_y] is located at the lower right most pixel.
    """

    BODY_COLOR = np.array([0,0,0], dtype=np.uint8)
    HEAD_COLOR = np.array([255, 0, 0], dtype=np.uint8)
    FOOD_COLOR = np.array([0,0,255], dtype=np.uint8)
    SPACE_COLOR = np.array([0,255,0], dtype=np.uint8)

    def __init__(self, grid_size=[30,30], unit_size=10):
        """
        grid_size - tuple, list, or ndarray specifying number of atomic units in
                    both the x and y direction
        unit_size - integer denoting the atomic size of grid units in pixels
        """

        self.unit_size = int(unit_size)
        self.grid_size = np.asarray(grid_size, dtype=np.int) # size in terms of units
        height = self.grid_size[1]*self.unit_size
        width = self.grid_size[0]*self.unit_size
        channels = 3
        self.grid = np.zeros((height, width, channels), dtype=np.uint8)
        self.grid[:,:,:] = self.SPACE_COLOR

    def color_of(self, coord):
        """
        Returns the color of the specified coordinate

        coord - x,y integer coordinates as a tuple, list, or ndarray
        """

        return self.grid[int(coord[1]*self.unit_size), int(coord[0]*self.unit_size), :]

    def draw(self, coord, color):
        """
        Colors a single space on the grid

        coord - x,y integer coordinates as a tuple, list, or ndarray
        color - [R,G,B] values as a tuple, list, or ndarray
        """

        x = int(coord[0]*self.unit_size)
        end_x = x+self.unit_size
        y = int(coord[1]*self.unit_size)
        end_y = y+self.unit_size
        self.grid[y:end_y, x:end_x, :] = np.asarray(color, dtype=np.uint8)

    def draw_snake(self, snake, head_color=HEAD_COLOR):
        """
        Draws a snake with the given head color.

        snake - Snake object
        head_color - [R,G,B] values as a tuple, list, or ndarray
        """

        self.draw(snake.head, head_color)
        for i in range(snake.body.qsize()):
            coord = snake.body.get()
            self.draw(coord, self.BODY_COLOR)
            snake.body.put(coord)

    def erase_snake(self, snake):
        """
        Removes the argued snake's body and head from the grid.

        snake - Snake object
        """

        for i in range(snake.body.qsize()):
            self.draw(snake.body.get(), self.SPACE_COLOR)


    def new_food(self):
        """
        Draws a food on a random, open unit of the grid.
        """

        coord_not_found = True
        while(coord_not_found):
            coord = (np.random.randint(0,self.grid_size[0]), np.random.randint(0,self.grid_size[1]))
            if np.array_equal(self.color_of(coord), self.SPACE_COLOR):
                coord_not_found = False
        self.draw(coord, self.FOOD_COLOR)
