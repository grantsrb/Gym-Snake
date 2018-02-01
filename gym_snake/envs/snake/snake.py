from queue import Queue
import numpy as np

class Snake():

    """
    The Snake class holds all pertinent information regarding the Snake's movement and boday.
    The position of the snake is tracked using a queue that stores the positions of the body.
    
    Note:
    A potentially more space efficient implementation could track directional changes rather
    than tracking each location of the snake's body.
    """

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def __init__(self, head_xy, length=3):

        assert type(head_

        self.direction = self.UP
        self.head = np.asarray(head_xy).astype(np.int)
        self.body = Queue()
        for i in range(length, 0, -1):
            self.body.put(self.head-np.asarray([i,0]).astype(np.int))
    
    def step(self, coord, direction):
        """
        Takes a step in the specified direction from the specified coordinate.

        coord - list, tuple, or numpy array
        direction - integer from 1-4 inclusive.
            1: up
            2: right
            3: down
            4: left
        """

        assert direction < 5 and direction > 0
        
        if direction == self.UP:
            return np.asarray([coord[0], coord[1]+1]).astype(np.int)
        elif direction == self.RIGHT:
            return np.asarray([coord[0]+1, coord[1]]).astype(np.int)
        elif direction == self.DOWN:
            return np.asarray([coord[0], coord[1]-1]).astype(np.int)
        else:
            return np.asarray([coord[0]-1, coord[1]]).astype(np.int)

    def action(self, direction):
        """
        This method sets a new head coordinate and puts the old head
        into the body queue. The Controller class handles popping the
        last piece of the body if no food is eaten on this step.

        The direction can be any integer value, but will be collapsed
        to 1, 2, 3, or 4 corresponding to up, right, down, left respectively.

        direction - integer from 1-4 inclusive.
            1: up
            2: right
            3: down
            4: left
        """

        # Ensure direction is either 1, 2, 3, or 4
        direction = (int(direction) % 4) + 1 

        if np.abs(self.direction-direction) != 2:
            self.direction = direction

        self.body.put(self.head)
        self.head = self.step(self.head, direction)

        return self.head

