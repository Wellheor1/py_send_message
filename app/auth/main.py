from fastapi import Header, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing_extensions import Annotated
from app.settings import BEARER_TOKEN

security = HTTPBearer()


async def verify_bearer_token(authorization: Annotated[str, Header()]):
    bearer_token = f"Bearer {BEARER_TOKEN}"
    if authorization != bearer_token:
        raise HTTPException(status_code=401, detail="bearer token invalid")


async def verify_bearer_token_v2(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="bearer token invalid")
