import configparser
import yfinance as yf
import serial
import random
import threading
from time import sleep

def getStockPrices(stockName):
    global price
    stock = yf.Ticker(stockName)
    price = stock.info['regularMarketPrice']
#    price = random.randint(2,9)
    print("[thread] price of ",stockName, " is ", price)
    return price

def getStockPricesPeriodically(stockNames,getDataSec):
    global prices
    while True:
        for stockName in stockNames:
            price = getStockPrices(stockName)
            prices[stockName] = price
        print("[thread] sleep for ", getDataSec)
        sleep(getDataSec)

prices = {}
config = configparser.ConfigParser()
config.read('stock.ini')
stockNames = config['yfinance']['stock_name'].split(',')
getDataSec = int(config['yfinance']['get_data_sec'])

print(type(stockNames))
t1 = threading.Thread(target=getStockPricesPeriodically,args=(stockNames,getDataSec))
t1.start()

sleep(10)

refreshDisplaySec = int(config['max7219']['refresh_display_sec'])
while True:
    for stockName in stockNames:
        print("price of ",stockName," = ", prices[stockName])
        print("sleep for ", refreshDisplaySec)
        sleep(refreshDisplaySec)

#ttyUSB = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
#config = configparser.ConfigParser()
#config.read('stock.ini')
#tickers = config['DEFAULT']['stock_name'].split(',')
#n = int(config['DEFAULT']['frequency'])

#while True:
#    for ticker in tickers:
#        stock = yf.Ticker(ticker)
#        print(stock.info['regularMarketPrice'])
#        if i % n == 0:
#            price = stock.info['regularMarketPrice']
#            str_price = str(f'{price:.2f}')
#            print(str_price)
#            ttyUSB.write(str_price.encode())
#        i += 1
#    time.sleep(60)
