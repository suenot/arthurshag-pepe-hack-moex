from sqlalchemy import Column, Integer, String
from database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    ticker = Column(String, unique=True)
    icon = Column(String)
    description = Column(String)
    background = Column(String)
