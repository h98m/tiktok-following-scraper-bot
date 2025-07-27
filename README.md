# 📲 TikTok Following Scraper Bot (Telegram Bot)

This is a Telegram bot that extracts the list of **accounts followed by a specific TikTok user**, and sends them back to the user as a `.txt` file.  
It uses **unofficial TikTok endpoints** and Python to automate the process.

---

## 🚀 Features

- Accepts TikTok usernames from Telegram users
- Scrapes the list of followings using TikTok’s web and mobile API
- Sends updates while scraping (every 10 accounts)
- Exports the results in a `.txt` file
- Deletes the file after sending
- Handles errors and invalid usernames

---

## ⚙️ How It Works

1. User sends `/start` to the bot on Telegram
2. Bot asks for a TikTok username (without @)
3. Bot fetches the user ID and `secUid` from the profile page
4. Using a mobile API endpoint, it extracts the full list of **followings**
5. The list is saved into a file and sent back to the user via Telegram
6. Temporary file is deleted afterward

---

## 🧪 Example Bot Interaction

