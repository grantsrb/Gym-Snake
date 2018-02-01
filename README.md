# gym-snake

#### Created in response to OpenAI's [Requests for Research 2.0](https://blog.openai.com/requests-for-research-2/)

## Description
gym-snake is a multi-agent implementation of the classic game [snake](https://www.youtube.com/watch?v=wDbTP0B94AM) that is made as an OpenAI gym environment.

Currently only a single file is available.

## Dependencies
- pip
- gym
- numpy
- matplotlib

## Installation
1. Clone this repository
2. Navigate to the cloned repository
3. Run command `$ pip install -e ./`

## SnakeEnv and SnakeExtraHardEnv
The snake environment has variable sizing, variable numbers of players, and variable quantities of food units on the map. The difference between SnakeEnv and SnakeExtraHardEnv are the default parameters. The potential parameters that can be passed to the SnakeEnv or SnakeExtraHardEnv initializers are as follows:

grid_size - tuple or list denoting (width units, height units) of grid for game to take place
unit_size - integer denoting number of pixels per unit on board
snake_size - initial number of units in snake's body
n_snakes - number of snakes on the grid
n_foods - number of foods on the grid at any given time
