from vkbottle import Bot
from vkbottle.bot import Message
from handlers.weather import Weather_Actions
from action_with_db.service import UserServices
def initialization(bot: Bot):
    @bot.on.message(text=["/weather", "Узнать погоду ☀"])
    async def get_weather_for_user(message: Message):
        user_id = message.from_id
        user = UserServices.get_user_by_id(user_id)
        if not user:
            await message.answer("Сначала нужно зарегистрироваться")
            return
        
        weather = Weather_Actions.get_weather(user.latitude, user.longitude)
        if not weather:
            await message.answer("❌Не удалось получить погоду. Сервис временно недоступен. Попробуйте позже")
            return
        
        temperature = weather["current_weather"]["temperature"]
        wind = weather["current_weather"]["windspeed"]
        weathercode = weather["current_weather"]["weathercode"]
        is_day = weather["current_weather"]["is_day"]

        emoji = Weather_Actions.get_weather_emoji(weathercode, is_day)

        await message.answer(
            f"Привет, {user.username}! {emoji}\n"
            f"{user.city_name}: {temperature:.0f}°C\n"
            f"💨 Ветер {wind:.1f} км/ч\n"
            "\n"
            "Хорошего дня!"
        )
