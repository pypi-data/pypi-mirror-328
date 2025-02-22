import os
from dotenv import load_dotenv
from pathlib import Path


class Config:
    in_docker = True if os.environ.get("IN_DOCKER") == "true" else False

    if in_docker:
        app_data = Path("/app_data")
    else:
        load_dotenv()  # pyright: ignore [reportUnusedCallResult]
        app_data = Path(Path.cwd() / "app_data")

    log_path: Path = Path(app_data / "logs")

    app_data.mkdir(exist_ok=True, parents=True)
    log_path.mkdir(exist_ok=True, parents=True)

    web_url: str = os.environ.get("WEB_URL", "")
    password: str = os.environ.get("PASSWORD", "")
    cron_schedule: str | None = os.environ.get("CRON_SCHEDULE", "0 * * * *")
    skip_re_announce: list[str] = (
        str(os.environ.get("SKIP_RE_ANNOUNCE", ["too many requests"]))
        .lower()
        .split("|")
    )
    force_re_announce: list[str] = (
        str(os.environ.get("FORCE_RE_ANNOUNCE", ["warning|error"])).lower().split("|")
    )
    force_re_announce_new_torrents_interval: int = int(
        os.environ.get("FORCE_RE_ANNOUNCE_NEW_TORRENTS_INTERVAL", 0)
    )
    force_re_announce_new_torrents_max_age: int = int(
        os.environ.get("FORCE_RE_ANNOUNCE_NEW_TORRENTS_MAX_AGE", 300)
    )
    log_level: str | None = os.environ.get("LOG_LEVEL")
