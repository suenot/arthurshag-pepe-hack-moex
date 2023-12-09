import uvicorn
from fastapi import FastAPI
from database import engine, Base
from routers.company import router as CompanyRouter
from routers.stock import router as StockRouter
from routers.stocks import router as StocksRouter
from routers.forecast import router as ForecastRouter
from routers.stockchart import router as StockchartRouter
from routers.stocks_catalog import router as StocksCatalogRouter


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(CompanyRouter, prefix="/company")
app.include_router(StockRouter, prefix="/stock")
app.include_router(StocksRouter, prefix="/stocks")
app.include_router(ForecastRouter, prefix="/forecast")
app.include_router(StockchartRouter, prefix="/stockchart")
app.include_router(StocksCatalogRouter, prefix="/stocks-catalog")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
