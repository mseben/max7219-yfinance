import yfinance as yf
import time
import serial
import math

ttyUSB = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
time.sleep(2)

sleep_time = 120

while True:
    stock = yf.Ticker("IWDA.AS")
    price = stock.info['regularMarketPrice']
    str_price = str(f'{price:.2f}') + "  iwda.as"
    print(str_price)
    ttyUSB.write(str_price.encode())
    time.sleep(sleep_time)
    
    stock = yf.Ticker("ETH-EUR")
    price = stock.info['regularMarketPrice']
    str_price = str(f'{price:.2f}') + "  eth/eur"
    print(str_price)
    ttyUSB.write(str_price.encode())
    time.sleep(sleep_time)
    
    stock = yf.Ticker("BTC-EUR")
    price = stock.info['regularMarketPrice']
    str_price = str(f'{price:.2f}') + "  btc/eur"
    print(str_price)
    ttyUSB.write(str_price.encode())
    time.sleep(sleep_time)
