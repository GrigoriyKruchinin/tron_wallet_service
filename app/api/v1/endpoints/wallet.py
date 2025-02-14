from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.repositories.wallet import WalletRepository
from app.services.wallet import WalletService
from app.api.v1.schemas.wallet import WalletQueryCreate, WalletQueryResponse

router = APIRouter()


@router.post("/wallet/", response_model=WalletQueryResponse)
def get_wallet_info(wallet_query: WalletQueryCreate, db: Session = Depends(get_db)):
    """Fetch wallet information based on the provided address and store it in the database.

    This endpoint calls the WalletService to fetch wallet details like balance, bandwidth, and energy.
    The fetched data is then saved into the database and returned as a response.

    Args:
        wallet_query (WalletQueryCreate): The request body containing the wallet address.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        WalletQueryResponse: The wallet query response with wallet details.

    Raises:
        HTTPException: If there is an error while fetching wallet info, a 400 HTTPException is raised.
    """
    wallet_repository = WalletRepository(db)
    wallet_service = WalletService(wallet_repository)
    try:
        return wallet_service.get_wallet_info(wallet_query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/wallets/", response_model=list[WalletQueryResponse])
def get_wallet_queries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of wallet queries from the database.

    This endpoint fetches the wallet data from the database with pagination support.

    Args:
        skip (int, optional): The number of items to skip (for pagination). Defaults to 0.
        limit (int, optional): The number of items to retrieve (for pagination). Defaults to 10.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        list[WalletQueryResponse]: A list of wallet queries with wallet details.
    """
    wallet_repository = WalletRepository(db)
    return wallet_repository.get_wallet_queries(skip, limit)
