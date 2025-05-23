[English](#Free_Game_DiscordBot) | [中文](#Discord免費遊戲機器人)
# Free_Game_DiscordBot   
## Before Start  
### [Create Discord Bot](https://discord.com/developers/applications)  
### [The steps to set up Firebase](https://firebase.google.com/docs/admin/setup?hl=zh&authuser=0)  
### [Where can I find the Discord channel ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)  
### You need to read main.py and getUrl.py first, and then modify the code inside them.   
## Install(Local Deployment)  
### bash (using WSL or Linux)

```sh
git clone https://github.com/KelenHappy/Free_Game_DiscordBot.git
```

```sh
cd path/to/your/main.py 
```

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

### Virtual Environment
```sh
pip install -r requirements.txt
```

## Modification

  1. Modify the BOT_TOKEN in start.sh.
  2. Go to Firebase Project Settings -> Service Accounts -> Python -> Generate New Private Key.
  3. Rename the JSON file to serviceAccountKey.json.

## Start
```sh
./start.sh
```

These instructions guide you through the process of setting up a Discord bot locally, including steps for Discord and Firebase setup, as well as the installation of necessary Python packages within a virtual environment. The final section provides commands to start the bot with the specified token.  

---------------------------------------------------------------------
# Discord免費遊戲機器人  
## 開始之前  
### [創建DiscordBot](https://discord.com/developers/applications)  
### [設置 Firebase 的步驟](https://firebase.google.com/docs/admin/setup?hl=zh&authuser=0)  
### [如何找到 Discord 頻道 ID？](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
### 你必須先閱讀 main.py 和 getUrl.py，然後修改裡面的程式碼。  

## 安裝（本地部署）

### bash（使用 WSL 或 Linux）

```sh
git clone https://github.com/KelenHappy/Free_Game_DiscordBot.git
```

```sh
cd path/to/your/main.py 
```

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```
### 虛擬環境(venv內)
```sh
pip install -r requirements.txt 
```

## 修改
  1. 修改start.sh裡的BOT_TOKEN
  2. FireBase專案設定 -> 服務帳戶 -> Python -> 產生新的密鑰
  3. 重新命名json FIle，改成 serviceAccountKey.json  
## 開始執行
```sh
./start.sh
```

這些說明將引導您完成本地設置 Discord 機器人的過程，包括 Discord 和 Firebase 的設置步驟，以及在虛擬環境中安裝所需的 Python 套件。最後一節提供了用指定令牌啟動機器人的命令。  
