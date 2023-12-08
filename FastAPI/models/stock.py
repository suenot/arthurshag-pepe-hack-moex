from sqlalchemy import Column, Integer, Float, ForeignKey
from database import Base


class Stock(Base):
    __tablename__ = "stocks"

    company_id = Column(Integer, ForeignKey("companies.id"), primary_key=True, unique=True)
    price = Column(Float)
    price_increase = Column(Float)
