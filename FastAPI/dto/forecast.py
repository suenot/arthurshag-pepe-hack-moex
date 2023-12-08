from pydantic import BaseModel
from enum import Enum


class ForecastPeriod(Enum):
    HOUR = "hour"
    WEEK = "week"
    MONTH = "month"


class Forecast(BaseModel):
    company_id: int
    period: str
    price: float
    price_increase: float
