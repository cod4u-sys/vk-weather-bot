# VK Weather Bot

Бот для VK с прогнозом погоды.

## Запуск

1. `pip install -r requirements.txt`
2. Создать `.env` с `TOKEN=ваш_токен` и `DB_PATH=action_with_db/bot.db`
3. `python bot.py`

## Команды

`/start` — регистрация  
`/help` — список команд  
`/weather` — погода  
`/change_city` — сменить город  
`/change_username` — сменить имя  
`/show_profile` — профиль  
`/cube` — бросить кубик  
`/time` — текущее время

## Технологии

Python + vkbottle + SQLAlchemy + Open-Meteo API