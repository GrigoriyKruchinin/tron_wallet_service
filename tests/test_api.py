from fastapi.testclient import TestClient

from app.api.v1.schemas.wallet import WalletQueryCreate


def test_get_wallet_info(client: TestClient):
    wallet_query_data = WalletQueryCreate(address="TXYZ9z92s6rc6dbNGgL9LC8RxnWLkWWhRYH")

    response = client.post("/wallet/", json=wallet_query_data.model_dump())

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "address" in data
    assert "balance" in data
    assert "bandwidth" in data
    assert "energy" in data
    assert "timestamp" in data
