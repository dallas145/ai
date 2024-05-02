import gymnasium as gym
from myaction import myaction

env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset(seed=42)
steps = 0
for _ in range(700):
   env.render()
   # action = env.action_space.sample()  # this is where you would insert your policy
   action = myaction(observation)
   observation, reward, terminated, truncated, info = env.step(action)
   # print('observation=', observation)
   if terminated or truncated:
      observation, info = env.reset()
      # print('done')
      print(f'die after {steps} steps.')
      steps = 0
   else:
      steps += 1
env.close()