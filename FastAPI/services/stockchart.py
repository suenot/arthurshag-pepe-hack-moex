from sqlalchemy.orm import Session
from moexalgo import Ticker
from datetime import date

from services.company import get_company


def get_stockchart(id: int, db: Session, date_from: str = None, date_to: str = None):
    try:
        ticker = get_company(id, db).ticker
    except:
        return

    date_from = date.fromisoformat("2020-01-01") if date_from is None else date.fromisoformat(date_from)
    date_to = date.today() if date_to is None else date.fromisoformat(date_to)

    ticker_data = Ticker(ticker)
    candles = ticker_data.candles(date=date_from, till_date=date_to, period="D")

    result = []

    for _, candle in candles.iterrows():
        result.append({
            "trade_date": candle.end.date(),
            "close": candle.close,
            "open": candle.open,
            "high": candle.high,
            "low": candle.low
        })

    return result
