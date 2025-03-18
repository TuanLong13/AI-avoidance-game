import pandas as pd
from dowhy import CausalModel
from stable_baselines3 import DQN
from env import AvoidanceEnv

data = []
model = DQN.load("avoidance_ai")
env = AvoidanceEnv()
obs = env.reset()

print("📊 Thu thập dữ liệu AI chơi game...")

for _ in range(1000):
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    data.append({
        "player_y": obs[1],
        "obstacle_y": obs[3],
        "action": action,
        "reward": reward,  # Thêm phần thưởng vào dữ liệu
        "collision": 1 if done else 0  # Xác định va chạm
    })
    if done:
        obs = env.reset()

df = pd.DataFrame(data)
print("🔍 Phân tích AI với DoWhy...")

model = CausalModel(
    data=df,
    treatment="action",
    outcome="collision",
    common_causes=["player_y", "reward"],  # Đảm bảo có biến gây nhiễu
    graph="""
        digraph {
            action -> collision;
            obstacle_y -> collision;
            player_y -> action;
            player_y -> collision;
            reward -> action;
        }
    """

)
df["action"] = df["action"].astype(float)  # Ép kiểu về số thực (nếu cần)
identified_estimand = model.identify_effect()

print(f"🚀 AI đã chơi xong! Số lần va chạm: {df['collision'].sum()} / {len(df)}")
estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")
print(f"📌 Tác động của hành động AI đến va chạm: {estimate.value}")
print(estimate)