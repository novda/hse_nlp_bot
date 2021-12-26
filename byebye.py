def byebye(bot, chat_id):
    bot.send_message(chat_id, "Пока пока👋")
    import state
    state.final = True
