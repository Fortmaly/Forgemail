===========================
    forgemail.py - v1.0
    made by Fortmaly
===========================

What is this?
-------------
A tiny library + example script to get a temporary email from temp-mail.org.
You can use it in your own Python projects or just run the example to watch for emails.

Files in this package:
- forgemail.py : the library (two functions)
- example.py   : a ready‑to‑run script that polls for new emails
- README.txt   : this file

How to use the library
----------------------
1. Put forgemail.py in the same folder as your script.
2. Import it:

   import forgemail

3. Create a new email:

   token, email = forgemail.create_email()
   # token: keep this secret, it's like a password
   # email: your temporary address (e.g. lagomix431@gixpos.com)

4. Fetch messages anytime:

   messages = forgemail.get_messages(token)
   # messages is the full JSON response (list or dict)

That's it. No extra dependencies except 'requests' – install it with:
   pip install requests

Running the example
-------------------
Just type:
   python example.py

It will create a new temp email and start polling every 10 seconds.
Press Ctrl+C to stop.

What does the output look like?
-------------------------------
When an email arrives, you will see:
- Sender and subject
- The message text with &nbsp; and <br> cleaned up
- The full raw JSON (so you see everything)

Example output:

   NEW EMAIL!
   From: Anonymousemail <noreply@anonymousemail.se>
   Subject: Hi
   Message:
   Powered by Anonymousemail Test 3256

   Full JSON:
   { "_id": "...", "from": "...", ...}

Troubleshooting
---------------
- If you get "Token expired", just run the script again – it makes a new email.
- If you get a 429 error (rate limit), wait a few seconds and try again.

Have fun! I made this for my own projects, hope it helps you too.
- Fortmaly