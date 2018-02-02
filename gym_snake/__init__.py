from gym.envs.registration import register

register(
    id='snake-v0',
    entry_point='gym_snake.envs:SnakeEnv',
)
register(
    id='snake-plural-v0',
    entry_point='gym_snake.envs:SnakeExtraHardEnv',
)
