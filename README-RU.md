# Tomarket

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/Tomarket_ai_bot/app?startapp=0000yBC8)

[![Static Badge](https://img.shields.io/badge/My_Telegram_Сhannel-@CryptoCats__tg-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CryptoCats_tg)

## Рекомендация перед использованием

# 🔥🔥 Используйте PYTHON 3.10 🔥🔥

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Функционал  
|                               Функционал                               | Поддерживается |
|:----------------------------------------------------------------------:|:--------------:|
|                            Многопоточность                             |       ✅        |
|                        Привязка прокси к сессии                        |       ✅        |
|                   Авто Реферальство ваших аккаунтов (75% успеха)       |       ✅        |
|                      Автоматическое выполнение задач                   |       ✅        |
|                      Поддержка pyrogram .session                       |       ✅        |
|                             Авто фарминг                               |       ✅        |
|                   Автоматическое выполнение квестов                    |       ✅        |
|                      Авто Ежедневная Награда                           |       ✅        |
|                       Авто Получение Звезд                             |       ✅        |
|                       Авто Получение Комбо                             |       ✅        |
|                    Авто игра mystery box (Spin)                        |       ✅        |
|                        Авто повышение уровня                           |       ✅        |

## [Настройки](https://github.com/CatSnowdrop/Tomarket/blob/main/.env-example/)
|           Настройка           |                                       Описание                                        |
|:-----------------------------:|:-------------------------------------------------------------------------------------:|
|         **API_ID**            |        Ваш Telegram API ID (целое число)                                              |
|         **API_HASH**          |        Ваш Telegram API Hash (строка)                                                 |
|         **REF_ID**            |        Ваш реферальный ID после startapp=                                             |
|      **FAKE_USERAGENT**       |        Использовать поддельный user agent для сессий (True / False)                   |
|      **AUTO_PLAY_GAME**       |        Автоматически играть в игры (True / False)                                     |
|      **AUTO_PLAY_SPIN**       |        Автоматически играть в Mystery Box (True / False)                              |
|     **AUTO_UPGRADE_RANK**     |        Автоматически повышать ранг (True / False)                                     |
|         **AUTO_TASK**         |        Автоматически выполнять задания (True / False)                                 |
|  **AUTO_GET_STASHED_TOMATO**  |        Автоматически получать ежедневную награду Mystery Box (True / False)           |
|    **AUTO_DAILY_REWARD**      |        Автоматически получать ежедневные награды (True / False)                       |
|    **AUTO_CLAIM_STARS**       |        Автоматически получать звездные награды (True / False)                         |
|     **AUTO_CLAIM_COMBO**      |        Автоматически получать комбо-награды (True / False)                            |
| **USE_RANDOM_DELAY_IN_RUN**   |        Использовать случайную задержку при запуске (True / False)                     |
|   **RANDOM_DELAY_IN_RUN**     |        Случайная задержка при запуске (например, [0, 15])                             |
|  **USE_PROXY_FROM_FILE**      |        Использовать прокси из файла `bot/config/proxies.txt` (True / False)           |

## Быстрый старт 📚
Windows: Для быстрой установки и последующего запуска - запустите файл run.bat

Linux: Для быстрой установки и последующего запуска - запустите файл run.sh

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт my.telegram.org и войдите в систему, используя свой номер телефона.
2. Выберите "API development tools" и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/CatSnowdrop/Tomarket) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/CatSnowdrop/Tomarket.git
cd Tomarket
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```


# Linux ручная установка
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/Tomarket >>> python3 main.py --action (1/2)
# Or
~/Tomarket >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```

# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/Tomarket >>> python main.py --action (1/2)
# Or
~/Tomarket >>> python main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```