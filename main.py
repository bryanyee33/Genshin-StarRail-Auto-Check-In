import os
import logging
from hoyo_checkin import game_perform_checkin

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)

DEFAULT_LANGUAGE = "en-us"
OS_COOKIE = os.environ.get('OS_COOKIE').split("#")
games = None

if "GAME_CHOICE" in os.environ:
    games = [s.split(",") for s in os.environ["GAME_CHOICE"].split("#")]
else:
    games = [["genshin", "starrail"]] * len(OS_COOKIE) # honkai and themis also available

for i, cookie in enumerate(OS_COOKIE):
    for game in games[i]:
        game_perform_checkin(
            i + 1,
            game,
            cookie,
            DEFAULT_LANGUAGE
        )

