#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
bot.send_message(message.chat.id, message.text)
if__name__ == '__main__':
bot.polling(none_stop=True)
