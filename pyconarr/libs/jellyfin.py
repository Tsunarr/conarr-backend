import requests
from pyconarr.libs.docs import Login
from pyconarr.libs.config import config
from fastapi import HTTPException

def valid_user(login: Login) -> bool:
    try:
        r = requests.get(
            config["jellyfin"]["url"] + "/Users/" + login.Username,
            timeout=10,)
    except requests.exceptions.ReadTimeout:
        raise HTTPException(status_code=502, detail="Failed to contact jellyfin server")
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False
    else:
        raise HTTPException(
            status_code=502, detail="Failed to contact jellyfin server"
        )
        



