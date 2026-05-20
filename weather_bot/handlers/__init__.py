from handlers.registration import initialize as reg
from handlers.weather_handlers import initialization as weather
from handlers.other_commands import initialize as other
from handlers.actions_with_profile import initialization as action
def initialization(bot):
    reg(bot)
    weather(bot)
    action(bot)
    other(bot)
