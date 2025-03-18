# 🏆 AI Avoidance Game - Reinforcement Learning + Causal Analysis

🚀 Đây là một trò chơi AI đơn giản sử dụng **Deep Q-Learning (DQN)** để huấn luyện AI né chướng ngại vật.  
🧐 Sau khi huấn luyện, AI được phân tích bằng **DoWhy** để xác định mối quan hệ nhân quả giữa hành động và kết quả.  

---

## 📌 1. Cài đặt môi trường  

Trước tiên, bạn cần cài đặt **Python** (>=3.8). Sau đó, cài đặt các thư viện cần thiết bằng lệnh sau:  

```bash
pip install -r requirements.txt
```

---

## 🎮 2. Cách chạy chương trình  

### 2.1. **Huấn luyện AI**  
Chạy script huấn luyện AI bằng DQN:  

```bash
python train.py
```

📌 **Kết quả mong đợi:**  
- AI sẽ học cách né chướng ngại vật qua 10.000 bước.  
- Sau khi huấn luyện xong, mô hình sẽ được lưu thành `avoidance_ai.zip`.  

---

### 2.2. **Chạy AI để kiểm tra**  
Sau khi AI đã được huấn luyện, chạy file `play.py` để xem AI hoạt động:  

```bash
python play.py
```

📌 **Kết quả mong đợi:**  
- AI sẽ tự động di chuyển để né chướng ngại vật.  
- Nếu AI va chạm, trò chơi sẽ tự động reset.  

---

### 2.3. **Phân tích AI bằng DoWhy**  
Sau khi AI đã chơi xong, phân tích dữ liệu để xem hành động của AI có thực sự giúp né tránh không:  

```bash
python analysis.py
```

📌 **Kết quả mong đợi:**  
- In ra số lần AI va chạm.  
- Hiển thị tác động của hành động AI lên số lần va chạm (`estimate.value`).  

---

