import os
import logging
from hoyo_checkin import hoyo_checkin

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)

OS_COOKIE = os.environ.get('OS_COOKIE')

#genshin
hoyo_checkin(
    "https://hk4e-api-os.mihoyo.com/event/sol",
    "e202102251931481",
    OS_COOKIE,
)

#star rail
hoyo_checkin(
    "https://sg-public-api.hoyolab.com/event/luna/os",
    "e202303301540311",
    OS_COOKIE,
)

