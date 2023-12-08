from sqlalchemy.orm import Session

from models.company import Company as CompanyBase
from dto.company import Company as CompanyModel


def add_company(data: CompanyModel, db: Session):
    company = CompanyBase(
        name=data.name,
        ticker=data.ticker,
        icon=data.icon,
        description=data.description,
        background=data.background
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company


def get_all_companies(db: Session):
    return db.query(CompanyBase).all()


def get_company(id: int, db: Session):
    return db.query(CompanyBase).filter(CompanyBase.id == id).first()


def update_company(id: int, data: CompanyModel, db: Session):
    company = db.query(CompanyBase).filter(CompanyBase.id == id).first()

    company.name = data.name
    company.ticker = data.ticker
    company.icon = data.icon
    company.description = data.description
    company.background = data.background

    db.add(company)
    db.commit()
    db.refresh(company)

    return company


def remove_company(id: int, db: Session):
    company = db.query(CompanyBase).filter(CompanyBase.id == id).delete()

    db.commit()

    return company


def get_company_by_ticker(ticker: str, db: Session):
    return db.query(CompanyBase).filter(CompanyBase.ticker == ticker).first()

