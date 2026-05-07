# forgemail.py - A simple temp email library I made for myself
# by Fortmaly

import requests
import time

def create_email():
    """Makes a new temp email. Returns (token, email) or (None, None) if it fails."""
    url = "https://web2.temp-mail.org/mailbox"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Origin": "https://temp-mail.org"
    }
    try:
        r = requests.post(url, headers=headers, json={}, timeout=20)
        if r.status_code == 200:
            data = r.json()
            return data.get("token"), data.get("mailbox")
        else:
            print("Error:", r.status_code)
            return None, None
    except Exception as e:
        print("Failed:", e)
        return None, None

def get_messages(token):
    """Gets all messages for the given token. Returns the full API response."""
    url = "https://web2.temp-mail.org/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.json()
        elif r.status_code in (401, 403):
            print("Token expired or bad")
            return None
        else:
            print("Strange status:", r.status_code)
            return []
    except Exception as e:
        print("Error fetching:", e)
        return []