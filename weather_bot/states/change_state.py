from vkbottle import BaseStateGroup

class CityChangeState(BaseStateGroup):
    WAIT_TITLE_OF_CITY = 0
    
class NameChangeState(BaseStateGroup):
    WAIT_NEW_NAME = 0