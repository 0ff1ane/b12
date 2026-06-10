import hashlib
import hmac
import json


def hash_payload(payload: dict[str, str], key: str):
    json_str = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    return hmac.new(bytes(key, "utf-8"), json_str, hashlib.sha256).hexdigest()
