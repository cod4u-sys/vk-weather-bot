import os
from dotenv import load_dotenv

from vkbottle import Bot
from handlers import initialization

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)

initialization(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    bot.run_forever()
