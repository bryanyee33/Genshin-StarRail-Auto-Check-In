import os
import logging
from hoyo_checkin import game_perform_checkin

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)

DEFAULT_LANGUAGE = "en-us"
OS_COOKIE = os.environ.get('OS_COOKIE')

games = ["genshin", "starrail"] # honkai and themis also available

for i, cookie in enumerate(OS_COOKIE.split(","), start = 1):
    for game in games:
        game_perform_checkin(
            i,
            game,
            cookie,
            DEFAULT_LANGUAGE
        )

