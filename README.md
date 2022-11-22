# This project is a Template
_by Friedjof Noweck_

## Structure
- `data/` contains the data of the container
- `env/` contains the environment variables for the container
- `dockerfiles/` contains the Dockerfiles for the container
- `scripts/` contains the scripts for the project

- `docker-compose.yml` contains the configuration for the container
- `setup.sh` prepares the project for the first run

## Container
- Portainer on port 9000
- PHPMyAdmin on port 8080
- MariaDB on port 3306

## Usage
- Clone the project from here
- Run `setup.sh` to prepare the project
- Run `docker compose up -d` to start the container