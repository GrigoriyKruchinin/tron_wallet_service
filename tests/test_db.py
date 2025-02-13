import pytest
from app.db.repositories.wallet import WalletRepository
from app.db.models.wallet import WalletQuery
from app.api.v1.schemas.wallet import WalletQueryCreate
from sqlalchemy.orm import Session


@pytest.fixture(scope="function")
def wallet_repository(db_session: Session) -> WalletRepository:
    return WalletRepository(db=db_session)


def test_create_wallet_query(wallet_repository: WalletRepository, db_session: Session):
    wallet_query_data = WalletQueryCreate(address="TXYZ9z92s6rc6dbNGgL9LC8RxnWLkWWhRYH")
    balance = 1000
    bandwidth = 500
    energy = 200

    wallet_query = wallet_repository.create_wallet_query(
        wallet_query_data, balance, bandwidth, energy
    )

    db_wallet_query = (
        db_session.query(WalletQuery)
        .filter_by(address=wallet_query_data.address)
        .first()
    )

    assert db_wallet_query is not None
    assert db_wallet_query.address == wallet_query_data.address
    assert db_wallet_query.balance == balance
    assert db_wallet_query.bandwidth == bandwidth
    assert db_wallet_query.energy == energy
    assert db_wallet_query.timestamp is not None
