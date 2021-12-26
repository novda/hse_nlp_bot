import time
def nu_che_tam(chat_id, bot):
    import state
    while not state.final:
        time.sleep(30)
        bot.send_message(chat_id, "Ну что там? Хочешь погоду узнать?\nЕсли нет, напиши stop")