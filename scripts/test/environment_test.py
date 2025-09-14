import numpy as np
import gymnasium as gym

seed: int = 42

env: gym.Env = gym.make("CartPole-v1", render_mode="human")
episode_over = False
total_reward = 0.0

max_epochs = 500

for i in range(max_epochs):
    seed = np.random.randint(0, 10000)
    observation, info = env.reset(seed=seed)
    print(f"{observation}, {info}")

    while not episode_over:
        action = env.action_space.sample() # Sample action over action space
        print(type(action))
        print(action)

        observation, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        episode_over = terminated or truncated
    print(f"Episode over total reward: {total_reward}")
env.close()