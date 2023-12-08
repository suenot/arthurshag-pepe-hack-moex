from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import stock as StockService

router = APIRouter()


@router.get("/{id}", tags=["stocks"])
async def get_stock_with_forecasts(id: int = None, db: Session = Depends(get_db)):
    return StockService.get_stock_with_forecasts(id, db)
