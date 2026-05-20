from vkbottle import Bot, Keyboard
from vkbottle.bot import Message
from states.registration_states import RegState
from action_with_db.service import UserServices
from handlers.weather import Weather_Actions
from keyboards.main_keyboard import keyboard
def initialize(bot: Bot):
    @bot.on.message(text=["/start"])
    async def registration(message: Message):
        user_id = message.from_id
        user = UserServices.get_user_by_id(user_id)
        if not user:
            await bot.state_dispenser.set(message.peer_id, RegState.WAIT_NAME)
            await message.answer("Привет! Как тебя зовут?")
            return
        await message.answer(f"Привет, {user.username}!", keyboard=keyboard)

    @bot.on.message(state=RegState.WAIT_NAME)
    async def wait_name(message: Message):
        username = message.text.strip()
        if not username:
            await message.answer("Имя не должно быть пустым")
            return
        if username.isdigit():
            await message.answer("Имя не может состоять из цифр")
            return
        if len(username) < 2 or len(username) > 50:
            await message.answer("Некорректное имя пользователя, в имени должно быть от 2 до 50 символов")
            return
        username = username.title()
        await bot.state_dispenser.set(message.peer_id, RegState.WAIT_CITY, username=username)
        await message.answer("А в каком городе ты живешь?")
    
    @bot.on.message(state=RegState.WAIT_CITY)
    async def wait_city(message: Message):
        city_name = message.text.strip().title()
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
        user_id = message.from_id
        state_data = await bot.state_dispenser.get(message.peer_id)
        username = state_data.payload.get("username")
        await bot.state_dispenser.delete(message.peer_id)
        UserServices.add_user(user_id, username, official_city_name, coords["latitude"], coords["longitude"])
        await message.answer(f"Спасибо за регистрацию! {username}", keyboard=keyboard)