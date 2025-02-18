import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from deluge_web_client import DelugeWebClient

from .logger import init_logger
from .config import Config

# inspiration from https://github.com/kenstir/deluge-reannounce/blob/develop/deluge_reannounce


class Announcer:
    def __init__(
        self,
        web_url: str | None = None,
        password: str | None = None,
        cron_schedule: str | None = None,
    ) -> None:
        self.config = Config()

        # update config only if not running in Docker and arguments are provided
        if not self.config.in_docker:
            if not web_url or not password or not cron_schedule:
                raise ValueError(
                    "You must provide all arguments if not running in docker."
                )
            self.config.cron_schedule = cron_schedule
            self.config.web_url = web_url
            self.config.password = password

        self.logger = init_logger(self.config.log_path)
        self.validate_config()

        # initialize client
        self.client = self.init_client()

    def validate_config(self) -> None:
        def validate_field(value, field_name, expected_type):
            if value is None:
                raise AttributeError(f"{field_name} is required.")
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"{field_name} should be of type {expected_type.__name__}."
                )

        validate_field(self.config.web_url, "Web URL", str)
        validate_field(self.config.password, "Password", str)
        validate_field(self.config.cron_schedule, "Cron schedule", str)

    def init_client(self) -> DelugeWebClient:
        client = DelugeWebClient(self.config.web_url, self.config.password)
        client.login()
        return client

    def iterate_torrents(self) -> None:
        self.logger.info("Iterating torrents.")

        torrents_status = self.client.get_torrents_status()
        if torrents_status.error:
            self.logger.warning(f"There was an error ({torrents_status.error}).")
            return

        if not torrents_status.result:
            self.logger.info("No torrents.")
            return

        if isinstance(torrents_status.result, dict):
            for torrent_hash, torrent_data in torrents_status.result.items():
                status = torrent_data.get("tracker_status", "")
                self._re_announce(torrent_hash, status)

        self.logger.info("Done iterating torrents.")

    def _re_announce(self, t_hash: str, status: str) -> None:
        status_lowered = status.lower()
        if "too many requests" in status_lowered:
            self.logger.info(f"Too many requests for torrent hash {t_hash}.")
        elif status_lowered in ("warning", "error"):
            self.logger.info(
                f"Force re-announcing torrent {t_hash} (status: {status})."
            )
            payload = {
                "method": "core.force_reannounce",
                "params": [[t_hash]],
                "id": self.client.ID + 1,
            }
            self.client.execute_call(payload=payload)
            self.logger.info(f"Force re-announcing torrent completed {t_hash}.")
        else:
            # could do no seeds but for now we'll do nothing
            pass

    def run(self) -> None:
        """Run the script once (for user-based execution)."""
        self.iterate_torrents()

    async def _keep_alive(self, scheduler: BackgroundScheduler):
        try:
            while True:
                await asyncio.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()

    def run_forever(self) -> None:
        """Run the script using APScheduler (for scheduler-based execution)."""
        self.logger.info(
            f"DelugeAnnounce initialized (CRON schedule: {self.config.cron_schedule})."
        )
        self.iterate_torrents()

        scheduler = BackgroundScheduler()
        cron_schedule = CronTrigger.from_crontab(self.config.cron_schedule)
        scheduler.add_job(self.iterate_torrents, cron_schedule)
        scheduler.start()

        # keep main thread alive
        asyncio.run(self._keep_alive(scheduler))
