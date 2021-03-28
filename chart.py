#hier gaan we een command voor de bot schrijven zodat de bot een chart image kan versturen

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from obvind import getOBV
import yfinance as yf

import pandas_ta as pt
#stock info
#print(getDF('AAPL'))

#hier verder gaan
def vwap(ticker, period, interval):
    ticker = yf.Ticker(ticker.upper())
    history = ticker.history(period=period, interval=interval)

    df = pd.DataFrame.from_dict(history)
    #df.set_index(df[0])

    print(df)

    return pt.vwap(df['High'], df['Low'], df['Close'], df['Volume'])

def getImage(ticker : str, period : str, interval : str, **options):
    ticker = yf.Ticker(ticker.upper())
    history = ticker.history(period=period, interval=interval)

    df = pd.DataFrame.from_dict(history)
    
    closing_prices = df['Close']

    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(closing_prices, label='close price')
    
    if options.get('vwap') == True:
        try:
            ax.plot(pt.vwap(df['High'], df['Low'], df['Close'], df['Volume']), label='VWAP')
        except:
            print('index error vwap')
    elif options.get('obv_signals') == True:
        try:
            getOBV(df)
            ax.scatter(df.index, df['Buy_Signal_Price'], label = 'Buy Signal', marker = '^', alpha=1, color='green')
            ax.scatter(df.index, df['Sell_Signal_Price'], label = 'Sell Signal', marker='v', alpha=1, color='red')
        except:
            print('OBV plot error')
    else:
        pass

    plt.title(f'{ticker} price history')
    ax.legend()

    fig.savefig('plot.png')



