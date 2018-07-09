# gym-snake

#### Created in response to OpenAI's [Requests for Research 2.0](https://blog.openai.com/requests-for-research-2/)

## Description
gym-snake is a multi-agent implementation of the classic game [snake](https://www.youtube.com/watch?v=wDbTP0B94AM) that is made as an OpenAI gym environment.

The two environments this repo offers are snake-v0 and snake-plural-v0. snake-v0 is the classic snake game. See the section on SnakeEnv for more details. snake-plural-v0 is a version of snake with multiple snakes and multiple snake foods on the map. See the section on SnakeExtraHardEnv for more details. 

Many of the aspects of the game can be changed for both environments. See the Game Details section for specifics.

## Dependencies
- pip
- gym
- numpy
- matplotlib

## Installation
1. Clone this repository
2. Navigate to the cloned repository
3. Run command `$ pip install -e ./`

## Using gym-snake
After installation, you can use gym-snake by making one of two gym environments.

#### SnakeEnv
Use `gym.make('snake-v0')` to make a new snake environment with the following default options (see Game Details to understand what each variable does):

    grid_size = [15,15]
    unit_size = 10
    unit_gap = 1
    snake_size = 3
    n_snakes = 1
    n_foods = 1

#### SnakeExtraHardEnv
Use `gym.make('snake-plural-v0')` to make a new snake environment with the following default parameters (see Game Details to understand what each variable does):

    grid_size = [25,25]
    unit_size = 10
    unit_gap = 1
    snake_size = 5
    n_snakes = 3
    n_foods = 2


## Game Details
You're probably familiar with the game of snake. This is an OpenAI gym implementation of the game with multi snake and multi food options.

#### Rewards
A +1 reward is returned when a snake eats a food.

A -1 reward is returned when a snake dies.

No extra reward is given for victory snakes in plural play.

#### Game Options

- _grid_size_ - An x,y coordinate denoting the number of units on the snake grid (width, height).
- _unit_size_ - Number of numpy pixels within a single grid unit.
- _unit_gap_ - Number of pixels separating each unit of the grid. Space between the units can be useful to understand the direction of the snake's body.
- _snake_size_ - Number of body units for each snake at start of game
- _n_snakes_ - Number of individual snakes on grid
- _n_foods_ - Number of food units (the stuff that makes the snakes grow) on the grid at any given time.
- _random_init_ - If set to false, the food units initialize to the same location at each reset.

Each of these options are member variables of the environment and will come into effect after the environment is reset. For example, if you wanted to use 5 food tokens in the regular version, you can be set the number of food tokens using the following code:

    env = gym.snake('snake-v0')
    env.n_foods = 5
    observation = env.reset()

This will create a vanilla snake environment with 5 food tokens on the map.


#### Environment Parameter Examples
Below is the default setting for `snake-v0` play, 15x15 unit grid.

![default](./imgs/default.png)


Below is the default setting for `snake-plural-v0` play, 25x25 unit grid.

![default](./imgs/default_plural.png)

Below is `env.unit_gap` == 0 and a 30x30 grid.

![default](./imgs/nogap.png)

Below set `env.unit_gap` half the unit size with a 15x15 sized grid.

![default](./imgs/widegap.png)

Below is a big grid with lots of food and small snakes.

![default](./imgs/biggrid.png)

#### General Info
The snake environment has three main interacting classes to construct the environment. The three are a Snake class, a Grid class, and a Controller class. Each holds information about the environment, and each can be accessed through the gym environment.

    import gym
    import gym_snake

    # Construct Environment
    env = gym.make('snake-v0')
    observation = env.reset() # Constructs an instance of the game

    # Controller
    game_controller = env.controller

    # Grid
    grid_object = game_controller.grid
    grid_pixels = grid_object.grid

    # Snake(s)
    snakes_array = game_controller.snakes
    snake_object1 = snakes_array[0]

#### Using Multiple Snakes
Snakes can be distinguished by the Green value of their `head_color` attribute. Each head color consists of [Red=255, Green=uniqueNonZeroValue, Blue=0]. For each snake instantiated, the head color will corespond to its index within the controller's snake array. The head value will take on [255, (i+1)*10, 0] where i is the index of the snake.

When using multiple snakes, at each step, you pass an array of actions corresponding to the action of each snake. The return is an array of rewards corresponding each snake. The reward returned upon a snakes' death is -1, each subsequent step after this, however, is a reward of 0. The contents of the action array are ignored at a dead snake's index, the action array must, however, continue to have an index for each snake that originally started out the game.

#### Coordinates
The units of the game are made to take up multiple pixels within the grid. Each unit has an x,y coordinate associated with it where (0,0) represents the uppermost left unit of the grid and (`grid_object.grid_size[0]`, `grid_object.grid_size[1]`) denotes the lowermost right unit of the grid. Positional information about snake food and snakes' bodies is encoded using this coordinate system.

#### Snake Class
This class holds all pertinent information about an individual snake. Useful information includes:

    # Action constants denote the action space.
    snake_object1.UP # Equal to integer 0
    snake_object1.RIGHT # Equal to integer 1
    snake_object1.DOWN # Equal to integer 2
    snake_object1.LEFT # Equal to integer 3

    # Member Variables
    snake_object1.direction # Indicates which direction the snake's head is pointing; initially points DOWN
    snake_object1.head # x,y Coordinate of the snake's head
    snake_object1.head_color # A pixel ([R,G,B]) of type uint8 with an R value of 255
    snake_object1.body # deque containing the coordinates of the snake's body ordered from tail to neck [furthest from head, ..., closest to head]

#### Grid Class
This class holds all pertinent information about the grid that the snakes move on. Useful information includes:

    # Color constants give information about the colors of the grid
    # Each are ndarrays with dtype uint8
    grid_object.BODY_COLOR # [1,0,0] Color of snake body units
    grid_object.HEAD_COLOR # [255, (i+1)*10, 0] Color of snake head units. i is the index of the snake.
    grid_object.FOOD_COLOR # [0,0,255] Color of food units
    grid_object.SPACE_COLOR # [0,255,0] Color of blank space

    # Member Variables
    grid_object.unit_size # See Game Options
    grid_object.unit_gap # See Game Options
    grid_object.grid_size # See Game Options
    grid_object.grid # Numpy [R,G,B] pixel array of game

#### Controller Class
The Controller holds a grid object and an array of snakes that move on the grid. The Controller class handles the game logic between the snakes and the grid. Actions are taken through this class and initialization parameters within this class dictate the initial parameters of the grid and snake objects in the game. Useful information includes:

    # Member variables
    game_controller.grid # An instance of the grid class for the game
    self.snakes # An array of snake objects that are on the board. If a snake dies, it is erased and it becomes None.
