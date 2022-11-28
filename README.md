# Reverse-Proxy - Compose template
_by Friedjof Noweck_

## About
This is a template project for private projects.
Do you have also the problem that you have to create everything from scratch for every new docker project?
And you always need the same services as a database or portainer?
Then this template is the right thing for you!
It contains a docker-compose file with the three most important services for every project.
As bonus, there is also a setup script for the project. So you can start your project immediately.

**Feel free to fork this project and adapt it to your needs.**
**If you have any questions or suggestions, feel free to contact me or create an issue.**

## Container
- NGINX reverse proxy manager on http://172.0.11.5:81
  - default login: `admin@example.com` `changeme`
- Portainer on http://172.0.11.4:9000
- PHPMyAdmin on http://172.0.11.3
- MariaDB on port 3306

## Structure
- `data/` contains the data of the container
- `env/` contains the environment variables for the container
- `dockerfiles/` contains the Dockerfiles for the container
- `scripts/` contains the scripts for the project

- `docker-compose.yml` contains the configuration for the container
- `setup.sh` prepares the project for the first run

## Usage
- Clone the project from here
- Run `setup.sh` to prepare the project
  1. The script will create the defined volumes from the `docker-compose.yml`
  2. The script will compare the env-templates with the env-files and create the missing ones
  3. After this two steps you will be asked for starting the container

## Delete the project data
The script `delete-all.sh` will delete container, volumes, networks, images, data and env-files, but you will be asked for every step.

## Network
- The network has a subnet of `172.0.11.0/29`
- The network has a gateway of `172.0.11.1`