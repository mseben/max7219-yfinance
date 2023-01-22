import configparser
import yfinance as yf
import serial
import random
import threading
from time import sleep

def getStockPrice(symbol):
    ticker = yf.Ticker(symbol)
    price = ticker.info['regularMarketPrice']
    if price is None:
        #todo try to use local cache
        todaysData = ticker.history(period='1d')
        return todaysData['Close'][0]
    else:
        return price

def getStockPricesPeriodically(stockNames,getDataSec):
    global prices
    while True:
        for stockName in stockNames:
            price = getStockPrice(stockName)
            print("[thread] fetched price for", stockName, ":" , price)
            prices[stockName] = price
        print("[thread] sleep for", getDataSec)
        sleep(getDataSec)

prices = {}
config = configparser.ConfigParser()
config.read('max7219-yfinance.ini')
stockNames = config['yfinance']['stock_names'].split(',')
getDataSec = int(config['yfinance']['get_data_sec'])

print(type(stockNames))
t1 = threading.Thread(target=getStockPricesPeriodically,args=(stockNames,getDataSec))
t1.start()

refreshDisplaySec = int(config['max7219']['refresh_display_sec'])
ttyDevice = config['max7219']['tty_device']
print(ttyDevice)

try:
    ttyUSB = serial.Serial(ttyDevice, 9600, timeout=0.5)
except:
    print("Can't open",ttyDevice,"for write")
    ttyUSB = None

#todo: wait for fully set prices 
sleep(10)

while True:
    for stockName in stockNames:
        price = prices[stockName]
        strPrice = str(f'{price:.2f}')
        displayStr = strPrice + ' ' + stockName
        print("show:",displayStr)
        if ttyUSB != None:
            ttyUSB.write(displayStr.encode())
        print("sleep for", refreshDisplaySec)
        sleep(refreshDisplaySec)
