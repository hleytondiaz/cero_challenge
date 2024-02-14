from fastapi import Header, HTTPException
from typing import Annotated
from config import config

def verify_key(x_api_key: Annotated[str or None, Header()] = None):
    try:
        if config["API_KEY"] != x_api_key:
            raise
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return None