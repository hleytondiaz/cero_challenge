from fastapi import Header, HTTPException
from typing import Annotated
from config import config

"""
    This file contains all the necessary middlewares. The first one allows verifying the existence of an x-api-key for authorization of the request from the client making the query.
"""

def verify_key(x_api_key: Annotated[str or None, Header()] = None):
    try:
        if config["API_KEY"] != x_api_key:
            raise
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return None