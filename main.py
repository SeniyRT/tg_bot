import time

import telebot
bot = telebot.TeleBot('6958785971:AAEvDh9s3ucFBI4jPGliZXZ5iTW1R9K8mkQ')

@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'Privet':
        bot.send_message(1685212625, 'Hello, how I can hellp you? Как дела')
    elif message.text == '/help':
        bot.send_message(1685212625, f'{message.from_user.first_name} Задал вопрос')
    bot.send_message(1685212625, 'Чушка скинь дз')
    bot.send_message(1428171460, 'Чушка скинь дз')


    print(message)







bot.polling(none_stop= True, interval= 0)
