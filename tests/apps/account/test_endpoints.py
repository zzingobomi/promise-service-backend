from fastapi import status
from fastapi.testclient import TestClient
from appserver.apps.account.models import User


async def test_user_detail_for_real_user(client: TestClient, host_user: User):
    response = client.get(f"/account/users/{host_user.username}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == host_user.username
    assert data["email"] == host_user.email
    assert data["display_name"] == host_user.display_name

    response = client.get("/account/users/not_found")
    assert response.status_code == status.HTTP_404_NOT_FOUND
