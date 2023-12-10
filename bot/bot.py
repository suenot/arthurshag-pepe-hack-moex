import requests
import pandas as pd
import json
from moexalgo import Ticker
from datetime import datetime
from forecasts.forecast import new_data_was_added
import time
import threading


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
            if is_start or self.new_forecasts_was_added(self.prev_price):
                self.set_params()

                data_for_trad_strat = [self.user_inf, self.current_price, self.forecast_price]
                trading_strategy = self.traiding_alg.get_trading_strategy(data_for_trad_strat)
                self.do_trading_strategy(trading_strategy)

                is_start = False
            break

    def new_forecasts_was_added(self):
        forecast_price = requests.get(f'http://127.0.0.1:8000/forecast/').json()
        forecast_price = pd.DataFrame(forecast_price).price.tolist()

        if self.prev_price != [forecast_price[0], forecast_price[-1]]:
            time.sleep(1)
            return True
        return False

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

    def do_trading_strategy(self, trading_strategy):
        for d in trading_strategy:
            if d[0] == 'stop_loss':
                self.backtest.set_stop_loss(d[1], d[2])
            if d[0] == 'order_buy':
                self.backtest.set_order_buy(d[1], d[2], d[3])
            if d[0] == 'order_sell':
                self.backtest.set_order_sell(d[1], d[2], d[3])



class TradingBot_backtest(TradingBot):
    def __init__(self, user, backtest):
        self.tickers = ['AFLT', 'BANE', 'DSKY', 'FEES', 'GAZP', 'PHOR', 'POSI', 'SBER', 'YNDX', 'MTLR']
        self.traiding_alg = TradingAlg(self.tickers)
        self.current_price = pd.DataFrame()
        self.forecast_price = pd.DataFrame()
        self.prev_price = []

        self.user_inf = user
        self.backtest = backtest
        self.thread = threading.Thread(target=self.start_bot)

    def start_thread(self):
        self.thread.start()

    def load_current_price(self):
        current_price = pd.DataFrame()

        for ticker_name in self.tickers:
            tradestats = self.backtest.get_tradestats()
            tradestats = tradestats[tradestats.secid == ticker_name].tail(1)

            orderbook = self.backtest.get_orderbook()
            orderbook = orderbook[orderbook.secid == ticker_name].tail(1)

            self.current_price = pd.concat([self.current_price, tradestats.merge(orderbook, on=['secid', 'ts'])])

        self.current_price.reset_index(drop=True, inplace=True)

    def new_forecasts_was_added(self):
        if self.backtest.forecast_was_adedd:
            self.backtest.forecast_was_adedd = False
            return True
        return False



class TradingAlg:
    def __init__(self, tickers: list):
        self.tickers = tickers
        self.lot_size = pd.read_csv('./backtest_data/lot_size.csv', index_col=0)
        self.pers_stop_loss = [0.02, 0.03, 0.04, 0.06, 0.08, 0.1]
        self.max_pers_stop_loss = 0
        self.pers_on_one_paper = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5]
        self.pers_money_in_stocks = [0.3, 0.4, 0.5, 0.7, 0.75, 1]
        self.pers_profit = 0.01
        self.max_pers_on_one_paper = 0
        self.max_pers_money_in_stocks = 0
        self.money_in_stocks = 0
        self.max_money_in_stocks = 0
        self.max_money_in_one_stock = 0

    def get_trading_strategy(self, data):
        trading_strategy = []
        user_inf = data[0]
        current_price = data[1]
        forecast_price = data[2]

        self.max_pers_on_one_paper = self.pers_on_one_paper[user_inf.risk_level]
        self.max_pers_money_in_stocks = self.pers_money_in_stocks[user_inf.risk_level]
        self.max_pers_stop_loss = self.pers_stop_loss[user_inf.risk_level]

        for ticker in user_inf.stocks.keys():
            lot_size = self.lot_size[self.lot_size.ticker == ticker].lot_size.values[0]
            cur_price_paper = current_price[current_price.secid == ticker].pr_close.values[-1]

            stock_price = lot_size * user_inf.stocks[ticker] * cur_price_paper
            self.money_in_stocks += stock_price

        self.max_money_in_one_stock = (self.money_in_stocks + user_inf.money) \
                                      * self.max_pers_money_in_stocks * self.max_pers_on_one_paper

        if self.money_in_stocks / (self.money_in_stocks + user_inf.money) < self.max_pers_money_in_stocks:
            best_papers = self.find_best_papers(current_price, forecast_price)

            mon_in_stoak = 0
            for i, r in best_papers.iterrows():
                if (mon_in_stoak + self.money_in_stocks) / (self.money_in_stocks + user_inf.money) >= self.max_pers_money_in_stocks:
                    break

                ticker = r.secid
                if r.pers_increase_sum > 0:
                    cur_price = current_price[current_price.secid == ticker].pr_close.values[-1]
                    trading_strategy.append(('stop_loss', ticker, self.max_pers_stop_loss*cur_price))
                    lot_size = self.lot_size[self.lot_size.ticker == ticker].lot_size.values[0]
                    num_lots = self.max_money_in_one_stock // (cur_price * lot_size)
                    mon_in_stoak -= cur_price*num_lots
                    trading_strategy.append(('order_buy', ticker, cur_price-cur_price*0.0005, num_lots))
                    user_inf.price_prev_buy.append((ticker, cur_price))

        for p in user_inf.price_prev_buy:
            ticker = p[0]
            cur_price = current_price[current_price.secid == ticker].pr_close.values[-1]
            if (cur_price - p[1]) / p[1] > self.pers_profit:
                num_lots = user_inf.stocks[ticker]
                trading_strategy.append(('order_sell', ticker, cur_price, num_lots))

        return trading_strategy


    def find_best_papers(self, current_price, forecast_price):

        for i, r in current_price.iterrows():
            cur_price = r.pr_close

            cur_forec = forecast_price[(forecast_price.ticker == r.secid)]

            current_price.loc[i, 'pred_hour'] = cur_forec[cur_forec.period == 'hour'].price.values[0]
            current_price.loc[i, 'pred_day'] = cur_forec[cur_forec.period == 'day'].price.values[0]
            current_price.loc[i, 'pred_week'] = cur_forec[cur_forec.period == 'week'].price.values[0]

            current_price.loc[i, 'pred_cur_prise_hour_diff'] = cur_forec[cur_forec.period == 'hour'].price_increase.values[0]
            current_price.loc[i, 'pred_cur_prise_day_diff'] = cur_forec[cur_forec.period == 'day'].price_increase.values[0]
            current_price.loc[i, 'pred_cur_prise_week_diff'] = cur_forec[cur_forec.period == 'week'].price_increase.values[0]

        current_price['pers_hour_increase'] = current_price['pred_cur_prise_hour_diff'] / current_price['pr_close']
        current_price['pers_day_increase'] = current_price['pred_cur_prise_day_diff'] / current_price['pr_close']
        current_price['pers_week_increase'] = current_price['pred_cur_prise_week_diff'] / current_price['pr_close']

        current_price['pers_increase_sum'] = current_price['pers_hour_increase'] + current_price['pers_day_increase'] + current_price['pers_week_increase']
        current_price.sort_values(by=['pers_increase_sum'], inplace=True, ascending=False)

        return current_price[['secid', 'pers_increase_sum']]



if __name__ == "__main__":
    trading_bot = TradingBot_backtest()
    trading_bot.start_bot()
