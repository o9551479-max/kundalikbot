import os
import requests

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send("1️⃣ Bot ishga tushdi")
send("2️⃣ Kundalik tekshirildi")
send("3️⃣ Bot ishini yakunladi ✅")
