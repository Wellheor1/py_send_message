from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from auth import verify_bearer_token

app = FastAPI(dependencies=[Depends(verify_bearer_token)])


@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World Well"})