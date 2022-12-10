# Import the required modules
import configparser
import yahoo_fin.stock_info as yf
import serial

# Open the ttyUSB serial connection
ttyUSB = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the ini file
config.read('stock.ini')

# Get the list of ticker symbols from the ini file
tickers = config['DEFAULT']['stock_name'].split(',')

# Get the frequency value from the ini file
n = int(config['DEFAULT']['frequency'])

# Loop forever
while True:
    # Loop through the list of ticker symbols
    for ticker in tickers:
        # Get the Ticker object for the stock with the ticker symbol
        stock = yf.Ticker(ticker)

        # Print the price every minute
        print(stock.info['regularMarketPrice'])

        # Get the price of the stock every n minutes
        if i % n == 0:
            price = stock.info['regularMarketPrice']

            # Format the price as a string with two decimal places
            str_price = str(f'{price:.2f}')

            # Print the price
            print(str_price)

            # Write the price to the ttyUSB device
            ttyUSB.write(str_price.encode())

        # Increment the counter
        i += 1

    # Wait for 1 minute
    time.sleep(60)
