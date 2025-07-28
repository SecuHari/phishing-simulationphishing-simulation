#  Phishing Simulation System

A phishing simulation system built using Python and Flask to educate and train users to recognize and avoid phishing attacks. This project simulates phishing scenarios by serving fake login pages, logging user interactions, and detecting potentially malicious URLs.

---

## 🧠 Objective

The project aims to simulate phishing attacks in a controlled environment to:
- Train users to recognize phishing attempts
- Log user interactions for analysis
- Detect suspicious URLs using defined rules

---

## ⚙️ Technology Stack

- Python
- Flask
- BeautifulSoup
- Requests
- HTML/CSS
- JSON

---

## 🚀 Features

✅ Fake phishing login page  
✅ Email/password capture (educational only)  
✅ Logging into `user_clicks.json`  
✅ Phishing URL detection logic  
✅ Admin-side report generation  

---

## 📸 Screenshots

### 🖥️ 1. Home Page – Phishing Login Simulation  
![Screenshot 1](./1.png)

---

### 🧾 2. User Inputs Fake Credentials  
![Screenshot 2](./2.png)

---

### 📂 3. Logs Captured in `user_clicks.json`  
![Screenshot 3](./3.png)

---

### 🛡️ 4. Phishing Detection Module – URL Checking  
![Screenshot 4](./4.png)

---

### 📊 5. Report Display (from report.py)  
![Screenshot 5](./5.png)

---

## 🧪 How It Works

1. User opens the phishing page (`/`)
2. Enters fake email and password
3. Data is stored in a log file
4. Admin can check suspicious URLs and user data
5. Reports can be generated using Python scripts

---

---

## 📄 Installation

```bash
git clone https://github.com/yourusername/phishing-simulation.git
cd phishing-simulation
pip install flask requests beautifulsoup4
python app.py
Visit: http://127.0.0.1:5000


