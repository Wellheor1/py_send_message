from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.auth.main import verify_bearer_token
from app.database import SessionLocal
from app.router.mail import router as mail_router
from app.settings import MODULES
from app.mail.utils import check_settings as mail_check_settings
from app.slog.models import Slog
from app.utils import check_settings as main_check_settings

app = FastAPI(dependencies=[Depends(verify_bearer_token)])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


main_check_settings()
if MODULES.get("mail"):
    app.include_router(mail_router)
    mail_check_settings()


@app.get("/", tags=["main"])
async def root(db: Session = Depends(get_db)):
    all_log = db.query(Slog).all()
    print(all_log)
    return JSONResponse({"message": "Hello World Well"})
