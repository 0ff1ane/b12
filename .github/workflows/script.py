import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from utils.hasher import hash_payload
from utils.payload import get_iso_datettime, make_payload


def send_post():
    github_url = os.environ["GITHUB_SERVER_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    signing_key = os.environ["SIGNING_KEY"]

    repo_url = f"{github_url}/{repo}"

    print(f"repo_url: {repo_url}")
    print(f"run_id: {run_id}")
    print(f"signing_key length: {len(signing_key)}")

    payload = make_payload(
        ts=get_iso_datettime(),
        name=os.environ.get("NAME", ""),
        email=os.environ.get("EMAIL", ""),
        resume_url=os.environ.get("RESUME_URL", ""),
        repo_url=repo_url,
        run_id=run_id,
    )

    print(f"payload: {payload}")

    hash = hash_payload(payload, signing_key)

    print(f"hash: {hash}")


send_post()
