import gym
from gym.envs.registration import register
from gym.scoreboard.registration import add_group
from gym.scoreboard.registration import add_taskcd 


register(
     id='SuperMarioBros-1-1-v0',
     entry_point='gym.envs.ppaquette_gym_super_mario:MetaSuperMarioBrosEnv',
)

add_group(
     id='ppaquette_gym_super_mario',
     name='ppaquette_gym_super_mario',
     description='super_mario'
)

add_task(
    id='SuperMarioBros-1-1-v0',
    group='ppaquette_gym_super_mario',
    summary="SuperMarioBros-1-1-v0"
)

env = gym.make('SuperMarioBros-1-1-v0')
env.reset()
for _ in range(10000):
    env.render()
    env.step(env.action_space.sample()) # take a random action