import os
import sys

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from utils.hasher import hash_payload
from utils.payload import get_iso_datettime, make_payload


def get_payload_and_hash():
    github_url = os.environ["GITHUB_SERVER_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    signing_key = os.environ["SIGNING_KEY"]

    repo_url = f"{github_url}/{repo}"
    payload = make_payload(
        ts=get_iso_datettime(),
        name=os.environ.get("NAME", ""),
        email=os.environ.get("EMAIL", ""),
        resume_url=os.environ.get("RESUME_URL", ""),
        repo_url=repo_url,
        run_id=run_id,
    )

    hash = hash_payload(payload, signing_key)

    return (payload, hash)


def send_post():
    (payload, hash) = get_payload_and_hash()
    try:
        API_URL = os.environ.get("API_URL")
        resp = requests.post(
            API_URL,
            json=payload,
            headers={"X-Signature-256": f"sha256={hash}"},
        )
        if resp.status_code != 200:
            print("API returned non 200 response")
            return

        resp_json = resp.json()
        if not resp_json.get("success"):
            print("API did not return success=True")
            return

        receipt = resp_json.get("receipt")
        print(f"Receipt: {receipt}")

    except Exception as e:
        print("Error sending POST:", e)


send_post()
