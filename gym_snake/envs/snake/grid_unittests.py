import unittest
from grid import Grid
from snake import Snake
import numpy as np

class GridTests(unittest.TestCase):

    grid_size = [30,30]
    unit_size = 10

    def test_grid_Initialization(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_size = [300,300,3]
        expected_grid = np.zeros(expected_size, dtype=np.uint8)
        expected_grid[:,:,1] = 255
        self.assertTrue(np.array_equal(grid.grid, expected_grid))

    def test_constant_Initialization(self):
        grid = Grid(self.grid_size, self.unit_size)
        self.assertTrue(grid.unit_size == self.unit_size)
        self.assertTrue(np.array_equal(grid.grid_size, self.grid_size))

    def test_color_Initialization(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,255,0], dtype=np.uint8)
        for i in range(grid.grid.shape[0]):
            for j in range(grid.grid.shape[1]):
                self.assertTrue(np.array_equal(grid.grid[i,j,:],expected_color))

    def test_color_of_Color(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,255,0], dtype=np.uint8)
        self.assertTrue(np.array_equal(grid.color_of([0,0]),expected_color))

    def test_color_of_Coordinate(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = [3,2]
        expected_color = np.array([0,0,0], dtype=np.uint8)
        grid.grid[coord[1]*self.unit_size,coord[0]*self.unit_size,:] = expected_color
        self.assertTrue(np.array_equal(grid.color_of(coord),expected_color))

    def test_draw_Positive(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,0,0], dtype=np.uint8)
        coord = [3,2]
        grid.draw(coord, expected_color)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if y >= coord[1]*self.unit_size and y < coord[1]*self.unit_size+grid.unit_size and x >= coord[0]*self.unit_size and x < coord[0]*self.unit_size+grid.unit_size:
                    self.assertTrue(np.array_equal(grid.grid[y,x,:],expected_color))
                else:
                    self.assertFalse(np.array_equal(grid.grid[y,x,:],expected_color))

    def test_draw_Negative(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = grid.SPACE_COLOR
        coord = [3,2]
        grid.draw(coord, grid.BODY_COLOR)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if y >= coord[1]*self.unit_size and y < coord[1]*self.unit_size+grid.unit_size and x >= coord[0]*self.unit_size and x < coord[0]*self.unit_size+grid.unit_size:
                    self.assertFalse(np.array_equal(grid.grid[y,x,:],expected_color))
                else:
                    self.assertTrue(np.array_equal(grid.grid[y,x,:],expected_color))

    def test_draw_snake_Positive(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, head_color=grid.HEAD_COLOR)

        expected_colors = np.array([grid.HEAD_COLOR, grid.BODY_COLOR, grid.BODY_COLOR], dtype=np.uint8)
        expected_coords = np.array([[10,10], [10,9], [10,8]])
        for coord,color in zip(expected_coords, expected_colors):
            self.assertTrue(np.array_equal(grid.color_of(coord), color))

    def test_draw_snake_Negative(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)

        expected_color = grid.SPACE_COLOR
        expected_coords = [(10,10), (10,9), (10,8)]
        for i,j in zip(range(grid.grid_size[0]),range(grid.grid_size[1])):
            coord = (i,j)
            if coord == expected_coords[0] or coord == expected_coords[1] or coord == expected_coords[2]:
                self.assertFalse(np.array_equal(grid.color_of(coord), expected_color))
            else:
                self.assertTrue(np.array_equal(grid.color_of(coord), expected_color))

    def test_draw_snake_Snake_Data(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)

        expected_coords = [[10,8],[10,9]]
        for i in range(snake.body.qsize()):
            self.assertTrue(np.array_equal(snake.body.get(), expected_coords[i]))

    def test_erase_snake(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)
        snake.action(1)
        grid.erase_snake(snake)

        expected_color = grid.SPACE_COLOR
        for i,j in zip(range(grid.grid_size[0]),range(grid.grid_size[1])):
            coord = (i,j)
            self.assertTrue(np.array_equal(grid.color_of(coord), expected_color))

    def test_new_food(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_coord = (10,11)
        for x in range(grid.grid_size[0]):
            for y in range(grid.grid_size[1]):
                coord = (x,y)
                if coord != expected_coord:
                    grid.draw(coord, grid.BODY_COLOR)

        grid.new_food()
        self.assertTrue(np.array_equal(grid.color_of(expected_coord), grid.FOOD_COLOR))



if __name__ == "__main__":
    unittest.main()
