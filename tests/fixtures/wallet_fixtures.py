import pytest
from sqlalchemy.orm import Session
from app.db.repositories.wallet import WalletRepository
from app.api.v1.schemas.wallet import WalletQueryCreate


@pytest.fixture(scope="function")
def wallet_repository(db_session: Session) -> WalletRepository:
    return WalletRepository(db=db_session)


@pytest.fixture
def prepopulated_wallets(db_session: Session):
    """Creates prepopulated wallets for testing."""
    wallet_repo = WalletRepository(db_session)

    address = "TSiru7uw2vmhGoLZeEfMqSq4Ew2yDM6dwC"
    test_data = [
        {"balance": 0, "bandwidth": 10, "energy": 5},
        {"balance": 100, "bandwidth": 50, "energy": 25},
        {"balance": 500, "bandwidth": 200, "energy": 100},
        {"balance": 1000, "bandwidth": 500, "energy": 250},
    ]

    created_wallets = []
    for data in test_data:
        created_wallets.append(
            wallet_repo.create_wallet_query(
                WalletQueryCreate(address=address),
                balance=data["balance"],
                bandwidth=data["bandwidth"],
                energy=data["energy"],
            )
        )

    db_session.commit()
    return created_wallets
