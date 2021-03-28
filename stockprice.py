from datetime import datetime as dt

import matplotlib.pyplot as plt

import pandas_datareader as web

tickers = []

try:
    with open('tickers.txt', 'r') as f:
        for ticker in f.readlines():
            tickers.append(ticker.upper().replace('\n', ''))
except FileNotFoundError:
    print('file: tickers.txt not found')

#houden we voor nu eventjes op gisteren omdat ik nog niet goed weet hoe we de datetime goed kunnen parsen
start_date = '2021-03-22'
end_date = '2021-03-22'


df = web.DataReader('AAPL', 'yahoo', start_date, end_date)
#print(df)

plt.figure(figsize=(16,8))
plt.title('Closing price history')

#hiermee selecteer ik enkel de kolom 'Close'
plt.plot(df['Close'])

#labels voor de grafiek
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close price in USD $', fontsize=18)

#plt.show()

def getStockPrice(ticker: str):
    if ticker not in tickers:
        #is voor nu eventjes makkelijker
        print('choose between AAPL, TLSA and GOOG')
    else:
        stock_data = web.DataReader(ticker.upper(), 'yahoo', start_date, end_date)
        stock_close = df['Close']
    return stock_close
