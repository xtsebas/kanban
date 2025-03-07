from fastapi import FastAPI
from routes.api import endpoints
from config.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(endpoints.router)
