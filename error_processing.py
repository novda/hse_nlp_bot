def error_processing(type, chat_id, bot):
    if type == 'unsupported_city':
        bot.send_message(chat_id, "Напиши город после /weather")
    elif type == 'none_data':
        bot.send_message(chat_id, "Напиши город и день, после /weather")
    elif type == 'unsupported_day':
        bot.send_message(chat_id, "Напиши время после /weather, я понимаю времена как: сейчас, сегодня, завтра")