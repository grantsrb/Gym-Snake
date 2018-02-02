import unittest
import numpy as np
from gym_snake.envs.snake import Snake

class SnakeTests(unittest.TestCase):

    head_xy = [0,0]
    bod_len = 3

    def test_head_Initialization(self):
        kaa = Snake(self.head_xy, self.bod_len)
        self.assertTrue(np.array_equal(self.head_xy, kaa.head))

    def test_body_Initialization(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_body_coords = [[0,-2], [0,-1]]
        for i in range(len(kaa.body)):
            self.assertTrue(np.array_equal(kaa.body.popleft(), expected_body_coords[i]))

    def test_step_UP(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,-1]
        actual_coord = kaa.step(kaa.head, kaa.UP)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_step_RIGHT(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.step(kaa.head,kaa.RIGHT)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_step_DOWN(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [0,1]
        actual_coord = kaa.step(kaa.head,kaa.DOWN)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_step_LEFT(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.step(kaa.head,kaa.LEFT)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_UP(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.UP
        expected_coord = [0,-1]
        actual_coord = kaa.action(kaa.UP)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_RIGHT(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.action(kaa.RIGHT)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_DOWN(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.DOWN
        expected_coord = [0,1]
        actual_coord = kaa.action(kaa.DOWN)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_LEFT(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.action(kaa.LEFT)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_UP_outofrange(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.UP
        expected_coord = [0,-1]
        actual_coord = kaa.action(kaa.UP+4)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_RIGHT_outofrange(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [1,0]
        actual_coord = kaa.action(kaa.RIGHT+4)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_DOWN_outofrange(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.DOWN
        expected_coord = [0,1]
        actual_coord = kaa.action(kaa.DOWN+4)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_LEFT_outofrange(self):
        kaa = Snake(self.head_xy, self.bod_len)
        expected_coord = [-1,0]
        actual_coord = kaa.action(kaa.LEFT+4)
        self.assertTrue(np.array_equal(expected_coord,actual_coord))

    def test_action_UP_backwards(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.UP
        head = kaa.action(kaa.DOWN)
        self.assertTrue(np.array_equal(head, [0,-1]))

    def test_action_RIGHT_backwards(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.RIGHT
        head = kaa.action(kaa.LEFT)
        self.assertTrue(np.array_equal(head, [1,0]))

    def test_action_DOWN_backwards(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.DOWN
        head = kaa.action(kaa.UP)
        self.assertTrue(np.array_equal(head, [0,1]))

    def test_action_LEFT_backwards(self):
        kaa = Snake(self.head_xy, self.bod_len)
        kaa.direction = kaa.LEFT
        head = kaa.action(kaa.RIGHT)
        self.assertTrue(np.array_equal(head, [-1,0]))



if __name__ == "__main__":
    unittest.main()
