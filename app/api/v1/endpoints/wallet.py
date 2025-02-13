from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.repositories.wallet import WalletRepository
from app.services.wallet import WalletService
from app.api.v1.schemas.wallet import WalletQueryCreate, WalletQueryResponse

router = APIRouter()


@router.post("/wallet/", response_model=WalletQueryResponse)
def get_wallet_info(wallet_query: WalletQueryCreate, db: Session = Depends(get_db)):
    wallet_repository = WalletRepository(db)
    wallet_service = WalletService(wallet_repository)
    try:
        return wallet_service.get_wallet_info(wallet_query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/wallets/", response_model=list[WalletQueryResponse])
def get_wallet_queries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    wallet_repository = WalletRepository(db)
    return wallet_repository.get_wallet_queries(skip, limit)
