# Deluge Announce

A script that will announce torrents on a timed interval (CRON).

## Prerequisites

- Python 3.10 or higher
- Docker (if using Docker setup)

## Setup

#### Options for Use

- Docker ([link](https://hub.docker.com/repository/docker/jlw4049/deluge-announce/))

#### Running the Docker Container

To run the Docker container with the appropriate environment variables, use the following command:

```bash
docker run -e "WEB_URL=<your_web_url>" -e "PASSWORD=<your_web_url_password>" -e "CRON_SCHEDULE=0 * * * *" -v "app_data:/app_data"
```

This command will mount the `app_data` volume to persist logs across container restarts.

#### Checking Logs

Outside of Docker, you can view the logs in `./app_data/logs/`.

### Notes

- The `app_data` volume is used for persistent storage.
- If you're running the script outside Docker, the `app_data` folder will be created in your local directory to store logs and the database.
- The **cron_schedule** format follows standard cron syntax for scheduling tasks. For example, `0 * * * *` runs the script every hour.

### Troubleshooting

- **Error Logs**: If something goes wrong, check the logs at `./app_data/logs/` for more details.
