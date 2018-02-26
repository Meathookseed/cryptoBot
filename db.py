import sqlite3
import coin_info
import time

#1.create db

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS data (btc TEXT,eth TEXT,wex TEXT,time REAL)")
    c.close()
    conn.close()

def data_entry():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    unix = time.time()
    c.execute("INSERT INTO data VALUES(?,?,?,?)", (coin_info.parse_polo_btc(), coin_info.parse_polo_eth(),
                                                   coin_info.wex(), unix))
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    conn = sqlite3.connect('example.db')
    while True:
        data_entry()
        time.sleep(1)
        conn.commit()

def data_fetch_eth():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("select eth from data order by time desc limit 1")
    message =''
    mes = c.fetchall()
    for row in mes:
        message+=str(row)
    return row
    conn.commit()
    c.close()
    conn.close()

def data_fetch_btc():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("select btc from data order by time desc limit 1")
    message =''
    mes = c.fetchone()
    for row in mes:
        message+=str(row)
    return row
    conn.commit()
    c.close()
    conn.close()

def data_fetch_wex():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("select wex from data order by time desc limit 1")
    message = ''
    mes = c.fetchone()
    for row in mes:
        message += str(row)
    return row
    conn.commit()
    c.close()
    conn.close()



