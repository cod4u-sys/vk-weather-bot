from vkbottle import Keyboard, KeyboardButtonColor, Text

keyboard = (Keyboard(one_time=False)
            .add(Text("Узнать погоду ☀"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Сменить город 🏙"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Подбросить кубик 🎲"), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text("Узнать время ⌚"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Показать профиль 👤"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Сменить имя ✍️"), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text("Помощь ℹ️"), color=KeyboardButtonColor.PRIMARY))
            