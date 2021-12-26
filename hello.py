def hello(bot, chat_id, message):
    import state
    state.state = {
        'city': None,
        'day': None}
    bot.send_message(chat_id, f"Приветсвую тебя {message.from_user.first_name}!")
    bot.send_message(chat_id, "Я могу рассказать про погоду в Петербурге или в Москве")
    bot.send_message(chat_id, "Напиши город и время")
