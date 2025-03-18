from stable_baselines3 import DQN
from env import AvoidanceEnv

model = DQN.load("avoidance_ai")
env = AvoidanceEnv()
obs = env.reset()

print("🎮 AI đang chơi game...")

for _ in range(1000):
    env.render()
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    if done:
        obs = env.reset()
env.close()
