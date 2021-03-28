#This program uses the on-Balance Volume (OBV) to determine whether to buy or sell a stock

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def buy_sell(signal, col1, col2):
    #Buy Signals
    sigPriceBuy = []
    #Sell signals
    sigPriceSell = []
    flag = -1

    #Loop through the length of the data set
    for i in range(0, len(signal)):
        # If OBV > OBV_EMA Then Buy --> col1 => 'OBV' and col1 => 'OBV_EMA'
        if signal[col1][i] > signal[col2][i] and flag != 1:
            sigPriceBuy.append(signal['Close'][i])
            sigPriceSell.append(np.nan)
            #Flag is to let us know that we went to the if statement
            flag = 1

        # If OBV < OBV_EMA Then Sell
        elif signal[col1][i] < signal[col2][i] and flag != 0:
            sigPriceSell.append(signal['Close'][i])
            sigPriceBuy.append(np.nan)
            #Flag is set to be zero
            flag = 0

        #When they are equal --> Do Nothing
        else:
            sigPriceSell.append(np.nan)
            sigPriceBuy.append(np.nan)

    #LET OP DE INDENTATION,
    #want door de indentation heb ik daarnet een uur staan zoeken waardoor het kwam dat mijn functie zo raar deed,
    #terwijl het gewoon lag aan de indentation van return
    return (sigPriceBuy, sigPriceSell)


def getOBV(df):
    df = pd.DataFrame(df)
    
    try:
        df.set_index(pf.DatetimeIndex(df['Date'].values()))
    except:
        print('index error')

    OBV = []
    OBV.append(0)

    #Loop through the dataset (close price) from the second row (index(1)) to the end of the dataset
    for i in range(1, len(df.Close)):
        if df.Close[i] > df.Close[i-1]:
            #append the previous OBV plus the current volume
            OBV.append(OBV[-1] + df.Volume[i])
        elif df.Close[i] < df.Close[i-1]:
            #append previous OBV minus the current volume
            OBV.append(OBV[-1] - df.Volume[i])
        #closing price is equal to the previous closing price
        else:
            OBV.append(OBV[-1])

    df['OBV'] = OBV
    #this does the ema calculation for us
    df['OBV_EMA'] = df['OBV'].ewm(span=20).mean()

    x = buy_sell(df, 'OBV', 'OBV_EMA')

    df['Buy_Signal_Price'] = x[0]
    df['Sell_Signal_Price'] = x[1]
