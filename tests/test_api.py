from fastapi.testclient import TestClient

from app.api.v1.schemas.wallet import WalletQueryCreate
from tests.fixtures.wallet_fixtures import prepopulated_wallets


def test_get_wallet_info(client: TestClient):
    """Test the get_wallet_info endpoint."""
    wallet_query_data = WalletQueryCreate(address="TSiru7uw2vmhGoLZeEfMqSq4Ew2yDM6dwC")

    response = client.post("/api/v1/wallet/", json=wallet_query_data.model_dump())

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "address" in data
    assert "balance" in data
    assert "bandwidth" in data
    assert "energy" in data
    assert "timestamp" in data


def test_get_wallets_info(client: TestClient, prepopulated_wallets):
    """Test the get_wallets_info endpoint."""
    response = client.get("/api/v1/wallets/")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == len(prepopulated_wallets)

    expected_data = {(w.balance, w.bandwidth, w.energy) for w in prepopulated_wallets}
    received_data = {
        (w["balance"], w["bandwidth"], w["energy"])
        for w in data
        if w["address"] == "TSiru7uw2vmhGoLZeEfMqSq4Ew2yDM6dwC"
    }

    assert expected_data == received_data
