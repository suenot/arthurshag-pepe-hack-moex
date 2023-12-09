from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import forecast as ForecastService
from dto.forecast import Forecast as ForecastModel
from dto.forecast import ForecastPeriod

router = APIRouter()


@router.get("/", tags=["forecast"])
async def get_all_forecasts(db: Session = Depends(get_db)):
    return ForecastService.get_all_forecasts(db)


@router.post("/{id}", tags=["forecast"])
async def update_forecast(data: ForecastModel = None, db: Session = Depends(get_db)):
    return ForecastService.update_forecast(data, db)


@router.delete("/{id}", tags=["forecast"])
async def delete_forecast(id: int = None, period: ForecastPeriod = None, db: Session = Depends(get_db)):
    return ForecastService.delete_forecast(db, id, period)
