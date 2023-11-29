import telebot

bot = telebot.TeleBot('6834735235:AAHOfbM2S14z3u8Woa3ltZRHMH8Kvw1Riv8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!)')


@bot.message_handler(commands=['bread'])
def main(message):
    bot.send_message(message.chat.id, '*вкусный хлебушек*', parse_mode='Markdown')


bot.infinity_polling()
