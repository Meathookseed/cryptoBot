from commands import *
import commands
import telebot



bot=telebot.TeleBot('526776089:AAGS05XYS3UceO2XTtjGY5AWJNn_4anU4a4')

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Hello new user',reply_markup=start)
    commands.collecting_data()

@bot.message_handler(func=lambda message:message.text=='Poloniex')
def polo(message):
        bot.send_message(message.chat.id,message.text,reply_markup=poloniex)

@bot.message_handler(func=lambda message:message.text=='WEX')
def polo(message):
        bot.send_message(message.chat.id,message.text,reply_markup=wex)

@bot.message_handler(func=lambda message:message.text=='Назад')
def backward(message):
    bot.send_message(message.chat.id,message.text,reply_markup=start)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id,'Hello new user')

@bot.message_handler(func=lambda message:(message.text =='Получить данные о BTC'),content_types='text')
def polo_eth(message):
    commands.parse_polo_btc(message)

@bot.message_handler(func=lambda message:(message.text == 'Получить данные об ETH'),content_types='text')
def polo_btc(message):
    commands.parse_polo_eth(message)

if __name__=='__main__':
    bot.polling(none_stop=True)
