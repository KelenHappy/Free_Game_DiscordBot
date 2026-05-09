[English](#Free_Game_DiscordBot) | [中文](#Discord免費遊戲機器人)  
# Free_Game_DiscordBot   
## Before Start  
### [Create Discord Bot](https://discord.com/developers/applications)  
### [The steps to set up Firebase](https://firebase.google.com/docs/admin/setup?hl=zh&authuser=0)  
### [Where can I find the Discord channel ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)  
### You need to read main.go and geturl.go first, and then modify the code inside them.   
## Install(Local Deployment)  

```sh
git clone https://github.com/KelenHappy/Free_Game_DiscordBot.git
```

```sh
cd Free_Game_DiscordBot 
```

```sh
go run .
```

## Modification

  1. Copy `.env.example` to `.env` and fill in your BOT_TOKEN.
  2. Go to Firebase Project Settings -> Service Accounts -> **Go** -> Generate New Private Key.
  3. Rename the JSON file to serviceAccountKey.json.


These instructions guide you through the process of setting up a Discord bot locally, including steps for Discord and Firebase setup, as well as the installation of necessary Go packages. The final section provides commands to start the bot with the specified token.  

---------------------------------------------------------------------
# Discord免費遊戲機器人  
## 開始之前  
### [創建DiscordBot](https://discord.com/developers/applications)  
### [設置 Firebase 的步驟](https://firebase.google.com/docs/admin/setup?hl=zh&authuser=0)  
### [如何找到 Discord 頻道 ID？](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
### 你必須先閱讀 main.go 和 geturl.go，然後修改裡面的程式碼。  

## 安裝（本地部署）

```sh
git clone https://github.com/KelenHappy/Free_Game_DiscordBot.git
```

```sh
cd Free_Game_DiscordBot 
```

```sh
go run .
```

## 修改
  1. 複製 `.env.example` 為 `.env`，填入你的 BOT_TOKEN
  2. Firebase 專案設定 -> 服務帳戶 -> **Go** -> 產生新的密鑰
  3. 重新命名 JSON 檔案，改成 serviceAccountKey.json  


這些說明將引導您完成本地設置 Discord 機器人的過程，包括 Discord 和 Firebase 的設置步驟，以及在虛擬環境中安裝所需的 Go 套件。最後一節提供了用指定令牌啟動機器人的命令。  
