# example.py - Watch for new emails on a temp mailbox
# by Fortmaly :)

import time
import json
import forgemail

# Helper to clean HTML junk like &nbsp; and <br>
def clean_text(html_text):
    if not html_text:
        return ""
    text = html_text.replace("<br>", "\n").replace("<br/>", "\n")
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    # remove any leftover HTML tags (simple way)
    while "<" in text and ">" in text:
        start = text.find("<")
        end = text.find(">", start)
        if end != -1:
            text = text[:start] + text[end+1:]
        else:
            break
    return text.strip()

print("=== Temp Mail by Fortmaly ===\n")

# 1. Create a new email
token, email = forgemail.create_email()
if not token:
    print("Oops, couldn't make an email. Check internet?")
    exit()

print(f"Your temp email: {email}")
print("Waiting for messages... Press Ctrl+C to stop.\n")

seen = set()
try:
    while True:
        data = forgemail.get_messages(token)
        if data is None:
            break

        # The API sometimes gives a list, sometimes a dict with "messages"
        if isinstance(data, list):
            msgs = data
        elif isinstance(data, dict) and "messages" in data:
            msgs = data["messages"]
        else:
            msgs = []

        for msg in msgs:
            msg_id = msg.get("_id") or msg.get("id")
            if msg_id and msg_id not in seen:
                seen.add(msg_id)
                print("\n" + "="*50)
                print("NEW EMAIL!")
                print(f"From: {msg.get('from', '?')}")
                print(f"Subject: {msg.get('subject', '?')}")
                # clean the body preview
                body = msg.get("bodyPreview") or msg.get("body") or ""
                print("Message:")
                print(clean_text(body))
                print("\nFull JSON (just in case):")
                print(json.dumps(msg, indent=2))
                print("="*50)

        time.sleep(10)
except KeyboardInterrupt:
    print("\nBye!")