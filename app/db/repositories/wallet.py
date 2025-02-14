from sqlalchemy import select
from app.db.models.wallet import WalletQuery
from app.api.v1.schemas.wallet import WalletQueryCreate
from sqlalchemy.orm import Session


class WalletRepository:
    """Repository for working with wallet queries in the database.

    This abstraction layer is responsible for performing CRUD operations on the WalletQuery entity.
    It encapsulates the ORM logic, providing a convenient interface for the service layer.
    """

    def __init__(self, db: Session):
        """Initializes the repository with a database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def create_wallet_query(
        self, wallet_query: WalletQueryCreate, balance: int, bandwidth: int, energy: int
    ):
        """Creates a new wallet query entry in the database.

        Args:
            wallet_query (WalletQueryCreate): Wallet query data.
            balance (int): Wallet balance.
            bandwidth (int): Bandwidth usage.
            energy (int): Energy usage.

        Returns:
            WalletQuery: The created wallet query object.
        """
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
        """Returns a list of wallet queries sorted by timestamp.

        Args:
            skip (int, optional): Number of records to skip. Defaults to 0.
            limit (int, optional): Number of records to return. Defaults to 10.

        Returns:
            list[WalletQuery]: A list of wallet query objects.
        """
        result = self.db.execute(
            select(WalletQuery)
            .order_by(WalletQuery.timestamp.desc())
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
