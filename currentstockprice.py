from yahoo_fin import stock_info as si

def getPrice(ticker):
    try:
        return si.get_live_price(ticker.upper())
    except IndexError:
        print('incorrect stock ticker')

def getDF(ticker):
    try:
        return si.get_quote_table(ticker.upper(), dict_result = False)
    except IndexError:
        print('incorrect stock ticker')