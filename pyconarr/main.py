import logging

from pyconarr.libs.config import config
from pyconarr.libs.route import app
from pyctuator.pyctuator import Pyctuator

logging.info("Starting app " + app.title)
logging.debug("Jellyfin server URL : " + config["jellyfin"]["url"])


Pyctuator(
    app,
    config["pyctuator"]["name"],
    app_url=config["pyctuator"]["app_url"],
    pyctuator_endpoint_url=config["pyctuator"]["endpoint_url"],
    registration_url=config["pyctuator"]["registration_url"],
)
