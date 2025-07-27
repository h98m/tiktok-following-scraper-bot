# 📲 TikTok Following Scraper Bot (Telegram Bot)

A Telegram bot that extracts the **list of accounts followed by any public TikTok user**.  
It uses **unofficial TikTok web and mobile API endpoints** to collect the data and sends the result as a `.txt` file via Telegram.

---

## 🚀 Features

- 🔍 Accepts TikTok usernames (without `@`)
- 📦 Scrapes the list of accounts they follow
- 💬 Sends live progress updates during the process
- 📄 Exports results to a `.txt` file
- 🧹 Automatically deletes the file after sending

---

## ⚙️ How It Works

1. User sends `/start` to the bot on Telegram
2. Bot asks for a TikTok username
3. It fetches the `user_id` and `secUid` using a request to the profile page
4. It uses TikTok’s internal API to fetch the following list
5. It creates a `.txt` file with the usernames
6. The file is sent back to the user via Telegram and then deleted

---

## 🧪 Example Interaction

```plaintext
👤 User: /start
🤖 Bot: Please send the TikTok username (without @)
👤 User: tiktok_user123
🤖 Bot: Extracting followings for @tiktok_user123...
📦 Collected 50 followings so far...
📄 Sending file: 123456789_followings.txt
```

---

## 🛠 Requirements

- Python 3.7 or higher

### 🧰 Required Python Libraries

Install them using:

```bash
pip install pyTelegramBotAPI==4.15.4 requests==2.31.0
```

These are used for:
- `pyTelegramBotAPI` → Telegram bot framework
- `requests` → Handling HTTP requests to TikTok

Alternatively, you can install them from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 📂 File Structure

```
tiktok-following-scraper-bot/
├── bot.py                # Main bot script
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## 🛠 Configuration

1. Get a bot token from [@BotFather](https://t.me/BotFather)
2. Open `bot.py` and replace:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

---

## 🔐 Disclaimer

> This tool is for **educational and personal use only**.  
> Scraping TikTok data may violate their [Terms of Service](https://www.tiktok.com/legal/terms-of-service).  
> Use responsibly and at your own risk.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact

Questions, suggestions, or contributions are welcome via GitHub Issues.

---

**Made with ❤️ by [h98m](https://github.com/h98m)**
