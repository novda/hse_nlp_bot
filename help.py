def help(chat_id, bot):
    bot.send_message(chat_id, "Я могу рассказать про погоду в Петербурге или в Москве")
    bot.send_message(chat_id, "Напиши город и время в таком ввиде:")
    bot.send_message(chat_id, "/weather <i>Хочу погоду на завтра в Москве</i>", parse_mode="HTML")