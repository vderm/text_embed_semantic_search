---
author: Vasken Dermardiros
categories: note
tags:
- programming
- training
title: Udemy Course Docker
---


[[containerization]], [[docker]], [[dramble]]

Title: Docker for the Absolute Beginnger - Hands On - DevOps

instructor part of kodekloud.com

# Section 1: Introduction

## Why?

Setting up envionments led to the "Matrix from Hell" because of compatibility issues and lack of guarantee of having a common development environment.

![](../attachments/2021-08-22-10-22-26.png)

Containers are completely isolated environment but share the same OS kernel.
OS kernel responsible to interact with the low level hardware.

## Container vs VM

Container advantage: run apps on an OS in an isolated manner. Much more lightweight compared to a VM.

![](../attachments/2021-08-22-10-27-01.png)

VM advantage: completely different.

## Where to find containers?

Most large companies have prepared their product images in dockerhub to get it up and running.

> docker run ansible
> docker run mongo db
> docker run redis

Docker containers are running instances of a docker image (template).

## Install on Ubuntu

Instructions: <https://docs.docker.com/engine/install/ubuntu/>

Going with 'stable' release. There's also a convenience script at the bottom to do this in an easier way.

``` sh
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

# sudo apt-get update & upgrade to upgrade docker to latest

# verify if everything worked:
sudo docker run hello-world
```

> sudo docker run docker/whalesay cowsay Hello-World!

```
Unable to find image 'docker/whalesay:latest' locally
latest: Pulling from docker/whalesay
Image docker.io/docker/whalesay:latest uses outdated schema1 manifest format. Please upgrade to a schema2 image for better future compatibility. More information at https://docs.docker.com/registry/spec/deprecated-schema-v1/
e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
00bf65475aba: Pull complete
c57b6bcc83e3: Pull complete
8978f6879e2f: Pull complete
8eed3712d2cf: Pull complete
Digest: sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Status: Downloaded newer image for docker/whalesay:latest
 ______________
< Hello-World! >
 --------------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/
```

# Section 2: Docker Commands

## Useful functions

+ `run`: starts a container; fetches image if not on local drive
+ `run -d`: detatched
+ `run -it`: auto-log in
+ `ps`: list live containers
+ `ps -a`: list all containers
+ `stop <name>`: stop container <name>
+ `rm`: remove container permanently
+ `images`: see list of images
+ `rmi`: remove image permanently --> first need to stop and remove containers to run this
+ `pull`: download image but don't run the image
+ `exec <container id> <command>`: run <command> in <container id> (/bin/bash)
+ `docker build -t <name> .`: build docker image from same directory
+ `docker run -dp <host>:<container> getting-started`
+ `docker run --rm -it --entrypoint bash <image name>`

containers are designed to run a specific task and then be killed/exits.

## Append a command

`docker run ubuntu sleep 5`

## Attached / Detached modes

+ `docker run kodekloud/simple-webapp` will run in attached mode
+ `docker run -d kodekloud/simple-webapp` will run in detached mode

to attach on a running instance:

+ `docker attach <name/id>`: provide <name> or first few characters of the <id>

## Demo

:)

# Section 3: Docker Run

+ `docker run redis`: will fetch latest
+ `docker run redis:4.0`: fetch v4.0

docker doesn't "listen" to stdin, runs in non-interactive mode, need to map it!

+ `docker run -i <image>`: interactive mode
+ `docker run -it <image>`: interactive mode and attached to terminal
+ `docker run -p <external out>:<internal docker>`: port mapping

![Port mapping](../attachments/2021-08-28-08-20-05.png)

+ docker is not persistent -> if image is killed, data is gone!

+ `docker run -v <external dir>:<internal dir> mysql`: mount a folder inside a container

![Volume mapping](../attachments/2021-08-28-08-23-12.png)

+ `docker inspect <container id/name>`: returns JSON-ed info of container
+ `docker logs <container id/name>`: container logs
+ `docker attach <container id/name>`: attach

## Run Jenkins

+ It's a webserver...

You can get to it through the docker host, otherwise you need to port forward.

# Section 4: Docker Images

![Creating a docker image](../attachments/2021-08-28-09-13-29.png)

All dockerfiles must start with the `FROM` keyword.

``` dockerfile
FROM Ubuntu
RUN apt-get update && apt-get -u install python
RUN pip install flask flask-mysql
COPY . /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

`ENTRYPOINT` is what will be run when the container is started.

docker stores each line from dockerfile as a layer

![](../attachments/2021-08-28-09-16-32.png)

`docker history <image name>` to see how it's built

Run a container named blue-app using image kodekloud/simple-webapp and set the environment variable APP_COLOR to blue. Make the application available on port 38282 on the host. The application listens on port 8080.

`docker run -p 38282:8080 --name blue-app -e APP_COLOR=blue -d kodekloud/simple-webapp`

To know the env field from within a mysql-db container, run `docker exec -it mysql-db env`

# Section 5: Docker Compose

Using a docker-compose.yaml file to manage the application stack: version of python, version of mysql, etc.

![Sample application: voting](../attachments/2021-08-28-13-21-07.png)

![Sample application](../attachments/2021-08-28-13-22-45.png)

Important to name the containers. Start with data layer.

![Docker run all apps](../attachments/2021-08-28-13-26-23.png)

Need to link them together next! Because there could be many Redis instances running.

![docker run --links](../attachments/2021-08-28-13-34-13.png)

Links is deprecated though...

## Docker-compose

``` yaml
# docker-compose.yaml [version 1]
redis:
  image: redis
db:
  image: postgres:9.4
vote:
  image: voting-app  # `build: ./vote` if the image isn't already built
  ports:
    - 5000:80
  links:
    - redis
