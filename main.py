# insta-bot/main.py
from flask import Flask, render_template
from app.scheduler import start_scheduler
import os

app = Flask(__name__, template_folder="../web")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    start_scheduler()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

# ---
# app/__init__.py
# (Empty or basic init file)



#
#
#
# Save session cookies
cl.dump_settings("session_cookies.json")

# Reuse session cookies
cl.load_settings("session_cookies.json")
