from chat import *
from telebot import types
import btce_parse
start = types.ReplyKeyboardMarkup(row_width=2)
choose_exchange = types.KeyboardButton('Poloniex')
choose_exchange2 = types.KeyboardButton('WEX')
start.add(choose_exchange,choose_exchange2)

poloniex = types.ReplyKeyboardMarkup(row_width=1)
btc_button = types.KeyboardButton('Получить данные о BTC')
eth_button = types.KeyboardButton('Получить данные об ETH')
backward = types.KeyboardButton('Назад')
poloniex.add(btc_button,eth_button,backward)

wex = types.ReplyKeyboardMarkup(row_width=1)
button1 = types.KeyboardButton('Получить данные')
wex.add(button1,backward)

def parse_polo_eth(message):
    bot.send_message(message.chat.id,btce_parse.parse_polo_eth(),parse_mode='HTML',
                     reply_markup=poloniex)
    bot.send_message(message.chat.id,'end')

def parse_polo_btc(message):
    bot.send_message(message.chat.id,btce_parse.parse_polo_btc(),parse_mode='HTML',
                     reply_markup=poloniex)
    bot.send_message(message.chat.id,'end')
