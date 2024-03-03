import telebot
from googletrans import Translator

# BotFatherdan olingan token
TOKEN = '6653305248:AAESDMkCOsbABGKvAavYih6Hn1WFuLX_aBU'
bot = telebot.TeleBot(TOKEN)

translator = Translator()


@bot.message_handler(commands=['start'])
def send_welcome(message):
  javob = '**Assalomu alaykum , Xush kelibsiz!**'
  javob += '\n Matinni yuboring: '
  bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Matnni tarjima qilish
    translation = translator.translate(message.text, dest='uz')
    # Tarjimani yuborish
    bot.reply_to(message, translation.text)

bot.polling()
