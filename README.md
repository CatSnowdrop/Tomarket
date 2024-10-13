# Tomarket

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/Tomarket_ai_bot/app?startapp=0000yBC8)

[![Static Badge](https://img.shields.io/badge/My_Telegram_Сhannel-@CryptoCats__tg-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CryptoCats_tg)

## Recommendation before use

# 🔥🔥 Use PYTHON 3.10 🔥🔥

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Functionality  
|                            Functionality                               |    Supported   |
|:----------------------------------------------------------------------:|:--------------:|
|                            Multithreading                              |       ✅        |
|                        Proxy binding to session                        |       ✅        |
|            Auto Referral of your accounts (75% success rate)           |       ✅        |
|                     Automatic task completion                          |       ✅        |
|                     Support pyrogram .session                          |       ✅        |
|                            Auto farming                                |       ✅        |
|                           Auto questing                                |       ✅        |
|                         Auto Daily Reward                              |       ✅        |
|                        Auto Getting Stars                              |       ✅        |
|                          Auto Get Combo                                |       ✅        |
|                    Auto Mystery Box Game (Spin)                        |       ✅        |
|                          Auto Level Up                                 |       ✅        |

## [Settings](https://github.com/CatSnowdrop/Tomarket/blob/main/.env-example/)
|           Settings            |                                       Description                                     |
|:-----------------------------:|:-------------------------------------------------------------------------------------:|
|         **API_ID**            |        Your Telegram API ID (integer)                                                 |
|         **API_HASH**          |        Your Telegram API Hash (string)                                                |
|         **REF_ID**            |        Your referral ID after startapp=                                               |
|      **FAKE_USERAGENT**       |        Use a fake user agent for sessions (True / False)                              |
|      **AUTO_PLAY_GAME**       |        Automatically play games (True / False)                                        |
|      **AUTO_PLAY_SPIN**       |        Automatically play Mystery Box (True / False)                                  |
|     **AUTO_UPGRADE_RANK**     |        Automatically increase rank (True / False)                                     |
|         **AUTO_TASK**         |        Automatically perform tasks (True / False)                                     |
|  **AUTO_GET_STASHED_TOMATO**  |        Automatically receive the daily Mystery Box reward (True / False)              |
|    **AUTO_DAILY_REWARD**      |        Automatically receive daily rewards (True / False)                             |
|    **AUTO_CLAIM_STARS**       |        Automatically earn star rewards (True / False)                                 |
|     **AUTO_CLAIM_COMBO**      |        Automatically earn combo rewards (True / False)                                |
| **USE_RANDOM_DELAY_IN_RUN**   |        Use random startup delay (True / False)                                        |
|   **RANDOM_DELAY_IN_RUN**     |        Random startup delay (eg, [0, 15])                                             |
|  **USE_PROXY_FROM_FILE**      |        Use proxy from `bot/config/proxies.txt` (True / False)                         |

## Quick Start 📚
Windows: For quick installation and subsequent startup - run the run.bat file

Linux: For quick installation and subsequent startup - run the run.sh file

## Prerequisites
Before you start, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Getting API keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Write `API_ID` and `API_HASH` in the `.env` file provided after registering your application.

## Installation
You can download [**Repository**](https://github.com/CatSnowdrop/Tomarket) by cloning it onto your system and installing the necessary dependencies:
```shell
git clone https://github.com/CatSnowdrop/Tomarket.git
cd Tomarket
```

Then, for automatic installation, enter:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```


# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH , the rest is taken by default
python3 main.py
```

You can also use arguments for a quick startup, such as:
```shell
~/Tomarket >>> python3 main.py --action (1/2)
# Or
~/Tomarket >>> python3 main.py -a (1/2)

# 1 - Starts the clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for a quick startup, such as:
```shell
~/Tomarket >>> python main.py --action (1/2)
# Or
~/Tomarket >>> python main.py -a (1/2)

# 1 - Starts the clicker
# 2 - Creates a session
```