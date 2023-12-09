import requests
import pandas as pd
import json
from moexalgo import Ticker
from datetime import datetime
from forecasts.forecast import new_data_was_added
import time


class TradingBot:
    def __init__(self):
        #######################################
        ##  данные для подлючения к брокеру  ##
        #######################################

        self.tickers = ['AFLT', 'BANE', 'DSKY', 'FEES', 'GAZP', 'PHOR', 'POSI', 'SBER', 'YNDX', 'MTLR']
        self.traiding_alg = TradingAlg(self.tickers)
        self.user_inf = pd.DataFrame()
        self.current_price = pd.DataFrame()
        self.forecast_price = pd.DataFrame()
        self.prev_price = []

    def set_params(self):
        self.load_user_inf()

        self.load_forecast_price()

        self.load_current_price()
        # объединение в один дф прогноза и текущей инфы

    def start_bot(self):
        is_start = True
        while True:
            if is_start:# or self.new_forecasts_was_added(self.prev_price):
                self.set_params()

                data_for_trad_strat = [self.user_inf, self.current_price, self.forecast_price]
                trading_strategy = self.traiding_alg.get_trading_strategy(data_for_trad_strat)
                self.do_trading_strategy(trading_strategy)

                is_start = False
            break

    def new_forecasts_was_added(self):
        forecast_price = requests.get(f'http://127.0.0.1:8000/forecast/').json()
        forecast_price = pd.DataFrame(forecast_price).price.tolist()

        return self.prev_price != [forecast_price[0], forecast_price[-1]]

    def load_user_inf(self):
        pass

    def load_forecast_price(self):
        forecast_price = requests.get(f'http://127.0.0.1:8000/forecast/').json()
        self.forecast_price = pd.DataFrame(forecast_price)

    def load_current_price(self):
        current_price = pd.DataFrame()

        for ticker_name in self.tickers:
            ticker = Ticker(ticker_name)

            tradestats = pd.DataFrame(ticker.tradestats(date=datetime.now(), limit=1))
            tradestats = tradestats[['secid', 'ts', 'pr_high', 'pr_low', 'pr_close', 'pr_change', 'trades']]

            orderbook = pd.DataFrame(ticker.obstats(date=datetime.now(), limit=1))
            orderbook = orderbook[['secid', 'ts', 'levels_b', 'levels_s', 'spread_bbo', 'spread_lv10', 'spread_1mio']]

            self.current_price = pd.concat([self.current_price, tradestats.merge(orderbook, on=['secid', 'ts'])])

        self.current_price.reset_index(drop=True, inplace=True)

    def do_trading_strategy(trading_strategy):
        pass


class TradingAlg:
    def __init__(self, tickers: list):
        self.tickers = tickers

    def get_trading_strategy(self, data):
        user_inf = data[0]
        current_price = data[1]
        forecast_price = data[2]

        print(current_price.columns)
        print(current_price)
        print(forecast_price)
        print(current_price.pr_change)

        for ticker in self.tickers:
            coolness_coef =






if __name__ == "__main__":
    trading_bot = TradingBot()
    trading_bot.start_bot()
