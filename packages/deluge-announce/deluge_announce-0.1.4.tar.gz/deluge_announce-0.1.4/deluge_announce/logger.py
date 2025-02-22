import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from .enums import LogLevel


def init_logger(
    log_directory: Path, log_level: LogLevel = LogLevel.INFO
) -> logging.Logger:
    logger = logging.getLogger("deluge_announce")
    logger.setLevel(log_level.value)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        str(log_directory / "deluge_announce.log"),
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
