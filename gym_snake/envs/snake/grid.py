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
        self.grid = np.ones((height, width, channels), dtype=np.uint8)
        self.grid[:,:,:] = self.SPACE_COLOR

    def color_of(self, coord):
        """
        Returns the color of the specified coordinate

        coord - x,y integer coordinates as a tuple, list, or np array
        """

        return self.grid[int(coord[1]*self.unit_size), int(coord[0]*self.unit_size), :]

    def draw(self, coord, color):
        """
        Colors a single space on the grid

        coord - x,y integer coordinates as a tuple, list, or np array
        color - [R,G,B] values as a tuple, list, or np array
        """

        x = int(coord[0]*self.unit_size)
        end_x = x+self.unit_size
        y = int(coord[1]*self.unit_size)
        end_y = y+self.unit_size
        self.grid[y:end_y, x:end_x, :] = np.asarray(color, dtype=np.uint8)
