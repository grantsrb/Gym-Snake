import numpy as np
from snake import Snake

class Grid():

    """
    This class contains all data related to the grid in which the game is contained.
    The information is stored as a numpy array of pixels.
    The grid is treated as a cartesian [x,y] plane in which [0,0] is located at
    the upper left most pixel and [max_x, max_y] is located at the lower right most pixel.

    Note that it is assumed spaces that can kill a snake have a non-zero value as their 0 channel.
    It is also assumed that HEAD_COLOR has a 255 value as its 0 channel.
    """

    BODY_COLOR = np.array([1,0,0], dtype=np.uint8)
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

    def check_death(self, head_coord):
        """
        Checks the grid to see if argued head_coord has collided with a death space (i.e. snake or wall)

        head_coord - x,y integer coordinates as a tuple, list, or ndarray
        """
        return self.off_grid(head_coord) or self.snake_space(head_coord)

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

    def food_space(self, coord):
        """
        Checks if argued coord is snake food

        coord - x,y integer coordinates as a tuple, list, or ndarray
        """

        return np.array_equal(self.color_of(coord), self.FOOD_COLOR)

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

    def off_grid(self, coord):
        """
        Checks if argued coord is off of the grid

        coord - x,y integer coordinates as a tuple, list, or ndarray
        """

        return coord[0]<0 or coord[0]>=self.grid_size[0] or coord[1]<0 or coord[1]>=self.grid_size[1]

    def snake_space(self, coord):
        """
        Checks if argued coord is occupied by a snake

        coord - x,y integer coordinates as a tuple, list, or ndarray
        """

        color = self.color_of(coord)
        return np.array_equal(color, self.BODY_COLOR) or color[0] == self.HEAD_COLOR[0]
