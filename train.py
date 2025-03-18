from stable_baselines3 import DQN
from env import AvoidanceEnv

env = AvoidanceEnv()

model = DQN("MlpPolicy", env, verbose=1)

print("🚀 Bắt đầu huấn luyện AI...")
model.learn(total_timesteps=10000)
print("✅ Huấn luyện xong!")

model.save("avoidance_ai")
print("💾 AI đã được lưu!")
