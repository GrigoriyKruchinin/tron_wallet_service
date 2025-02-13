from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.repositories.wallet import WalletRepository
from app.services.wallet import WalletService
from app.api.v1.schemas.wallet import WalletQueryCreate, WalletQueryResponse

router = APIRouter()


@router.post("/wallet/", response_model=WalletQueryResponse)
async def get_wallet_info(
    wallet_query: WalletQueryCreate, db: AsyncSession = Depends(get_db)
):
    wallet_repository = WalletRepository(db)
    wallet_service = WalletService(wallet_repository)
    try:
        return await wallet_service.get_wallet_info(wallet_query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/wallets/", response_model=list[WalletQueryResponse])
async def get_wallet_queries(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    wallet_repository = WalletRepository(db)
    return await wallet_repository.get_wallet_queries(skip, limit)
