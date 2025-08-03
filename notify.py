
import requests

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

def send_discord_alert(message):
    payload = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)
