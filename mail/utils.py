import os
from fastapi import HTTPException


async def check_settings():
    mail_dir = os.path.dirname(os.path.abspath(__file__))
    print(mail_dir)
    local_settings_path = os.path.join("/local_settings.py")
    module_configured = os.path.exists(local_settings_path)
    if not module_configured:
        raise HTTPException(status_code=500, detail="module mail is not configured")
