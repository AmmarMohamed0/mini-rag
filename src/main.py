from fastapi import FastAPI
from routes import base,data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

app = FastAPI()

@app.lifespan("startup")     #  event happened when starting
async def startup_db_clint():
    settings = get_settings()
    
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_clint = app.mongo_conn[settings.MONGODB_DATABASE]
    

@app.lifespan("shutdown")    #  event happened when shutting down
async def shutdown_db_clint():
    app.mongo_conn.close()


app.include_router(data.data_router)
app.include_router(base.base_router)

