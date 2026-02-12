from typing import Any, Dict

from fastapi.responses import JSONResponse


def generate_json_response(data: Dict[str, Any]) -> JSONResponse:
    return JSONResponse(content=data)
