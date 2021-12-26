# from telebot.async_telebot import AsyncTeleBot
#
# import byebye as bye
# import hello
# import help
# import rec_intention
# from get_weather import get_weather
# from project_manager import nu_che_tam
# import asyncio
#
# bot = AsyncTeleBot('2016486951:AAEOoaV0N1rYTMt7VU3YtqlaUX_j2RgqdhU')
#
#
# @bot.message_handler(content_types=['text'])
# async def get_text_messages(message):
#     chat_id = message.from_user.id
#     import state
#     state.final = False
#     if message.text.lower() == "stop":
#         bye.byebye(bot, chat_id)
#     elif message.text == "/help":
#         help.help(chat_id, bot)
#     elif message.text == "/start":
#         hello.hello(bot, chat_id, message)
#     elif isinstance(message.text, str):
#         data = rec_intention.rec_intention(message.text, chat_id, bot)
#         if data['city'] is not None and data['day'] is not None:
#             await bot.send_message(chat_id, get_weather(data))
#     else:
#         await bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#     await nu_che_tam(chat_id, bot)
#
#
# asyncio.run(bot.polling(none_stop=True, interval=0))
