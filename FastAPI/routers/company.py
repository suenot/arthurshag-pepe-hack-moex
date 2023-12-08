from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import company as CompanyService
from dto.company import Company as CompanyModel

router = APIRouter()


@router.post("/", tags=["company"])
async def create_company(data: CompanyModel = None, db: Session = Depends(get_db)):
    return CompanyService.add_company(data, db)


@router.get("/", tags=["company"])
async def get_all_companies(db: Session = Depends(get_db)):
    return CompanyService.get_all_companies(db)


@router.get("/{id}", tags=["company"])
async def get_company(id: int = None, db: Session = Depends(get_db)):
    return CompanyService.get_company(id, db)


@router.put("/{id}", tags=["company"])
async def update_company(id: int = None, data: CompanyModel = None, db: Session = Depends(get_db)):
    return CompanyService.update_company(id, data, db)


@router.delete("/{id}", tags=["company"])
async def delete_company(id: int = None, db: Session = Depends(get_db)):
    return CompanyService.remove_company(id, db)
