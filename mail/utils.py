import os
from fastapi import HTTPException


async def check_settings():
    local_settings_path = "./local_settings.py"
    module_configured = os.path.exists(local_settings_path)
    if not module_configured:
        raise HTTPException(status_code=500, detail="module mail is not configured")
