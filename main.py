#bot.py
import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

import pandas_datareader as web

try:
    import chart
except ImportError:
    print('failed to import chart.py')

try:
    import currentstockprice
except ImportError:
    print('failed to import currentstockprice.py')

try:
    import quoting as qt
except ImportError:
    print('failed to import quoting.py')

try:
    import stockprice as sprice
except ImportError:
    print('failed to import stockprice.py')
    
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '?')
#change


@client.event
async def on_ready():
    print('Bot is ready')
    
    channel = client.get_channel(823914966473375765)
    await channel.send('stonky is online :)')
    try:
        os.remove('plot.png')
    except:
        pass

@client.command()
async def thierryquote(ctx):
    await ctx.send(qt.randomQuote())

@client.command()
async def getstockprice(ctx, tickersymbol):
    try:
        await ctx.send(f'Live price of {tickersymbol.upper()} is {currentstockprice.getPrice(tickersymbol.upper())}')
        print(currentstockprice.getPrice(tickersymbol.upper()))
    except:
        await ctx.send('Incorrect ticker!')
    
@client.command()
async def getplottedimage(ctx, ticker, period, interval, indicator: str):
    #to do: zorgen dat het plot.png niet wordt geopend iedere keer at de command gedaan wordt
    #to do: zorgen dat de vwap indicator werkt op hetzelfde aandeel en dezelfde periode en interval als de gehele grafiek
    if indicator == 'vwap' or indicator == 'VWAP':
        chart.getImage(ticker, period, interval, vwap=True)
    elif indicator == 'obv' or indicator == 'OBV':
        chart.getImage(ticker, period, interval, obv_signals=True)       
    else:
        chart.getImage(ticker, period, interval)
    
    await ctx.send(file=discord.File('plot.png'))
    time.sleep(1)
    os.remove('plot.png')

client.run(TOKEN)