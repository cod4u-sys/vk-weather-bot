from vkbottle import Bot
from vkbottle.bot import Message
from handlers.weather import Weather_Actions
from action_with_db.service import UserServices
from states.change_state import CityChangeState, NameChangeState
from keyboards.main_keyboard import keyboard
from keyboards.cancel_keyboard import keyboard as cancel
def initialization(bot: Bot):
    @bot.on.message(text=["/change_city", "Сменить город 🏙"])
    async def change_city(message: Message):
        user_id = message.from_id
        user = UserServices.get_user_by_id(user_id)
        if not user:
            await message.answer("Сначала нужно зарегистрироваться")
            return
        await bot.state_dispenser.set(message.peer_id, CityChangeState.WAIT_TITLE_OF_CITY)
        await message.answer("Напиши название города", keyboard=cancel)
    
    @bot.on.message(state=CityChangeState.WAIT_TITLE_OF_CITY)
    async def wait_city_name(message: Message):
        
        user_id = message.from_id
        city_name = message.text.strip().title()
        if city_name == "Отменить":
            await message.answer("Отмена смены города", keyboard=keyboard)
            await bot.state_dispenser.delete(message.peer_id)
            return
        if not city_name:
            await message.answer("Некорректный ввод, вы ничего не ввели")
            return
        if any(not (char.isalpha() or char.isspace() or char == '-') for char in city_name):
            await message.answer("❌ Название города может содержать только буквы, пробелы и дефис")
            return
        coords = Weather_Actions.get_coordinates(city_name)
        if not coords:
            await message.answer("Не могу найти такой город, попробуй ввести другой город")
            return
        official_city_name = coords["name"]
        await bot.state_dispenser.delete(message.peer_id)
        UserServices.change_cityname(user_id, official_city_name, coords["latitude"], coords["longitude"])
        await message.answer("Город успешно изменён!")
    @bot.on.message(text=["/show_profile", "Показать профиль 👤"])
    async def show_profile(message: Message):
        user_id = message.from_id
        user = UserServices.get_user_by_id(user_id)
        if not user:
            await message.answer("Вы не зарегистрированы❌", keyboard=keyboard)
            return
        await message.answer(
            f"👤 **Твой профиль**\n\n"
            f"🧑 Имя: {user.username}\n"
            f"🏙️ Город: {user.city_name}\n"
            f"📅 Зарегистрирован: {user.created_at.strftime('%d.%m.%Y')}"
        )
    @bot.on.message(text=["/change_username", "Сменить имя ✍️"])
    async def change_name(message: Message):
        user_id = message.from_id
        user = UserServices.get_user_by_id(user_id)
        if not user:
            await message.answer("Вы не зарегистрированы❌")
            return
        await bot.state_dispenser.set(message.peer_id, NameChangeState.WAIT_NEW_NAME)
        await message.answer("Введите новое имя", keyboard=cancel)
    @bot.on.message(state=NameChangeState.WAIT_NEW_NAME)
    async def changing_name(message: Message):
        user_id = message.from_id
        username = message.text.strip().title()
        if username == "Отменить":
            await message.answer("Отмена смены имени", keyboard=keyboard)
            await bot.state_dispenser.delete(message.peer_id)
            return
        if not username:
            await message.answer("Имя не должно быть пустым")
            return
        if username.isdigit():
            await message.answer("Имя не может состоять из цифр")
            return
        if len(username) < 2 or len(username) > 50:
            await message.answer("Некорректное имя пользователя, в имени должно быть от 2 до 50 символов")
            return
        new_username = UserServices.change_username(user_id, username)
        await bot.state_dispenser.delete(message.peer_id)
        await message.answer(f"Ваше новое имя: {username}", keyboard=keyboard)
