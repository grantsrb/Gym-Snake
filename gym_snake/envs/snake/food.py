"""
This class holds the coordinates for the snake food to give
rewards and help your snake grow.
"""
class Food():
    def __init__(self, coord=[0,0]):
        self.x = coords[0]
        self.y = coords[1]
        self.coord = np.asarray(coord).astype(np.int)

