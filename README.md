# dcbot

一個使用 Python 製作的 Discord Bot 專案。

此機器人可用於 Discord 伺服器，提供指令互動、自動化功能，並可依需求持續擴充。

## 📌 Features

- Discord Bot 基本指令
- 自動回應訊息
- 可擴充模組化設計
- 使用 Discord API 進行互動

（實際功能請依目前程式碼內容調整）

## 🛠 Requirements

- Python 3.8+
- Discord Bot Token
- 以下 Python 套件（請參考 `requirements.txt`）

## 📥 Installation

### 1️⃣ Clone 專案

```bash
git clone https://github.com/YiJhu/dcbot.git
cd dcbot
```

### 2️⃣ 建立虛擬環境（建議）
```bash
python -m venv venv
```

## 啟用虛擬環境：

- Windows
```bash
venv\Scripts\activate
```

- macOS / Linux
```bash
source venv/bin/activate
```

### 3️⃣ 安裝套件
pip install -r requirements.txt

### 4️⃣ 設定 Bot Token

在專案根目錄建立 .env 檔案，內容如下：
```env
DISCORD_TOKEN=你的DiscordBotToken
```

⚠️ **請勿將 .env 上傳至 GitHub**

### 5️⃣ 啟動 Bot

```bash
python bot.py
```

### 🤝 Contributing

歡迎提交 Issue 或 Pull Request！

Fork 本專案

建立新分支

提交修改

發送 Pull Request

### 📜 License

本專案採用 **MIT License**
詳情請見 [LICENSE]("https://github.com/YiJhu/dcbot/blob/master/LICENSE.md")

### 🙏 Acknowledgements

- [Discord.py]("https://github.com/Rapptz/discord.py")
- [discord-py-slash-command]("https://github.com/interactions-py/interactions.py")
