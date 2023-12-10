from datetime import datetime, timedelta
import pandas as pd
from bot import TradingAlg
import time
import requests
from forecasts.forecast import start_forecast_backtest
import threading
from bot import TradingBot_backtest

import warnings
warnings.filterwarnings('ignore')

class User:
    def __init__(self, end_investment, risk_level, money, stocks):
        self.end_investment = end_investment
        self.risk_level = risk_level
        self.money = money
        self.stocks = stocks
        self.price_prev_buy = []


class BackTest:
    def __init__(self, time_interval, user):
        self.time_interval = time_interval
        self.user = user

        self.tradestats_data = pd.read_csv('./backtest_data/backtest_tradestats.csv', index_col=0)
        self.tradestats_data['ts'] = self.tradestats_data['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
        self.obstats_data = pd.read_csv('./backtest_data/backtest_obstats.csv', index_col=0)
        self.obstats_data['ts'] = self.obstats_data['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
        self.orderbook_data = pd.read_csv('./backtest_data/backtest_orderbook.csv', index_col=0)
        self.orderbook_data['ts'] = self.orderbook_data['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

        self.tradestats = pd.read_csv('./backtest_data/backtest_tradestats_2023-10-01_2023-10-31.csv', index_col=0)
        self.tradestats['ts'] = self.tradestats['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
        self.obstats = pd.read_csv('./backtest_data/backtest_obstats_2023-10-01_2023-10-31.csv', index_col=0)
        self.obstats['ts'] = self.obstats['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
        self.orderbook = pd.read_csv('./backtest_data/backtest_orderbook_2023-10-01_2023-10-31.csv', index_col=0)
        self.orderbook['ts'] = self.orderbook['ts'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

        self.lot_size = pd.read_csv('./backtest_data/lot_size.csv', index_col=0)

        self.stop_losses = {}#{'ticker': prise}
        self.orders_buy = {}#{'ticker': (prise, num_lots)}
        self.orders_sell = {}#{'ticker': (prise, num_lots)}

        self.new_data_was_adedd = False
        self.forecast_was_adedd = False

        self.thread = threading.Thread(target=self.start_test)

    def start_thread(self):
        self.thread.start()

    def start_test(self):
        datetime_stop = datetime.strptime('2023-11-14 18:40:00', "%Y-%m-%d %H:%M:%S")
        cur_datetime = datetime.strptime('2023-11-01 10:05:00', "%Y-%m-%d %H:%M:%S")
        print('ТЕСТ НАЧАЛСЯ\n')

        while True:
            print('\n', '#'*80)
            print('Дата: ', cur_datetime, '\n')
            print(f'Портфель: {self.user.money} рублей')
            for stock in self.user.stocks.keys():
                print(f'{stock}: {self.user.stocks[stock]} лотов')

            new_tradestats = self.tradestats_data[self.tradestats_data.ts == cur_datetime]
            self.tradestats = pd.concat([self.tradestats, new_tradestats])

            new_obstats = self.obstats_data[self.obstats_data.ts == cur_datetime]
            self.obstats = pd.concat([self.obstats, new_obstats])

            new_orderbook = self.orderbook_data[self.orderbook_data.ts == cur_datetime]
            self.orderbook = pd.concat([self.orderbook, new_orderbook])

            self.check_stop_losses()
            self.check_orders()

            self.new_data_was_adedd = True

            if cur_datetime == datetime_stop:
                print('ТЕСТ ЗАКОНЧЕН')
                time.sleep(time_interval)
                break

            cur_datetime = self.set_cur_datetime(cur_datetime)

            time.sleep(self.time_interval)

    def set_cur_datetime(self, cur_datetime):
        cur_datetime += timedelta(minutes=5)

        if cur_datetime.time() == datetime.strptime('18:45:00', '%H:%M:%S').time():
            cur_datetime += timedelta(days=1)
            cur_datetime = cur_datetime.replace(minute=5, hour=10)

        if cur_datetime.weekday() == 5:
            cur_datetime += timedelta(days=2)

        return cur_datetime

    def get_new_data_was_adedd(self):
        return self.new_data_was_adedd

    def set_new_data_was_adedd(self, value):
        self.new_data_was_adedd = value

    def get_tradestats(self):
        return self.tradestats

    def get_obstats(self):
        return self.obstats

    def get_orderbook(self):
        return self.orderbook

    def set_order_buy(self, ticker, offered_price, num_lots):
        print(f'Установлена заявка на покупку {num_lots}, {ticker}, Цена покупки: {offered_price}')
        self.orders_buy[ticker] = (offered_price, num_lots)

    def set_order_sell(self, ticker, offered_price, num_lots):
        print(f'Установлена заявка на продажу {num_lots}, {ticker}, Цена продажи: {offered_price}')
        self.orders_buy[ticker] = (offered_price, num_lots)

    def check_orders(self):
        for ticker in self.orders_sell.keys():
            pr_h = self.tradestats[self.tradestats.secid == ticker].pr_high.values[-1]

            if pr_h < self.orders_sell[ticker]:
                lot_size = self.lot_size[self.lot_size.ticker == ticker]
                num_stocks = self.orders_sell[ticker][1] * lot_size
                order_size = self.orders_sell[ticker][0] * num_stocks

                if lot_size <= self.user.stocks[ticker]:
                    self.user.stocks[ticker] -= self.orders_sell[ticker][1]
                    self.user.money += order_size
                    print(f'Бумага {ticker} в кол-ве {num_stocks} лота продана по цене {self.orders_sell[ticker][0]}, покупалась по {self.user.price_prev_buy[ticker]}')
                    del self.orders_sell[ticker]

        ks = list(self.orders_buy.keys())
        for ticker in ks:
            pr_l = self.tradestats[self.tradestats.secid == ticker].pr_low.values[-1]

            if self.orders_buy[ticker] != () and pr_l > self.orders_buy[ticker][0]:
                lot_size = self.lot_size[self.lot_size.ticker == ticker].lot_size.values[0]
                num_stocks = self.orders_buy[ticker][1] * lot_size
                order_size = self.orders_buy[ticker][0] * num_stocks

                if order_size < self.user.money:
                    self.user.stocks[ticker] += self.orders_buy[ticker][1]

                    self.user.money -= order_size
                    print(
                        f'Бумага {ticker} в кол-ве {num_stocks} лота куплена по цене {self.orders_buy[ticker][0]}. Объем покупки = {order_size}')
                    del self.orders_buy[ticker]

    def set_stop_loss(self, ticker, stop_loss):
        self.stop_losses[ticker] = stop_loss

    def del_stop_loss(self, ticker):
        del self.stop_losses[ticker]

    def check_stop_losses(self):
        for ticker in self.stop_losses.keys():
            pr_low = self.tradestats[self.tradestats.secid == ticker].pr_low.values[-1]
            if pr_low <= self.stop_losses[ticker]:

                lot_size = self.lot_size[self.lot_size.ticker == ticker]
                num_stocks = self.user.stocks[ticker] * lot_size
                order_size = self.stop_losses[ticker] * num_stocks

                self.user.stocks[ticker] = 0
                self.user.money += order_size
                print(f'Бумага {ticker} в кол-ве {num_stocks} лота продана по стоп-лосу по цене {order_size}')
                del self.stop_losses[ticker]


if __name__ == "__main__":
    time_interval = 2
    tickers = ['AFLT', 'BANE', 'DSKY', 'FEES', 'GAZP', 'PHOR', 'POSI', 'SBER', 'YNDX', 'MTLR']
    stocks = {ticker: 0 for ticker in tickers}

    end_investment = datetime.strptime('30-11-2023 12:00:00', "%d-%m-%Y %H:%M:%S")

    user = User(end_investment=end_investment, risk_level=3, money=100000, stocks=stocks)

    backtest = BackTest(time_interval, user)
    trading_bot = TradingBot_backtest(user, backtest)

    backtest.start_thread()
    trading_bot.start_thread()
    thread1 = threading.Thread(target=start_forecast_backtest(backtest))
    thread1.start()








