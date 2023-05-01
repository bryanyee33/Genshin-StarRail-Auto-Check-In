import os
import logging
from hoyo_checkin import hoyo_checkin

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)

OS_COOKIE = os.environ.get('OS_COOKIE')

def genshin(cookie_str: str):
    hoyo_checkin(
        "https://hk4e-api-os.mihoyo.com/event/sol",
        "e202102251931481",
        cookie_str,
    )

def starrail(cookie_str: str):
    hoyo_checkin(
        "https://sg-public-api.hoyolab.com/event/luna/os",
        "e202303301540311",
        cookie_str,
    )

genshin(OS_COOKIE)
starrail(OS_COOKIE)
