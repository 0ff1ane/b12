import os

from dotenv import load_dotenv

from utils.hasher import hash_payload


def test_payload_hash():
    load_dotenv()
    payload = {
        "action_run_link": "https://link-to-github-or-another-forge.example.com/your/repository/actions/runs/run_id",
        "email": "you@example.com",
        "name": "Your name",
        "repository_link": "https://link-to-github-or-other-forge.example.com/your/repository",
        "resume_link": "https://pdf-or-html-or-linkedin.example.com",
        "timestamp": "2026-01-06T16:59:37.571Z",
    }
    signing_key = os.getenv("SIGNING_KEY")
    assert signing_key is not None
    hash = hash_payload(payload, signing_key)
    assert hash == "c5db257a56e3c258ec1162459c9a295280871269f4cf70146d2c9f1b52671d45"
