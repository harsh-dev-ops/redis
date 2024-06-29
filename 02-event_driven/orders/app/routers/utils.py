from typing import Annotated, List
from typing_extensions import Doc
from fastapi import HTTPException

from app.networks import apis
from app.conf.settings import settings


async def inventory_request(
    path: Annotated[str, Doc("Microservice url")],
    method: Annotated[str, Doc("GET, POST, PUT, PATCH, DELETE")],
    payload: Annotated[dict, Doc("Data as json (dict) format for api")] = {},
    status_codes: Annotated[List[int], Doc("Accepted Status Codes")] = [200]
):
    url = f"{settings.INVENTORY_SERVICE_URL}/{path}"
    
    resp, status_code = await apis.create_request(
        url=url,
        method=method,
        headers={'accept':'application/json'},
        payload=payload,
    )
    
    if status_code not in status_codes:
        raise HTTPException(
            status_code=500, detail='Error occured in inventory service.'
        )
    
    return (resp, status_code)
    
    