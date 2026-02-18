from __future__ import annotations

from typing import Generator

import pytest
from flask.testing import FlaskClient

from app import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    with app.test_client() as client:
        yield client


def test_index(client: FlaskClient) -> None:
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, dict)
    assert data.get("status") == "Finance API is running"
