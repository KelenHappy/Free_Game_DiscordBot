### [The steps to set up Firebase](https://ithelp.ithome.com.tw/articles/10335720)  
### [Where can I find the Discord channel ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)  
## Install(Local Deployment)  
### bash (using wsl)
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
