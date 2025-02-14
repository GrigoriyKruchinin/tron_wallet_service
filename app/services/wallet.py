from tronpy import Tron
from tronpy.providers import HTTPProvider
from app.core.config import settings
from app.db.repositories.wallet import WalletRepository
from app.api.v1.schemas.wallet import WalletQueryCreate


class WalletService:
    """Service layer for interacting with wallet data.

    This layer is responsible for orchestrating the business logic related to wallet queries.
    It communicates with the Tron blockchain to fetch wallet-related data and persists it in the database.
    """

    def __init__(self, wallet_repository: WalletRepository):
        """Initializes the WalletService with the given wallet repository and Tron client.

        Args:
            wallet_repository (WalletRepository): Repository for interacting with wallet data in the database.
        """
        self.wallet_repository = wallet_repository
        self.tron_client = Tron(
            provider=HTTPProvider(api_key=settings.api_tron_key),
            network=settings.tron_network,
        )

    def get_wallet_info(self, wallet_query: WalletQueryCreate):
        """Fetches wallet information from the Tron blockchain and stores it in the database.

        This method retrieves the balance, bandwidth usage, and energy usage for a given wallet address.
        It then creates a new wallet entry in the database with the retrieved data.

        Args:
            wallet_query (WalletQueryCreate): Wallet query object containing the wallet address.

        Returns:
            WalletQuery: The created wallet query object saved in the database.

        Raises:
            ValueError: If there is an error fetching wallet information from the Tron blockchain.
        """
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
