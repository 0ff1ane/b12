import datetime


def make_url(repo, run_id):
    return f"{repo}/actions/runs/{run_id}"


def get_iso_datettime():
    return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_payload(
    ts: str, name: str, email: str, resume_url: str, repo_url: str, run_id: str
) -> dict[str, str]:
    payload = {
        "timestamp": ts,  # get_iso_datettime(),
        "name": name,
        "email": email,
        "resume_link": resume_url,
        "repository_link": repo_url,
        "action_run_link": make_url(repo_url, run_id),
    }
    sorted_payload = dict(sorted(payload.items()))
    return sorted_payload
