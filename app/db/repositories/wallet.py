from sqlalchemy import select
from app.db.models.wallet import WalletQuery
from app.api.v1.schemas.wallet import WalletQueryCreate, WalletQueryResponse
from sqlalchemy.orm import Session


class WalletRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wallet_query(
        self, wallet_query: WalletQueryCreate, balance: int, bandwidth: int, energy: int
    ):
        db_wallet_query = WalletQuery(
            address=wallet_query.address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy,
        )
        self.db.add(db_wallet_query)
        self.db.commit()
        self.db.refresh(db_wallet_query)
        return db_wallet_query

    def get_wallet_queries(self, skip: int = 0, limit: int = 10):
        result = self.db.execute(
            select(WalletQuery)
            .order_by(WalletQuery.timestamp.desc())
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
