# tests/test_views.py

from src.views import generate_json_response


def test_generate_json_response_structure() -> None:
    response = generate_json_response({"test": 1})
    assert response is not None
