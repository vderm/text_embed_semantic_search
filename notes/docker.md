---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Docker
---

Private namespaces = containers

+ Tutorial: <https://www.youtube.com/watch?v=YFl2mCHdv24>
+ Install instructions: <https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>
+ Verify installation >>> sudo docker run hello-world
+ Docker daemon: <https://docs.docker.com/config/daemon/>
+ Minimal docker containers for Python applications:
  <https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3>
+ Docker run command with examples: <https://linuxize.com/post/docker-run-command/>
+ Docker for data science: <https://valohai.com/blog/docker-for-data-science/>

# Why Docker?

1. Same environment
2. Sandbox projects
3. It just works!

The 'dockerfile' is used to /build/ the /image/.

# Build on top of existing Docker images
<https://hub.docker.com>

```
FROM php:7.0-apache  <-- which one to use from the hub
COPY src/ /var/www/html <-- copy files into the docker
EXPOSE 80  <-- expose a port
```

Dockers are built on top of other dockers.

PHP is built on top of debian which is built on top of ...

# Building it
>>>
>>> docker build -t hello-world .

cd where the dockerfile is located
"hello-world" is the name we're giving it

A container builds the image, copies the files, and that's that.
If you update the files, the container needs to be rebuilt.
You could instead share volumes.

# Run it
>>>
>>> docker run -p 80:80 hello-world

-p = host:container port

# Sharing/mounting volumes
>>>
>>> docker run -p 80:80 -v /path/on/host/:/path/on/container/ hello-world

# Shutdown

Make the container do one thing.
If the main container function dies, the container stops!
So make sure nothing critical is running on the side, so it's easiest to simply
use a container for one specific thing.

# Docker compose [keeps changing]

docker build
docker run
docker ...
into a nice file

put this at a higher level:

docker-compose.yaml

``` yaml
version: '3'

services:
  product-service:
    build: ./product
    volumes:
      - ./product:/usr/src/app
    port:
      - 5001:80

  website:
    image: php:apache
    volumes:
      - ./website:/var/www/html
    port:
      - 5000:80
    depends_on:
      - product_service
```

>>> docker-compose up

docker compose makes a network between every container it is running

depends_on: another container

# Detached mode: run in background
>>>
>>> docker-compose up -d

>>> docker ps
to see what's running

>>> docker-compose stop

# Trouble running it

See: <https://stackoverflow.com/questions/43537790/docker-fails-to-start-due-to-volume-store-metadata-database-timeout>
and: <https://github.com/moby/moby/issues/22507>

ps axf | grep docker | grep -v grep | awk '{print "kill -9 " $1}' | sudo sh

sudo systemctl start docker

# SSH into a container; running a command
>>>
>>> docker ps
to get a list of all running containers

>>> docker exec -it <container name> <command>
>>> docker exec -it <container name> /bin/bash

>>> docker run -it <container name> /bin/bash

# List all
>>>
>>> docker container ls --all

# Remove
>>>
>>> docker container rm <id>

Stop and Delete all the containers:
>>> docker stop `docker ps -q`
>>> docker rm `docker ps -aq`

# DataKit

1. copy git files (DataKit+KitUtils) to docker_test folder
2. remove extra files
3. build container: `sudo docker build -t datakit .`
4. run container: `sudo docker run -it -v $HOME/Toolkit_Merged/DataKit/Examples/:$HOME/Examples/ datakit /bin/bash`

# Makefile

source: <https://github.com/ibpsa/project1-boptest/blob/master/makefile>

``` bash
IMG_NAME=boptest_${TESTCASE}

COMMAND_RUN=docker run \
   --name ${IMG_NAME} \
   --rm \
    -it \
   -p 127.0.0.1:5000:5000

build:
 docker build --build-arg testcase=${TESTCASE} --no-cache --rm -t ${IMG_NAME} .

remove-image:
 docker rmi ${IMG_NAME}

run:
 $(COMMAND_RUN) --detach=false ${IMG_NAME} /bin/bash -c "python restapi.py && bash"

run-detached:
 $(COMMAND_RUN) --detach=true ${IMG_NAME} /bin/bash -c "python restapi.py && bash"

stop:
 docker stop ${IMG_NAME}
```

# Maroun's Dockerfile

``` dockerfile
FROM python:3.9

# set workdirectory as code
WORKDIR /code

# create a folder for ssh
RUN mkdir /root/.ssh && chmod 400  /root/.ssh
# add git server to known_hosts
RUN ssh-keyscan git.brainboxai.net >> ~/.ssh/known_hosts

# copy requirement to docker image
COPY ./requirements.txt /code/requirements.txt

# install packages
RUN --mount=type=ssh pip install git+ssh://root@git.brainboxai.net/Toolkit/DataKit.git
RUN --mount=type=ssh pip install git+ssh://root@git.brainboxai.net/Toolkit/KitUtils.git
RUN --mount=type=ssh pip install git+ssh://root@git.brainboxai.net/Toolkit/ControlKit.git
# RUN --mount=type=ssh pip install git+ssh://root@git.brainboxai.net/Toolkit/MLKit.git
RUN --mount=type=ssh pip install -r requirements.txt

# copy project code to docker image
COPY ./assets /code/missioncontrol/assets
COPY ./stations /code/missioncontrol/stations
COPY launch_mission_control.py /code/missioncontrol/launch_mission_control.py

# setting python environment variable to the api workspace folder
ENV PYTHONPATH /code/missioncontrol

# start server
CMD ["streamlit", "run", "/code/missioncontrol/launch_mission_control.py", "--server.address", "0.0.0.0", "--server.port", "8505"]

# ---------------------------------------------------------------------
# Docker Commands
# ---------------------------------------------------------------------

# =======================
# Docker Build Commands
# =======================

# To build the image run in the same path of "Dockerfile" (default="location of your ssh private key")
# or specify the location with "-f dockerfilepath"

# Windows (Make sure Build Kit is enabled in docker configuration)
# -------
# docker build  --ssh default=c:/users/username/.ssh/id_rsa -t missioncontrol_image .

# Linux (and buildkit is not enabled in Docker)
# -------
# DOCKER_BUILDKIT=1 docker build  --ssh default=/home/$USER/.ssh/id_rsa -t missioncontrol_image .

# If you don't want to use the cached libraries add --no-cache

# Windows
# -------
# docker build  --no-cache --ssh default=c:/users/username/.ssh/id_rsa -t missioncontrol_image .

# Linux
# -------
# DOCKER_BUILDKIT=1 docker build --no-cache --ssh default=/home/$USER/.ssh/id_rsa -t missioncontrol_image .

# =======================
# Upload Image to Server
# =======================

# To upload Image to remote server
# docker save missioncontrol_image | ssh -C user@my.remote.host.com docker load

# =======================
# Run Comainter
# =======================

# To create and run container
# docker run -d --name missioncontrol_container -p 8000:8000 missioncontrol_image

# =======================
# Docker-Compose Commands
# =======================
# To run as service (After configuring docker-compose.yml) --service-ports exposes the ports
# docker-compose run --service-ports missioncontrol_service

# Or to run all services in one shot
# docker-compose up -d

# ===================
# Monitoring Commands
# ===================

# To list containers (with IDs)
# -------------------
# docker ps

# To list compose services
# ------------------------
# docker-compose ps

# To open container shell
# ------------------------
# docker exec -it container_id /bin/bash

# To open container logs (continous)
# ----------------------------------
# docker logs -f container_id

# Stop a Container
# ----------------------------------
# docker kill container_id

# Remove a Container
# ----------------------------------
# docker rm container_id
```
