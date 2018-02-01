import unittest
from snake import Snake

class SnakeTests(unittest.TestCase):

    head_xy = [0,0]
    bod_len = 3

    def head_Initialization_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        self.assertTrue(np.array_equal(self.head_xy, kaa.head))

    def direction_Initialization_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        self.assertTrue(kaa.UP == kaa.direction)

    def body_Initialization_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_body_coords = np.asarray([[0,-3], [0,-2], [0,-1]])
        actual_body_coords = []
        for i in range(kaa.body.qsize()):
            self.assertTrue(np.array_equal(kaa.body.get(), expected_body_coords[i]))

    def step_UP_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,1]
        actual_coord = kaa.step(kaa.UP)
        self.assertTrue(expected_coord == actual_coord)

    def step_RIGHT_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.step(kaa.RIGHT)
        self.assertTrue(expected_coord == actual_coord)

    def step_DOWN_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,-1]
        actual_coord = kaa.step(kaa.DOWN)
        self.assertTrue(expected_coord == actual_coord)

    def step_LEFT_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.step(kaa.LEFT)
        self.assertTrue(expected_coord == actual_coord)

    def action_UP_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,1]
        actual_coord = kaa.action(kaa.UP)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_RIGHT_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.action(kaa.RIGHT)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_DOWN_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,-1]
        actual_coord = kaa.action(kaa.DOWN)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_LEFT_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.action(kaa.LEFT)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_UP_outofrange_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,1]
        actual_coord = kaa.action(kaa.UP+4)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_RIGHT_outofrange_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.action(kaa.RIGHT+4)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_DOWN_outofrange_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,-1]
        actual_coord = kaa.action(kaa.DOWN+4)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)

    def action_LEFT_outofrange_Test(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.action(kaa.LEFT+4)
        self.assertTrue(expected_coord == actual_coord)
        self.assertTrue(expected_coord == kaa.head)


if __name__ == "__main__":
    unittest.main()
