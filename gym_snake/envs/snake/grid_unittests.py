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
        expected_color = np.array(grid.BODY_COLOR, dtype=np.uint8)
        grid.grid[coord[1]*self.unit_size,coord[0]*self.unit_size,:] = expected_color
        self.assertTrue(np.array_equal(grid.color_of(coord),expected_color))

    def test_draw_Positive(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array(grid.BODY_COLOR, dtype=np.uint8)
        coord = [3,2]
        grid.draw(coord, expected_color)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if y >= coord[1]*self.unit_size and y < coord[1]*self.unit_size+grid.unit_size-grid.unit_gap and x >= coord[0]*self.unit_size and x < coord[0]*self.unit_size+grid.unit_size-grid.unit_gap:
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
                if y >= coord[1]*self.unit_size and y < coord[1]*self.unit_size+grid.unit_size-grid.unit_gap and x >= coord[0]*self.unit_size and x < coord[0]*self.unit_size+grid.unit_size-grid.unit_gap:
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
        for i in range(len(snake.body)):
            self.assertTrue(np.array_equal(snake.body.popleft(), expected_coords[i]))

    def test_erase_snake_body(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)
        snake.action(1)
        grid.erase_snake_body(snake)

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

        self.assertTrue(grid.new_food())
        self.assertTrue(np.array_equal(grid.color_of(expected_coord), grid.FOOD_COLOR))

    def test_new_food_nospace(self):
        grid = Grid(self.grid_size, self.unit_size)
        for x in range(grid.grid_size[0]):
            for y in range(grid.grid_size[1]):
                coord = (x,y)
                grid.draw(coord, grid.BODY_COLOR)
        self.assertFalse(grid.new_food())

    def test_snake_space_BODY(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.BODY_COLOR)
        self.assertTrue(grid.snake_space(coord))

    def test_snake_space_HEAD(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.HEAD_COLOR)
        self.assertTrue(grid.snake_space(coord))

    def test_snake_space_FOOD(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.FOOD_COLOR)
        self.assertFalse(grid.snake_space(coord))

    def test_snake_space_SPACE(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.SPACE_COLOR)
        self.assertFalse(grid.snake_space(coord))

    def test_off_grid_UP(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (0,-1)
        self.assertTrue(grid.off_grid(coord))

    def test_off_grid_RIGHT(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (self.grid_size[0],0)
        self.assertTrue(grid.off_grid(coord))

    def test_off_grid_DOWN(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (0,self.grid_size[1])
        self.assertTrue(grid.off_grid(coord))

    def test_off_grid_LEFT(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (-1,0)
        self.assertTrue(grid.off_grid(coord))

    def test_food_space_FOOD(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.FOOD_COLOR)
        self.assertTrue(grid.food_space(coord))

    def test_food_space_BODY(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.BODY_COLOR)
        self.assertFalse(grid.food_space(coord))

    def test_food_space_HEAD(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.HEAD_COLOR)
        self.assertFalse(grid.food_space(coord))

    def test_food_space_SPACE(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = (10,11)
        grid.draw(coord, grid.SPACE_COLOR)
        self.assertFalse(grid.food_space(coord))

    def test_connect_x(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = grid.BODY_COLOR
        coord1 = [3,2]
        coord2 = [4,2]
        grid.connect(coord1, coord2, expected_color)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if (y == coord1[1]*self.unit_size or y == coord1[1]*self.unit_size+grid.unit_size-grid.unit_gap-1) and (x < coord2[0]*self.unit_size and x >= coord1[0]*self.unit_size+grid.unit_size-grid.unit_gap):
                    self.assertTrue(np.array_equal(grid.grid[y,x,:],expected_color))
                else:
                    self.assertFalse(np.array_equal(grid.grid[y,x,:],expected_color))

    def test_connect_y(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = grid.BODY_COLOR
        coord1 = [2,3]
        coord2 = [2,4]
        grid.connect(coord1, coord2, expected_color)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if (x == coord1[0]*self.unit_size or x == coord1[0]*self.unit_size+grid.unit_size-grid.unit_gap-1) and (y < coord2[1]*self.unit_size and y >= coord1[1]*self.unit_size+grid.unit_size-grid.unit_gap):
                    self.assertTrue(np.array_equal(grid.grid[y,x,:],expected_color))
                else:
                    self.assertFalse(np.array_equal(grid.grid[y,x,:],expected_color))

    def test_erase(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord1 = [2,3]
        coord2 = [2,4]
        grid.draw(coord1, grid.BODY_COLOR)
        grid.draw(coord2, grid.BODY_COLOR)
        grid.connect(coord1,coord2)
        expected_color = grid.SPACE_COLOR
        grid.erase(coord1)
        grid.erase(coord2)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                self.assertTrue(np.array_equal(grid.grid[y,x,:],expected_color))

    def test_erase_connections(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord1 = [2,3]
        coord2 = [2,4]
        grid.draw(coord1, grid.BODY_COLOR)
        grid.connect(coord1,coord2)
        grid.erase_connections(coord1)
        for y in range(grid.grid.shape[0]):
            for x in range(grid.grid.shape[1]):
                if y >= coord1[1]*self.unit_size and y < coord1[1]*self.unit_size+grid.unit_size-grid.unit_gap and x >= coord1[0]*self.unit_size and x < coord1[0]*self.unit_size+grid.unit_size-grid.unit_gap:
                    self.assertTrue(np.array_equal(grid.grid[y,x,:],grid.BODY_COLOR))
                else:
                    self.assertFalse(np.array_equal(grid.grid[y,x,:],grid.BODY_COLOR))

    def test_open_space(self):
        grid = Grid([10,10], self.unit_size)
        self.assertTrue(grid.open_space == 100)
        for i in range(1,10):
            grid.draw([i,i], grid.BODY_COLOR)
            self.assertTrue(grid.open_space == 100-i)
        for i in range(1,10):
            grid.erase([i,i])
            self.assertTrue(grid.open_space == 91+i)
        snake_len = 3
        snake = Snake((5,5), snake_len)
        grid.draw_snake(snake)
        self.assertTrue(grid.open_space == 100-snake_len)

    def test_open_space_draw(self):
        grid = Grid([10,10], self.unit_size)
        for i in range(1,10):
            grid.draw([i,i], grid.BODY_COLOR)
            self.assertTrue(grid.open_space == 100-i)

    def test_open_space_erase(self):
        grid = Grid([10,10], self.unit_size)
        for i in range(1,10):
            grid.erase([i,i])
            self.assertTrue(grid.open_space == 100+i)

    def test_open_space_draw_snake(self):
        grid = Grid([10,10], self.unit_size)
        snake_len = 3
        snake = Snake((5,5), snake_len)
        grid.draw_snake(snake)
        self.assertTrue(grid.open_space == 100-snake_len)

    def test_open_space_erase_snake_body(self):
        grid = Grid([10,10], self.unit_size)
        snake_len = 3
        snake = Snake((5,5), snake_len)
        grid.erase_snake_body(snake)
        self.assertTrue(grid.open_space == 100+snake_len-1)


if __name__ == "__main__":
    unittest.main()
