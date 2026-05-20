# 🩺 IoT Real-Time Health Monitor

> Real-time patient vitals tracking with ML anomaly detection and instant SMS alerts.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-HiveMQ-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![Twilio](https://img.shields.io/badge/Twilio-SMS_Alerts-F22F46?style=for-the-badge&logo=twilio&logoColor=white)
![ML](https://img.shields.io/badge/ML-Isolation_Forest-FF6B35?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 🔍 What It Does

Monitors patient health vitals in real-time using IoT sensors, detects anomalies using machine learning, and sends instant SMS alerts — no manual thresholds required.

---

## ⚙️ Architecture

```
IoT Sensors → MQTT Broker (HiveMQ) → Data Ingestion → Isolation Forest (ML)
                                                              ↓
                                              Normal → Live Dashboard
                                              Anomaly → Twilio SMS Alert
```

---

## 📊 Vitals Monitored

| Metric | Normal Range | Alert Trigger |
|--------|-------------|---------------|
| Heart Rate | 60–100 bpm | Outside range |
| Body Temperature | 36.0–38.5 °C | Outside range |
| Oxygen Level (SpO2) | 95–100% | Below threshold |

---

## 🤖 ML Anomaly Detection

Uses **Isolation Forest** (unsupervised learning) to detect abnormal vitals patterns:

- No manual threshold configuration needed
- Trained on baseline vitals data
- Flags anomalies in real-time
- Triggers automated Twilio SMS alert on detection

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.8+ |
| IoT Protocol | MQTT (paho-mqtt) |
| Message Broker | HiveMQ (public broker) |
| ML Model | Isolation Forest (scikit-learn) |
| Alerts | Twilio SMS API |
| Visualization | Matplotlib (real-time plots) |
| IDE | PyCharm |

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/SOMNATH43910/Python-Project_Summer-.git
cd Python-Project_Summer-
```

### 2. Install dependencies
```bash
pip install paho-mqtt scikit-learn twilio matplotlib numpy
```

### 3. Set environment variables
```bash
export TWILIO_ACCOUNT_SID=your_account_sid
export TWILIO_AUTH_TOKEN=your_auth_token
export TWILIO_PHONE=your_twilio_number
export DESTINATION_PHONE=your_phone_number
```

### 4. Run the system
```bash
python main.py
```

Choose from the menu:
- `1` → Simulate IoT sensor data
- `2` → Start data ingestion + live dashboard
- `3` → Exit

---

## 📁 Project Structure

```
📦 IoT-Health-Monitor
 ┣ 📄 main.py              — Entry point & menu
 ┣ 📄 simulate_iot_data.py — IoT sensor data simulator
 ┣ 📄 data_ingestion.py    — MQTT subscriber + live plots
 ┣ 📄 dashboard.py         — Console dashboard
 ┗ 📄 anomaly_detection.py — Isolation Forest + Twilio alerts
```

---

## 🔐 Security Note

Never hardcode API credentials. Always use environment variables:

```python
import os
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')
```

---

## 👨‍💻 Built By

**Somnath** — Java Backend Developer @ Wipro  
[LinkedIn](https://www.linkedin.com/in/somnath7/) · [GitHub](https://github.com/SOMNATH43910)

---

> Built as part of Engineering Internship — LPU | Jun–Aug 2024
