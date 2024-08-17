[English](#the-steps-to-set-up-firebase) | [中文](#設置-Firebase-的步驟)
### [The steps to set up Firebase](https://ithelp.ithome.com.tw/articles/10335720)  
### [Where can I find the Discord channel ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)  
## Install(Local Deployment)  
### bash (using WSL)
```sh
cd path/to/your/project 
```

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

### Virtual Environment
```sh
pip install firebase  
```
```sh
pip install asyncio
```

```sh
pip install Flask  
```

```sh
pip install py-cord  
```

```sh
pip install requests  
```

```sh
pip install discord2  
```
## Start  
```sh
export BOT_TOKEN=YOURTOKEN  
```
```sh
python3 main.py  
```

These instructions guide you through the process of setting up a Discord bot locally, including steps for Discord and Firebase setup, as well as the installation of necessary Python packages within a virtual environment. The final section provides commands to start the bot with the specified token.  

### [設置 Firebase 的步驟](https://ithelp.ithome.com.tw/articles/10335720)  
### [如何找到 Discord 頻道 ID？](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

## 安裝（本地部署）

### bash（使用 WSL）
```sh
cd path/to/your/project 
```

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```
### 虛擬環境(venv內)
```sh
pip install firebase  
```
```sh
pip install asyncio
```

```sh
pip install Flask  
```

```sh
pip install py-cord  
```

```sh
pip install requests  
```

```sh
pip install discord2  
```
## 開始執行
```sh
export BOT_TOKEN=YOURTOKEN  
```
```sh
python3 main.py  
```

這些說明將引導您完成本地設置 Discord 機器人的過程，包括 Discord 和 Firebase 的設置步驟，以及在虛擬環境中安裝所需的 Python 套件。最後一節提供了用指定令牌啟動機器人的命令。  
