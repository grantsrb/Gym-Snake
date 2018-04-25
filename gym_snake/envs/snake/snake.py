from queue import deque
import numpy as np

class Snake():

    """
    The Snake class holds all pertinent information regarding the Snake's movement and boday.
    The position of the snake is tracked using a queue that stores the positions of the body.

    Note:
    A potentially more space efficient implementation could track directional changes rather
    than tracking each location of the snake's body.
    """

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, head_coord_start, length=3):
        """
        head_coord_start - tuple, list, or ndarray denoting the starting coordinates for the snake's head
        length - starting number of units in snake's body
        """

        self.direction = self.DOWN
        self.head = np.asarray(head_coord_start).astype(np.int)
        self.head_color = np.array([255,0,0], np.uint8)
        self.body = deque()
        for i in range(length-1, 0, -1):
            self.body.append(self.head-np.asarray([0,i]).astype(np.int))

    def step(self, coord, direction):
        """
        Takes a step in the specified direction from the specified coordinate.

        coord - list, tuple, or numpy array
        direction - integer from 1-4 inclusive.
            0: up
            1: right
            2: down
            3: left
        """

        assert direction < 4 and direction >= 0

        if direction == self.UP:
            return np.asarray([coord[0], coord[1]-1]).astype(np.int)
        elif direction == self.RIGHT:
            return np.asarray([coord[0]+1, coord[1]]).astype(np.int)
        elif direction == self.DOWN:
            return np.asarray([coord[0], coord[1]+1]).astype(np.int)
        else:
            return np.asarray([coord[0]-1, coord[1]]).astype(np.int)

    def action(self, direction):
        """
        This method sets a new head coordinate and appends the old head
        into the body queue. The Controller class handles popping the
        last piece of the body if no food is eaten on this step.

        The direction can be any integer value, but will be collapsed
        to 0, 1, 2, or 3 corresponding to up, right, down, left respectively.

        direction - integer from 0-3 inclusive.
            0: up
            1: right
            2: down
            3: left
        """

        # Ensure direction is either 0, 1, 2, or 3
        direction = (int(direction) % 4)

        if np.abs(self.direction-direction) != 2:
            self.direction = direction

        self.body.append(self.head)
        self.head = self.step(self.head, self.direction)

        return self.head
