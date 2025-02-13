from tronpy import Tron
from tronpy.providers import HTTPProvider
from app.core.config import settings
from app.db.repositories.wallet import WalletRepository
from app.api.v1.schemas.wallet import WalletQueryCreate


class WalletService:
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository
        self.tron_client = Tron(
            provider=HTTPProvider(api_key=settings.api_tron_key),
            network=settings.tron_network,
        )

    def get_wallet_info(self, wallet_query: WalletQueryCreate):
        try:
            balance = self.tron_client.get_account_balance(wallet_query.address)
            resources = self.tron_client.get_account_resource(wallet_query.address)
            bandwidth = resources.get("freeNetUsed", 0) + resources.get("NetLimit", 0)
            energy = resources.get("EnergyLimit", 0)

            db_wallet_query = self.wallet_repository.create_wallet_query(
                wallet_query, balance, bandwidth, energy
            )
            return db_wallet_query
        except Exception as e:
            raise ValueError(f"Error fetching wallet info: {str(e)}")
