from utils.payload import make_payload


def test_payload():
    payload = make_payload(
        ts="2026-01-06T16:59:37.571Z",
        name="Your name",
        email="you@example.com",
        resume_url="https://pdf-or-html-or-linkedin.example.com",
        repo_url="https://link-to-github-or-other-forge.example.com/your/repository",
        run_id="run_id",
    )

    assert payload["email"] == "you@example.com"
    assert (
        payload["action_run_link"]
        == "https://link-to-github-or-other-forge.example.com/your/repository/actions/runs/run_id"
    )
