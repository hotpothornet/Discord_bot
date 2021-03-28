ticker = yf.Ticker('AAPL')
history = ticker.history(period='1mo', interval='1d')

df = pd.DataFrame.from_dict(history)

closing_prices = df['Close']

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(closing_prices, label='$y = numbers')
plt.title('Legend inside')
ax.legend()
plt.show()

fig.savefig('plot.png')