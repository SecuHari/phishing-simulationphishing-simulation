from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime
from phishing_detector import is_phishing

app = Flask(__name__)

log_file = 'logs/user_clicks.json'
if not os.path.exists('logs'):
    os.makedirs('logs')

@app.route('/')
def home():
    return render_template('phishing_page.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    log_user_click(email)
    return "<h3>Thanks. Your account is now verified. (Simulation)</h3>"

def log_user_click(email):
    entry = {
        'email': email,
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data.append(entry)
        with open(log_file, 'w') as f:
            json.dump(data, f, indent=2)

    except Exception as e:
        print(f"Logging Error: {e}")

@app.route('/check_url')
def check_example_url():
    test_url = "http://192.168.0.50/login"
    is_suspicious = is_phishing(test_url)
    return f"Phishing Detected: {is_suspicious}"

if __name__ == '__main__':
    app.run(debug=True)
