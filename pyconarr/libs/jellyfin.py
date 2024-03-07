import requests
from fastapi import HTTPException
from pyconarr.libs.config import config, get_version
from pyconarr.libs.docs import Login


def valid_user(login: Login) -> bool:
    headers = {
        "Content-Type": "application/json",
        "x-emby-authorization": 'MediaBrowser , Client="Conarr", Device="Pyconarr", DeviceId="Conarr", Version="'
        + get_version()
        + '", Token="'
        + config["jellyfin"]["token"]
        + '"',
    }
    try:
        r = requests.get(
            config["jellyfin"]["url"] + "/Users/" + login.Username,
            headers=headers,
            timeout=10,
        )
    except requests.exceptions.ReadTimeout:
        raise HTTPException(status_code=502, detail="Failed to contact jellyfin server")
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False
    else:
        raise HTTPException(status_code=502, detail="Failed to contact jellyfin server")
