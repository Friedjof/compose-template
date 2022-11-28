#!/bin/bash

# This script is used to delete all the containers, volumes, networks, images and env files

# Delete all containers
# Dialog for deleting all containers
echo "Do you want to delete all containers? (y/n)"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
  docker compose down -v --rmi all --remove-orphans

  # Delete all volumes
  # Dialog for deleting all volumes
  echo "Do you want to delete all volumes? (y/n)"
  read answer
  if [ "$answer" != "${answer#[Yy]}" ] ;then
    docker volume prune -f
  fi

  # Delete all unused volumes
  # Dialog for deleting all not used volumes
  echo "Do you want to delete all not used volumes? (y/n)"
  read answer
  if [ "$answer" != "${answer#[Yy]}" ] ;then
    docker volume prune -f
  fi

  # Delete all unused networks
  # Dialog for deleting all not used networks
  echo "Do you want to delete all not used networks? (y/n)"
  read answer
  if [ "$answer" != "${answer#[Yy]}" ] ;then
    docker network prune -f
  fi

  # Delete all unused images
  # Dialog for deleting all not used images
  echo "Do you want to delete all not used images? (y/n)"
  read answer
  if [ "$answer" != "${answer#[Yy]}" ] ;then
    docker image prune -f
  fi
fi

# Delete all env files
# Dialog for deleting all env files
echo "Do you want to delete all env files? (y/n)"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
  rm -rf env/*.env
fi

# Delete the data in the data folder
# Dialog for deleting the data in the data folder
echo "Do you want to delete the data in the data folder? (y/n)"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
  sudo rm -rf data/*
  touch data/.placeholder
fi