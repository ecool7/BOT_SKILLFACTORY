import telebot
from config import keys,TOKEN
from extensions import CovertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Привет! Чтобы начать работу введите команду в след.формате \n <имя валюты> < в какую перевести> \
     <количество переводимой валюты> \"" \
           "Допустимые валюты /values"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text' , ])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")
    if len(values) > 3:
        raise ConvertionExceptions('Слишком много переменных')
    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()