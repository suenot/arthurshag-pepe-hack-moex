from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import stockchart as StockchartService

router = APIRouter()


@router.get("/{id}", tags=["stockchart"])
async def get_stockchart(id: int = None, date_from: str = None, date_to: str = None, db: Session = Depends(get_db)):
    return StockchartService.get_stockchart(id, db, date_from, date_to)
