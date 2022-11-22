#!/bin/bash

# This script is used to setup the environment for the

python3 scripts/volumes.py docker-compose.yaml
python3 scripts/environments.py docker-compose.yaml

# Dialog for starting the containers
echo "Do you want to start the containers? (y/n)"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    docker compose up -d
fi