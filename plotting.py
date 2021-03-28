#In deze module gaan we een live candlestick plotte maken 
# met de matplotlib.pyplot module en een live index module

#used modules:
# *ta
# *yfinance


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import yfinance as yf

def loadData(stock: str, period: str):
    try:
        stockdata = yf.Ticker(stock.upper())
    except ValueError:
        print('not entered a correct stock ticker')

    try:
        history = stockdata.history(period=period)
    except ValueError:
        print('not entered a correct period')

    return history

def getSingleColumn(data, column):
    try:
        singlecolumn = data[column]
    except IndexError:
        print('not a correct column')
    try:
        df = pd.DataFrame.from_dict(singlecolumn)
    except IndexError:
        print('not able to transform dict to df')

    return df

def bb(stock):
    # Load datas
    stockdata = loadData(stock, '30d')
    getSingleColumn(stockdata, 'Close')

    df = getSingleColumn(stockdata, 'Close')

    
    #Maakt de 'Date' kolom de index_kolom
    #df = df.set_index('Date')

    #calculating the ma, upperbb, lowerb:
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['20dSTD'] = df['Close'].rolling(window=20).std() 

    df['Upper'] = df['MA20'] + (df['20dSTD'] * 2)
    df['Lower'] = df['MA20'] - (df['20dSTD'] * 2)

    #hieronder gaan we alles plotten
    df[['Close','MA20','Upper','Lower']].plot(figsize=(10,4))
    plt.grid(True)
    plt.title(stock + ' Bollinger Bands')
    plt.axis('tight')
    plt.ylabel('Price')
    plt.show()

    print(df)

bb('AAPL')

