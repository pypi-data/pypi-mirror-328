# Deluge Announce

A script that will announce torrents on a timed interval (CRON).

## Prerequisites

- Python 3.10 or higher
- Docker (if using Docker setup)

## Setup

#### Options for Use

- Docker ([link](https://hub.docker.com/repository/docker/jlw4049/deluge-announce/))
- Package ([link](https://pypi.org/project/deluge-announce/))

#### Running the Docker Container

To run the Docker container with the appropriate environment variables, use the following command:

```bash
docker run -e "WEB_URL=<your_web_url>" -e "PASSWORD=<your_web_url_password>" -e "CRON_SCHEDULE=0 * * * *" -e "SKIP_RE_ANNOUNCE=too many requests" -e "FORCE_RE_ANNOUNCE=warning|error" -e "LOG_LEVEL=Info" -v "app_data:/app_data"
```

`SKIP_RE_ANNOUNCE` and `SKIP_RE_ANNOUNCE` expects **pipe operator |** separated strings. i.e. `SKIP_RE_ANNOUNCE=reason1|reason2`

`LOG_LEVEL` defaults to **Info**. It can be any of **Debug**, **Info**, **Warning**, **Error**, or **Critical**. _(Case insensitive)_

This command will mount the `app_data` volume to persist logs across container restarts.

#### Running the Script as a Package

1. Install the package

```bash
poetry add deluge-announce
# or
pip install deluge-announce
```

2. Use in your Python code

```python
from deluge_announce import Announcer
announcer = Announcer(
    web_url="https://yourweburl.com/",
    password="YOUR PASSWORD",
    cron_schedule="0 * * * *", # runs every hour
    skip_re_announce=["too many requests"], # defaults
    force_re_announce=["warning", "error"]  # defaults
    log_level="Info", # defaults to INFO from enum LogLevel. Strings are also accepted "Debug", "Info", "Warning", "Error", or "Critical". (Case insensitive)
)

# Run the notifier once
announcer.run()

# Or run continuously as scheduled by cron
announcer.run_forever()
```

#### Checking Logs

Outside of Docker, you can view the logs in `./app_data/logs/`.

### Notes

- The `app_data` volume is used for persistent storage.
- If you're running the script outside Docker, the `app_data` folder will be created in your local directory to store logs and the database.
- The **cron_schedule** format follows standard cron syntax for scheduling tasks. For example, `0 * * * *` runs the script every hour.

### Troubleshooting

- **Error Logs**: If something goes wrong, check the logs at `./app_data/logs/` for more details.
