import unittest
from food import Food

class SnakeTests(unittest.TestCase):

    food_coord = [0,0]

    def x_Initialization_Test(self):
        cheetos = Food(self.food_coord)
        self.assertTrue(self.food_coord[0] == cheetos.x)

    def y_Initialization_Test(self):
        cheetos = Food(self.food_coord)
        self.assertTrue(self.food_coord[1] == cheetos.y)

    def coord_Initialization_Test(self):
        cheetos = Food(self.food_coord)
        self.assertTrue(np.array_equal(self.food_coord, cheetos.coord))


if __name__ == "__main__":
    unittest.main()
