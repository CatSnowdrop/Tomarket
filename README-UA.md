# Tomarket

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/Tomarket_ai_bot/app?startapp=0000yBC8)

[![Static Badge](https://img.shields.io/badge/My_Telegram_Сhannel-@CryptoCats__tg-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CryptoCats_tg)

## Рекомендація перед використанням

# 🔥🔥 Використовуйте PYTHON 3.10 🔥🔥

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Функціонал  
|                               Функціонал                               | Підтримується |
|:----------------------------------------------------------------------:|:--------------:|
|                            Багатопоточність                            |       ✅        |
|                        Прив'язка проксі до сесії                       |       ✅        |
|                   Авто Реферальство ваших акаунтів (75% успіху)        |       ✅        |
|                      Автоматичне виконання завдань                     |       ✅        |
|                      Підтримка pyrogram .session                       |       ✅        |
|                             Авто фармінг                               |       ✅        |
|                   Автоматичне виконання квестів                        |       ✅        |
|                      Авто Щоденна Нагорода                             |       ✅        |
|                       Авто Отримання Зірок                             |       ✅        |
|                       Авто Отримання Комбо                             |       ✅        |
|                    Авто гра mystery box (Spin)                         |       ✅        |
|                        Авто підвищення рівня                           |       ✅        |

## [Налаштування](https://github.com/CatSnowdrop/Tomarket/blob/main/.env-example/)
|           Налаштування        |                                       Опис                                            |
|:-----------------------------:|:-------------------------------------------------------------------------------------:|
|         **API_ID**            |        Ваш Telegram API ID (ціле число)                                               |
|         **API_HASH**          |        Ваш Telegram API Hash (рядок)                                                  |
|         **REF_ID**            |        Ваш реферальний ID після startapp=                                             |
|      **FAKE_USERAGENT**       |        Використовувати підроблений user agent для сесій (True / False)                |
|      **AUTO_PLAY_GAME**       |        Автоматично грати в ігри (True / False)                                        |
|      **AUTO_PLAY_SPIN**       |        Автоматично грати в Mystery Box (True / False)                                 |
|     **AUTO_UPGRADE_RANK**     |        Автоматично підвищувати ранг (True / False)                                    |
|         **AUTO_TASK**         |        Автоматично виконувати завдання (True / False)                                 |
|  **AUTO_GET_STASHED_TOMATO**  |        Автоматично отримувати щоденну нагороду Mystery Box (True / False)             |
|    **AUTO_DAILY_REWARD**      |        Автоматично отримувати щоденні нагороди (True / False)                         |
|    **AUTO_CLAIM_STARS**       |        Автоматично отримувати зіркові нагороди (True / False)                         |
|     **AUTO_CLAIM_COMBO**      |        Автоматично отримувати комбо-нагороди (True / False)                           |
| **USE_RANDOM_DELAY_IN_RUN**   |        Використовувати випадкову затримку при запуску (True / False)                  |
|   **RANDOM_DELAY_IN_RUN**     |        Випадкова затримка під час запуску (наприклад, [0, 15])                        |
|  **USE_PROXY_FROM_FILE**      |        Використовувати проксі з файлу `bot/config/proxies.txt` (True / False)         |

## Швидкий старт 📚
Windows: Для швидкого встановлення і подальшого запуску - запустіть файл run.bat

Linux: Для швидкого встановлення і подальшого запуску - запустіть файл run.sh

## Попередні умови
Перш ніж почати, переконайтеся, що у вас встановлено наступне:
- [Python](https://www.python.org/downloads/) **версії 3.10**

## Отримання API ключів
1. Перейдіть на сайт my.telegram.org і увійдіть у систему, використовуючи свій номер телефону.
2. Виберіть "API development tools" і заповніть форму для реєстрації нового додатка.
3. Запишіть `API_ID` та `API_HASH` у файлі `.env`, що надані після реєстрації вашого застосунку.

## Установка
Ви можете завантажити [**Репозиторій**](https://github.com/CatSnowdrop/Tomarket) клонуванням на вашу систему і встановленням необхідних залежностей:
```shell
git clone https://github.com/CatSnowdrop/Tomarket.git
cd Tomarket
```

Потім для автоматичного встановлення введіть:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```


# Linux ручне встановлення
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Тут ви обов'язково маєте вказати ваші API_ID і API_HASH, решта береться за замовчуванням
python3 main.py
```

Також для швидкого запуску ви можете використовувати аргументи, наприклад:
```shell
~/Tomarket >>> python3 main.py --action (1/2)
# Or
~/Tomarket >>> python3 main.py -a (1/2)

# 1 - Запускає клікер
# 2 - Створює сесію
```

# Windows ручне встановлення
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Вказуєте ваші API_ID і API_HASH, решта береться за замовчуванням
python main.py
```

Також для швидкого запуску ви можете використовувати аргументи, наприклад:
```shell
~/Tomarket >>> python main.py --action (1/2)
# Or
~/Tomarket >>> python main.py -a (1/2)

# 1 - Запускає клікер
# 2 - Створює сесію
```