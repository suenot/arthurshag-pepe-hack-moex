from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import forecast as ForecastService
from dto.forecast import Forecast as ForecastModel
from dto.forecast import ForecastPeriod

router = APIRouter()


@router.post("/", tags=["forecast"])
async def create_forecast(data: ForecastModel = None, db: Session = Depends(get_db)):
    return ForecastService.add_forecast(data, db)


@router.get("/", tags=["forecast"])
async def get_all_forecasts(db: Session = Depends(get_db)):
    return ForecastService.get_all_forecasts(db)


@router.put("/{id}", tags=["forecast"])
async def update_forecast(id: int = None, period: ForecastPeriod = None, data: ForecastModel = None,
                          db: Session = Depends(get_db)):
    return ForecastService.update_forecast(id, period, data, db)


@router.delete("/{id}", tags=["forecast"])
async def delete_forecast(id: int = None, period: ForecastPeriod = None, db: Session = Depends(get_db)):
    return ForecastService.delete_forecast(id, period, db)
