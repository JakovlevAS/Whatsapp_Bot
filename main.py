from whatsapp_chatbot_python import GreenAPIBot, Notification

bot = GreenAPIBot("",'')
)


@bot.router.message(text_message="start")
def message_handler(notification: Notification) -> None:
    notification.answer(
        (
            f"Привет, что вы хотите?: \n \n"
            "1. Узнать ближайшие мероприятия по направлению\n"
            "2. Записаться на мероприятие\n"
            "3. Связаться с технической поддержкой\n \n"
            "Выберите вариант и отправьте его мне"
        )
    )


@bot.router.message(text_message=["1", "Узнать ближайшие мероприятия по направлению"])
def meropriyatiya(notification: Notification) -> None:
    notification.answer("ссылка")  # ссылка для получения ближайших мероприятий


@bot.router.message(text_message=["2", "Записаться на мероприятие"])
def zapis(notification: Notification) -> None:
    notification.answer(
        (
            f"На какое мероприятие?\n"
            "1. Мероприятие 1\n"
            "2. Мероприятие 2\n"
            "3. Мероприятие 3\n"
            "4. Мероприятие 4\n"
        )
    )

@bot.router.message(text_message=["1"])
def meropriyatie1(notification: Notification) -> None:
    notification.answer("Ссылка на Мероприятие 1")  # ссылка на первое мероприятие

@bot.router.message(text_message=["2"])
def meropriyatie2(notification: Notification) -> None:
    notification.answer("Ссылка на Мероприятие 2")   # ссылка на второе мероприятие

@bot.router.message(text_message=["3"])
def meropriyatie3(notification: Notification) -> None:
    notification.answer("Ссылка на Мероприятие 3")  # ссылка на третье мероприятие

@bot.router.message(text_message=["4"])
def meropriyatie4(notification: Notification) -> None:
    notification.answer("Ссылка на Мероприятие 4")  # ссылка на четвертое мероприятие



@bot.router.message(text_message=["3", "Связаться с технической поддержкой"])
def call_support_operator(notification: Notification) -> None:
    notification.answer("Хорошо, техническая поддержка свяжется с вами")


bot.run_forever()
