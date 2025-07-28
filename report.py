import json

with open('logs/user_clicks.json', 'r') as f:
    data = json.load(f)

print(f"🔍 Total users who clicked: {len(data)}")
emails = [entry['email'] for entry in data]
print("📧 Emails captured:")
for email in emails:
    print(f" - {email}")
