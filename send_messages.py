import requests
import os
from datetime import datetime
import pytz

# Load webhook URL from environment variables
WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1322319995908132975/1zfXSl69FniZHyhj5MNyR0T4_49mfdjFLpnBb4Ek8d7daoHjC2bH-KxM49Iy2rb-aR0B")

def send_message(message):
    if not WEBHOOK_URL:
        print("Webhook URL is not set!")
        return
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"Message sent: {message}")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")

# Define timezone
est = pytz.timezone("US/Eastern")
now = datetime.now(est)

# Decide which message to send based on the time
if now.hour == 8:  # 8:00 AM EST
    send_message("Good Morning! ☀️")
elif now.hour == 22:  # 10:00 PM EST
    send_message("Good Night! 🌙")
else:
    print("No message to send at this time.")
