from sqlalchemy.orm import Session

from models.forecast import Forecast as ForecastBase
from dto.forecast import Forecast as ForecastModel
from dto.forecast import ForecastPeriod


def add_forecast(data: ForecastModel, db: Session):
    forecast = ForecastBase(
        company_id=data.company_id,
        period=data.period,
        price=data.price,
        price_increase=data.price_increase
    )

    db.add(forecast)
    db.commit()
    db.refresh(forecast)

    return forecast


def get_all_forecasts(db: Session):
    return db.query(ForecastBase).all()


def update_forecast(id: int, period: ForecastPeriod, data: ForecastModel, db: Session):
    forecast = db.query(ForecastBase).filter(ForecastBase.company_id == id and ForecastBase.period == period).first()

    forecast.price = data.price
    forecast.price_increase = data.price_increase

    db.add(forecast)
    db.commit()
    db.refresh(forecast)

    return forecast


def delete_forecast(id: int, period: ForecastPeriod, db: Session):
    forecast = db.query(ForecastBase).filter(ForecastBase.company_id == id and ForecastBase.period == period).delete()

    db.commit()

    return forecast
