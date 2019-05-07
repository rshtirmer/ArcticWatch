from arctic import Arctic
from asciichartpy import plot
from colorama import init, Fore, Back, Style
import pandas as pd
import time
import os
from datetime import timedelta
import datetime as dt
import argparse

def updateChart(exchange, symbol, tf, height):
    store = Arctic('localhost')
    library = store[exchange.upper()]

    startDate = pd.to_datetime('today') - timedelta(days=5)
    endDate = startDate + timedelta(days=7)
    startDate = startDate.strftime("%Y-%m-%d")
    endDate = endDate.strftime("%Y-%m-%d")
    readStr = 'trades-' + str(symbol)

    item = library.read(readStr, chunk_range=pd.date_range(startDate,
                                                           endDate)).copy()

    df = item.price.resample(tf).agg({'open': 'first',
                                        'high': 'max',
                                        'low': 'min',
                                        'close': 'last'})
    df = df.fillna(method='ffill')
    chart = plot(df.close.tail(60), { 'height': height})

    priceStr = str(item.price.iat[-1])
    if(item.price.iat[-1] < item.price.iat[-2]):
        priceStr = Fore.RED + priceStr
    else:
        priceStr = Fore.GREEN + priceStr
    priceStr = priceStr + Style.RESET_ALL

    exchangeStr = exchange
    if(exchangeStr=="Bitfinex"):
        exchangeStr = Fore.GREEN + exchangeStr
    elif(exchangeStr=="Coinbase"):
        exchangeStr = Fore.BLUE + exchangeStr
    exchangeStr = exchangeStr + Style.RESET_ALL
    exchangeStr = exchange
    if(exchangeStr=="Bitfinex"):
        exchangeStr = Fore.GREEN + exchangeStr
    elif(exchangeStr=="Coinbase"):
        exchangeStr = Fore.BLUE + exchangeStr
    exchangeStr = exchangeStr + Style.RESET_ALL

    os.system('clear')
    print('Exchange: {}'.format(exchangeStr))
    print('Symbol: {}'.format(symbol))
    print('Timeframe: {}'.format(tf))
    print('Price: {}'.format(priceStr))
    print('{}'.format(chart))
    time.sleep(15)


def main():
    init()

    parser = argparse.ArgumentParser()
    parser.add_argument("--exchange", default='Bitfinex', help="Example: Bitfinex")
    parser.add_argument("--symbol", default='BTC-USD', help="Example: BTC-USD")
    parser.add_argument("--tf", default='1Min', help="Examples: 1Min, 15Min, 1H")
    parser.add_argument("--height", default=6, type=int, help="Chart Size")
    args = parser.parse_args()
    if args.exchange:
        pass

    if args.symbol:
        pass

    if args.tf:
        pass
    if args.height:
        pass

    while True:
        updateChart(args.exchange, args.symbol, args.tf, args.height)

if __name__== "__main__":
    main()
