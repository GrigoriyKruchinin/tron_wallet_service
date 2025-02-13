from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String
from app.db.base import Base


class WalletQuery(Base):
    """
    WalletQuery model for representing wallet queries in the database.

    Attributes:
        id (int): Unique identifier for the wallet query. Primary key.
        address (str): Wallet address.
        balance (int): Wallet balance.
        bandwidth (int): Wallet bandwidth.
        energy (int): Wallet energy.
        timestamp (datetime): Timestamp of the record creation. Defaults to the current time.
    """

    __tablename__ = "wallet_queries"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(Integer)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
