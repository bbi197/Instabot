 README.md

Auotofollow use at your own risk
# InstaBot MVP (Stealth Mode - Ubuntu + Ngrok)

## 📦 Features
- Random follow/unfollow of Instagram users at human-like intervals
- Stealth session handling via cookies (persistent login)
- Randomized delays and headers to mimic human behavior
- Flask web dashboard for monitoring (optional)
- Can be exposed via Ngrok for demo/testing remotely

## 🧠 Disclaimer (Learning Use Only)
This tool is for **educational purposes** only and must **never** be used on a real Instagram account. Use only on dummy/test accounts in isolated environments (e.g., VMs). The author is not responsible for any misuse or violations.

---

## 🔧 Installation (Ubuntu)
```bash
sudo apt update && sudo apt install python3 python3-pip git
pip3 install -r requirements.txt
```

### 📁 Required Folder Structure
```
instabot-mvp/
├── app/
│   ├── __init__.py
│   ├── bot.py
│   └── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔐 Set Environment Variables (Add to ~/.bashrc)
```bash
echo 'export IG_USERNAME="your_dummy_username"' >> ~/.bashrc
echo 'export IG_PASSWORD="your_dummy_password"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🚀 Running the Bot
```bash
python3 main.py
```
This launches the follow/unfollow logic and web dashboard.

---

## 🌍 Optional: Ngrok Setup for External Access
```bash
ngrok http 5000
```
Ngrok will give you a public HTTPS URL to share your local dashboard remotely.

---

## 🧪 Testing & Limits
- Follow/unfollow rate limited to every **30–90 minutes**.
- Each session mimics real behavior with cookies and randomized user-agent headers.
- Automatically persists session in `session_cookies.json`.

---

## 🛡️ Best Practices
- Never exceed Instagram's action limits.
- Only use on test accounts — not production.
- Always run inside isolated sandbox (VM or container).

---

## 📜 License
MIT License (for educational/demonstration use only)


