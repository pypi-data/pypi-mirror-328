import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from deluge_web_client import DelugeWebClient

from .logger import init_logger
from .config import Config
from .enums import LogLevel

# inspiration from https://github.com/kenstir/deluge-reannounce/blob/develop/deluge_reannounce


class Announcer:
    def __init__(
        self,
        web_url: str | None = None,
        password: str | None = None,
        cron_schedule: str | None = None,
        skip_re_announce: list[str] = ["too many requests"],
        force_re_announce: list[str] = ["warning", "error"],
        log_level: LogLevel = LogLevel.INFO,
    ) -> None:
        """
        Re-announcer for Deluge.

        Attributes:
            web_url (str | None): Web URL for the announcement Deluge service.
            password (str | None): Web URL password for the Deluge service.
            cron_schedule (str | None): A cron-style schedule string defining when announcements should occur.
            skip_re_announce (list[str]): A list of status messages that should prevent re-announcement.
            force_re_announce (list[str]): A list of status messages that should always trigger a re-announcement.
            log_level (LogLevel): Level of logging to use, defaults to INFO.
        """
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
            self.config.skip_re_announce = skip_re_announce
            self.config.force_re_announce = force_re_announce

        # if running in docker and log level was passed we'll use it
        if self.config.in_docker and self.config.log_level:
            log_level = LogLevel(self.config.log_level)

        self.logger = init_logger(self.config.log_path, LogLevel(log_level))
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
        validate_field(self.config.skip_re_announce, "Skip re-announce", list)
        validate_field(self.config.force_re_announce, "Force re-announce", list)

    def init_client(self) -> DelugeWebClient:
        client = DelugeWebClient(self.config.web_url, self.config.password)
        client.login()
        return client

    def parse_torrents(self) -> None:
        self.logger.info("Parsing torrents to re-announce.")

        torrents_status = self.client.get_torrents_status()
        if torrents_status.error:
            self.logger.warning(f"There was an error ({torrents_status.error}).")
            return

        if not torrents_status.result:
            self.logger.info("No torrents detected.")
            return

        if isinstance(torrents_status.result, dict):
            # collect trackers to force re-announce
            torrents_to_re_announce = []
            for torrent_hash, torrent_data in torrents_status.result.items():
                if self._check_re_announce(torrent_data):
                    torrents_to_re_announce.append(torrent_hash)

            # force re-announce trackers
            if not torrents_to_re_announce:
                self.logger.info("No torrents to re-announce.")
            if torrents_to_re_announce:
                self.logger.info(
                    f"Re-announcing {len(torrents_to_re_announce)} torrent(s)."
                )
                self._re_announce(torrents_to_re_announce)
                self.logger.info(
                    f"Re-announcing {len(torrents_to_re_announce)} torrent(s) completed."
                )

        self.logger.info("Done parsing torrents.")

    def _check_re_announce(self, data: dict) -> bool:
        paused = data.get("paused")
        if paused is True:
            return False

        status = data.get("tracker_status", "")
        status_lowered = status.lower()
        t_hash = data.get("hash")
        name = data.get("name")

        # iterate skip re announce strings
        for skip_str in self.config.skip_re_announce:
            if skip_str and skip_str in status_lowered:
                self.logger.info(
                    f"Skipping torrent, reason={skip_str}, hash={t_hash}, name={name}."
                )
                return False

        # iterate force re announce strings
        for force_str in self.config.force_re_announce:
            if force_str and force_str in status_lowered:
                self.logger.info(
                    f"Adding torrent to force re-announce, status={status}, hash={t_hash}, name={name}."
                )
                return True

        # all other conditions will return False
        self.logger.debug(
            f"Condition not met for torrent, status={status}, hash={t_hash}, name={name}."
        )
        return False

    def _re_announce(self, torrents: list[str]) -> None:
        payload = {
            "method": "core.force_reannounce",
            "params": [torrents],
            "id": self.client.ID + 1,
        }
        self.client.execute_call(payload=payload)

    def run(self) -> None:
        """Run the script once (for user-based execution)."""
        self.parse_torrents()

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
        self.parse_torrents()

        scheduler = BackgroundScheduler()
        cron_schedule = CronTrigger.from_crontab(self.config.cron_schedule)
        scheduler.add_job(self.parse_torrents, cron_schedule)
        scheduler.start()

        # keep main thread alive
        asyncio.run(self._keep_alive(scheduler))
