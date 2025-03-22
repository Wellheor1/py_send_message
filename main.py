from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from auth.main import verify_bearer_token
from router.mail import router as mail_router
from settings import MODULES

app = FastAPI(dependencies=[Depends(verify_bearer_token)])
if MODULES.get("mail"):
    app.include_router(mail_router)


@app.get("/", tags=["main"])
async def root():
    return JSONResponse({"message": "Hello World Well"})

