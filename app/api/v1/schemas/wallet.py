from pydantic import BaseModel
from datetime import datetime


class WalletQueryBase(BaseModel):
    address: str


class WalletQueryCreate(WalletQueryBase):
    pass


class WalletQueryResponse(WalletQueryBase):
    id: int
    balance: int
    bandwidth: int
    energy: int
    timestamp: datetime

    class Config:
        from_attributes = True
