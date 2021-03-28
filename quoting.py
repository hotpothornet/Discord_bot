import random
quotes = []

try:
    with open('quotes.txt', 'r') as f:
        for quote in f.readlines():
            quotes.append(quote.replace('\n', ''))
except FileExistsError:
    print('failed to find the file')

def randomQuote():
    return random.choice(quotes)
