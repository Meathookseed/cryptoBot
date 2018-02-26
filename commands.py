from chat import *
from telebot import types
from db import dynamic_data_entry,data_fetch_btc,data_fetch_eth,data_fetch_wex

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
    bot.send_message(message.chat.id,data_fetch_eth(),parse_mode='HTML',
                     reply_markup=poloniex)
    bot.send_message(message.chat.id,'end')

def parse_polo_btc(message):
    bot.send_message(message.chat.id,data_fetch_btc(),parse_mode='HTML',
                     reply_markup=poloniex)
    bot.send_message(message.chat.id,'end')

def parse_wex(message):
    bot.send_message(message.chat.id, data_fetch_wex(), parse_mode='HTML',
                     reply_markup=wex)
    bot.send_message(message.chat.id, 'end')

def collecting_data():
    dynamic_data_entry()