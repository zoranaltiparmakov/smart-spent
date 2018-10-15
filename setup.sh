#!/bin/bash

if [ "$1" = "createvm" ]; then
  # create new virtualbox docker machine
  docker-machine create -d virtualbox moneyspent-dev
  # update environment vars, in order docker client to talks to docker engine on moneyspent-dev VM
  eval $(docker-machine env moneyspent-dev)
elif [ "$1" = "update" ] || [ "$1" = "" ]; then
  docker-compose build
  docker-compose up -d
elif [ "$1" = "makemigrations" ]; then
  docker-compose run web /usr/local/bin/python3 manage.py makemigrations
elif [ "$1" = "migrate" ]; then
  docker-compose run web /usr/local/bin/python3 manage.py migrate
fi