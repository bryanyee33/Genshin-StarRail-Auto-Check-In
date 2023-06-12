import json
import logging

import requests
from requests import HTTPError, Response

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/74.0.3729.169 Safari/537.36"
)


def http_get(url: str, max_retries: int = 2, **kwargs) -> Response:
    return http_request("get", url, max_retries, **kwargs)


def http_get_json(url: str, max_retries: int = 2, **kwargs):
    resp = http_get(url, max_retries, **kwargs)
    data = resp.text
    return json.loads(data)


def http_post(url: str, max_retries: int = 2, **kwargs) -> Response:
    return http_request("post", url, max_retries, **kwargs)


def http_post_json(url: str, max_retries: int = 2, **kwargs):
    resp = http_post(url, max_retries, **kwargs)
    data = resp.text
    return json.loads(data)


def http_request(
        method: str,
        url: str,
        max_retries: int = 2,
        **kwargs,
) -> Response:
    for i in range(max_retries + 1):
        try:
            logging.debug(f"{method.upper()} {url}, REQ: {i + 1}/{max_retries}")
            session = requests.Session()
            session.headers["User-Agent"] = USER_AGENT
            resp = session.request(method, url, **kwargs)

            text = resp.text
            if resp.headers.get("Content-Type", "") == "application/json":
                text = json.loads(text)
            logging.debug(f"Response: {resp.status_code}\n\n{text}\n")
        except HTTPError as e:
            logging.error(f"HTTP error: {e}, REQ: {i + 1}/{max_retries}")
        except KeyError as e:
            logging.error(f"Wrong response: {e}, REQ: {i + 1}/{max_retries}")
        else:
            return resp
    msg = f"All {max_retries} HTTP requests have failed"
    raise Exception(msg)