result:
  image: result-app
  ports:
    - 5001:80
  links:
    - db  # equivalent to db:db
worker:
  image: worker
  links:
    - redis
    - db
```

+ `docker-compose up`: bring up the stack, assumes images are already built

## Docker-compose v2

``` yaml
version: 2
services:
  redis:
    image: redis
  db:
    image: postgres:9.4
  vote:
    image: voting-app  # `build: ./vote` if the image isn't already built
    ports:
      - 5000:80
    depends_on:
      - redis
```

docker-compose 2 builds a bridge network between all containers automatically.

## Docker-compose v3

``` yaml
version: 3
services:
  redis:
    image: redis
  db:
    image: postgres:9.4
  vote:
    image: voting-app  # `build: ./vote` if the image isn't already built
    ports:
      - 5000:80
    depends_on:
      - redis
```

Support for docker swarm and docker stacks.

## Networks: front-end, back-end

![Front-end, back-end networks](../attachments/2021-08-28-13-45-05.png)

``` yaml
version: 2
services:
  redis:
    image: redis
    networks:
     - back-end
  db:
    image: postgres:9.4
    networks:
     - back-end
  vote:
    image: voting-app  # `build: ./vote` if the image isn't already built
    networks:
     - front-end
     - back-end
  result:
    image: result
    networks:
     - front-end
     - back-end
networks:
  front-end:
  back-end:
```

# Section 6: Docker Registry

Central repo of all docker images.

> image: nginx

is actually:
> image: docker.io/nginx/nginx
> image: <resitry>/<user>/<image>

private registries available in private repos like in Amazon AWS

+ `docker login private-registry.io` where `private-registry.io` is a side where the repos are located
+ `docker run private-registry.io/apps/internal-app` to build/run it

![Deploy Private Registry](../attachments/2021-08-28-15-34-50.png)

# Section 7: Docker Engine, Storage and Networking

## Docker engine and namespaces

containerization == private namespaces <- PID

![PID on host vs container (child)](../attachments/2021-08-28-15-39-39.png)

docker uses **cgroups** to limit CPU/RAM usage to container

+ `docker run --cpu=.5 ubuntu`: limit to 50% CPU usage
+ `docker run --memory=100m ubuntu`: limit to 100 meg RAM usage

## Layered architecture

Docker builds on top of previous layer. Only applies changes (similar to how git works)

![Layered architecture](../attachments/2021-08-28-15-52-12.png)

Whatever is in the "image layer" is **read-only**. If modified, it's actually a copy in the container layer, which is also erased when the docker is killed.

## Volumes

Persistent storage

+ `docker volume create data_volume`: create a new volume
+ `docker run -v data_volume:/var/lib/mysql mysql`: **volume mount** mysql default location now pushed to data_volume
+ `docker run -v data_volume2:/var/lib/mysql mysql`: docker will automatically create data_volume2 since it wasn't already created
+ `docker run -v /path/to/folder:/var/lib/mysql mysql`: **bind mount**
+ `--mount` is preferred over `-v`, eg:
  + `docker run --mount type=bind,source=/data/mysql,targer=/var/lib/mysql mysql`

docker is installed in `var/lib/docker` and that's where it keeps its files

![Volume mounting](../attachments/2021-08-28-16-06-36.png)

+ `docker system df`: disk usage by image
+ `docker system df -v`: disk usage by image more verbose (shared size)

## Networking

+ Bridge
  + Inside the docker host
  + range 172.17.x.x (172.17.0.1)
  + to reach this, map them out
+ none
  + not connected, isolated
+ host
  + use host's network

to create a network within the host:

+ `docker network create --driver bridge --subnet 182.18.0.0/16 --gateway 182.18.0.1 custom-isolated-network`
+ `docker network ls` to list all networks
+ `docker inspect <name>` and you can see under network what is the containers mac/ip addresses
+ `docker run --network=none`: to start a docker without a network
+ `docker run --network=<network>`: to start a docker attaching to network <network>

# Section 8: Docker on Mac & Windows

# Section 9: Container Orchestration - Docker Swarm & Kubernetes

Host containers in a production environment

+ `docker service create --replicas=100 nodejs`

Orchestration offers:

+ Managing many hosts
+ Communication between hosts
+ Shared storage
+ Load balancing: increase number of containers is load increases, remove containers as load is decreased
+ Configuration management

Available:

+ kubernetes: most popular (by Google)
+ docker swarm:
+ mesos: hard to set up

## docker swarm

Have multiple hosts set up. Assign one as "swarm manager" or "master" and the rest as "workers" or "nodes" or "slaves".

+ `docker swarm init`: run on manager
+ `docker swarm join --token <token>`: join worker
+ `docker swarm create --replicas=3 my-web-server`
  + `docker swarm create` is equivalent to `docker run`

## kubernetes

+ `kubectl run --replicas=1000 my-web-server`: launch 1000
+ `kubectl scale --replicas=2000 my-web-server`: add more replicas
+ `kubectl rolling-update my-web-server --image=web-server:2`: update the containers
+ `kubectl rolling-update my-web-server --rollback`: roll-back the update
  + A/B testing...

master is responsible for orchestration

![kubernetes components](../attachments/2021-08-28-17-55-46.png)

Container runtime == docker!

+ `kubectl run hello-minikube`: launch a container
+ `kubectl cluster-info`
+ `kubectl get nodes`: list workers

# Section 10: Conclusion

[//begin]: # "Autogenerated link references for markdown compatibility"
[containerization]: containerization.md "Containerization"
[docker]: docker.md "Docker"
[dramble]: dramble.md "Raspberry Pi Dramble"
[//end]: # "Autogenerated link references"