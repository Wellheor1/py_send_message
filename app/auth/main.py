from fastapi import Header, HTTPException
from typing_extensions import Annotated
from app.settings import BEARER_TOKEN


async def verify_bearer_token(authorization: Annotated[str, Header()]):
    print(authorization)
    bearer_token = f"Bearer {BEARER_TOKEN}"
    if authorization != bearer_token:
        raise HTTPException(status_code=401, detail="bearer token invalid")
