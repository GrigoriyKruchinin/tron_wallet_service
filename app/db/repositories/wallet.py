from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.wallet import WalletQuery
from app.api.v1.schemas.wallet import WalletQueryCreate, WalletQueryResponse

class WalletRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_wallet_query(self, wallet_query: WalletQueryCreate, balance: int, bandwidth: int, energy: int):
        db_wallet_query = WalletQuery(
            address=wallet_query.address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy
        )
        self.db.add(db_wallet_query)
        await self.db.commit()
        await self.db.refresh(db_wallet_query)
        return db_wallet_query

    async def get_wallet_queries(self, skip: int = 0, limit: int = 10):
        result = await self.db.execute(
            select(WalletQuery).order_by(WalletQuery.timestamp.desc()).offset(skip).limit(limit)
        )
        return result.scalars().all()