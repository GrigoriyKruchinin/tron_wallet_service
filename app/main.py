from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import wallet

app = FastAPI(title=settings.PROJECT_NAME)


app = FastAPI(title="Tron Wallet Service")
app.include_router(wallet.router, prefix="/api/v1")
