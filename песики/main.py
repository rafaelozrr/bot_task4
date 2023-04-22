import telebot
from req import get_url
import config
bot=telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет,')




@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.type == 'private':
        url = get_url()
        bot.send_document(message.chat.id, url)


bot.infinity_polling()