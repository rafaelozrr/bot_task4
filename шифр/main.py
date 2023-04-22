import telebot
import config

bot=telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.type == 'private':
        ans = ''
        for i in range(len(message.text)):
            ans += chr(ord(str(message.text)[i]) + 1)
        bot.send_message(message.chat.id, ans)


bot.infinity_polling()