from vkbottle import Bot
from vkbottle.bot import Message
from random import randint 
from datetime import datetime
def initialize(bot: Bot):
    @bot.on.message(text=["/cube", "Подбросить кубик 🎲"])
    async def roll_cube(message: Message):
        """Функция для подбрасывания кубика"""
        num = randint(1, 6)
        await message.answer(f"Выпала цифра {num}")
    @bot.on.message(text=["/time", "Узнать время ⌚"])
    async def get_time(message: Message):
        """Функция для получения нынешнего времени"""
        time = datetime.now().strftime("%H:%M:%S")
        await message.answer(f"Сейчас {time}")
    @bot.on.message(text=["/help", "Помощь ℹ️"])
    async def show_help(message: Message):
        try:
            with open("commands.txt", "r", encoding="utf-8") as f:
                help_text = f.read()
            await message.answer(help_text)
        except FileNotFoundError:
            await message.answer("❌ Файл с командами не найден")