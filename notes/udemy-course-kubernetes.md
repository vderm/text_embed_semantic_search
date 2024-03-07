---
author: Vasken Dermardiros
categories: note
tags:
- programming
- training
title: Udemy Course Kubernetes
---


[[containerization]], [[docker]], [[k3s]], [[dramble]]

Title: Kubernetes for the Absolute Beginnger - Hands On - DevOps

instructor part of kodekloud.com

# Section 1: Introduction

Kubernetes for Developers: prep for *Certified Kubernetes Application Developer* certifications

# Section 2: Kubernetes Overview

kubernetes = container orchestration

+ master == kube-apiserver installed, etcd (key-value distributed data store), controller (check how things are running), scheduler (distribute work)
+ worker == kubelet installed

# Section 3: Setup Kubernetes

## Install kubectl

+ <https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/>
+ <https://minikube.sigs.k8s.io/docs/handbook/kubectl/>

> curl -LO "<https://dl.k8s.io/release/$(curl> -L -s <https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl>"
> sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

## Install VirtualBox

<https://www.virtualbox.org/wiki/Linux_Downloads>

## Install minikube

<https://minikube.sigs.k8s.io/docs/start/>

> curl -LO <https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb>
> sudo dpkg -i minikube_latest_amd64.deb

### Minikube in docker
>
> sudo usermod -aG docker $USER && newgrp docker
> minikube start

### Minikube in VirtualMachine
>
> minikube start --driver=virtualbox
>
# Section 4: Kubernetes Concepts

## PODs

+ [Pods overview](https://kubernetes.io/docs/concepts/workloads/pods/)

POD ~= containter. To scale in kubernetes, add a new POD. Don't add a new container to an existing pod.

![PODs and containers](../attachments/2021-08-30-10-57-25.png)

In case that two containers really need to work together, they can be spun up in the same POD and can communicate to each other via "localhost". They can also share the local storage space.

+ `kubectl run nginx --image nginx`: install nginx from dockerhub repo
+ `kubectl get pods`: list pods available/running
+ `kubectl get pods -o wide`: list pods available/running with more info
+ `kubectl get deployments`: list deployments available/running
+ `kubectl delete deployment <deployment name>`: delete deployment `<deployment name>`
+ `kubectl describe pod <pod name>`: get lots of info

# Section 5: YAML Introduction

skipped

# Section 6: PODs, ReplicaSets, Deployments

## PODs

``` yaml
# pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    type: front-end
spec:
  containers:
  - name: nginx-container
    image: nginx
```

+ mandatory fields: apiVersion, kind, metadata, spec
+ apiVersion: kind
  + v1: POD or Service
  + apps/v1: ReplicaSet or Deployment
+ metadata is stricter on what can be under it (name, labels)
  + labels: can have any key:value pair
+ spec:
  + containers: list of containers to use

+ `kubectl create -f pod-definition.yml`: create pod
+ `kubectl apply pod-definition.yml`: create pod
+ `kubectl get pods`: active pods
+ `kubectl describe pod myapp-pod`: detailed info about myapp-pod

### Another Example

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
  labels:
    tier: db-tier
spec:
  containers:
    - name: postgres
      image: postgres
      env:
        - name: POSTGRES_PASSWORD
          value: mysecretpassword
```

## Replication Controller

Responsible for high availability. Ensures specified number of pods are running at a given time.

Responsible of load balancing too within a node and multiple nodes.

+ `Replication controller`: older technology
+ `Replica set`: newer technology

``` yaml
# rc-definition.yml
apiVersion: v1
kind: ReplicationController
metadata:
  name: myapp-rc
  labels:
    app: myapp
    type: front-end
spec:
  template:  # pod-definition.yml
    metadata:
      name: myapp-pod
      labels:
        app: myapp
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
```

+ `kubectl create -f rc-definition.yml`: start replication controller
+ `kubectl get replicationcontroller`: see replication contoller running containers
+ `kubectl get pods`

## Replica Set

``` yaml
# replicaset-definition.yml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-replicaset
  labels:
    app: myapp
    type: front-end
spec:
  template:  # pod-definition.yml
    metadata:
      name: myapp-pod
      labels:
        app: myapp
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
  selector:  # replica set can handle pods created before this was launched if matching a name
    matchLabels:
      type: front-end
```

`Replica Set` can handle pods created before this was launched if matching a name --> can monitor pods and if any fails, launch a new one. It knows which one to look for using labels.

If you want to change the number of replicas from 3 to 6:

1. update the `replicas` entry in the `replicaset-definition.yml` file
2. `kubectl replace -f replicaset-definition.yml`: more permanent solution
3. or do it manually `kubectl scale --replicas=6 -f replicaset-definition.yml`
4. or do it manually `kubectl scale --replicas=6 replicaset myapp-replicaset`

+ `kubectl delete replicaset myapp-replicaset`: deletes the controller and the pods associated
+ `kubectl edit replicaset myapp-replicaset`: edit the live file

## Deployments

Want to deploy apps, update pods if new version comes up, perform upgrades in a rolling fashion. If it doesn't work, rollback.

Deployment is at a higher level than Replica Set

![Deployment and Replica Set](../attachments/2021-09-04-16-24-07.png)

``` yaml
# deployment-definition.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  labels:
    app: myapp
    type: front-end
spec:
  template:  # pod-definition.yml
    metadata:
      name: myapp-pod
      labels:
        app: myapp
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
  selector:  # replica set can handle pods created before this was launched if matching a name
    matchLabels:
      type: front-end
```

+ `kubectl create -f deployment-definition.yml`
+ `kubectl get deployments`: creates a replica set too and then pods
+ `kubectl get all`: see everything

## Rollout and Versionning (updates)

![](../attachments/2021-09-04-16-34-10.png)

+ `kubectl rollout status deployment/myapp-deployment`: see status
+ `kubectl rollout history deployment/myapp-deployment`: see revision numbers

+ Deployment strategy 1 (recreate): destroy all running apps and then launch new ones from scratch
+ Deployment strategy 2 (rolling update): destroy 1 running app and then launch a new one from scratch one by one

1. update the image or wtv in the container section of the deployment
2. `kubectl apply -f deployment-definition.yml`: to start the update process

How it actually upgrades: deployment creates a new replica set and starts new pods. While those start turning on, it destroys the pods in the old replica set.

![](../attachments/2021-09-04-16-45-24.png)

+ `kubectl rollout undo deployment/myapp-deployment`: go back to previous replica set

Assume we have 3 revisions. If we undo to go back to "2", it actually pushes those changes as revision "4" and deletes the old "2".

# Section 7: Networking in Kubernetes

![Single-Node Internal Networking](../attachments/2021-09-04-16-58-58.png)

Each pod is given an IP address. Don't rely on it too much since pods are started and destroyed non-stop.

![Cluster Networking](../attachments/2021-09-04-17-02-03.png)

A router is needed to link Nodes together!

# Section 8: Services

Services enable communication between pods.

![Services](../attachments/2021-09-04-17-04-14.png)

+ `NodePort`: External connection: service to forward ports
+ `ClusterIP`: Create virtual IP
+ `LoadBalancer`: Distribute load across different servers/pods

## NodePort

![Ports](../attachments/2021-09-04-17-08-12.png)

``` yaml
# service-definition.yml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: NodePort
  ports:
  - targetPort: 80
    port: 80
    nodePort: 30008
  selector:  # take the labels from metadata from the pod-definition.yml file
    app: myapp
    type: front-end
```

+ `kubectl create -f service-definition.yml`
+ `kubectl get services`

![App on different nodes](../attachments/2021-09-04-17-16-17.png)

Kubernetes takes care of routing stuff :)

Since I'm running this using minikube, do this to get to the final IP:

`minikube service myapp-service --url`

## ClusterIP

Cannot rely on internal IPs since containers keep switching.

![ClusterIP](../attachments/2021-09-05-09-41-11.png)

``` yaml
# service-definition.yml
apiVersion: v1
kind: Service
metadata:
  name: back-end
spec:
  type: ClusterIP  # default type
  ports:
  - targetPort: 80
    port: 80
  selector:
    app: myapp
    type: back-end
```

## Load Balancer

![Example voting app](../attachments/2021-09-05-10-11-04.png)

``` yaml
# service-definition.yml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: LoadBalancer  # will work in normal cloud providers; in virtualbox, itll act as nodeport
  ports:
  - targetPort: 80
    port: 80
    nodePort: 30008
  selector:
    app: myapp
    type: back-end
```

# Section 9: Microservices Architecture

![Sample voting application](../attachments/2021-09-05-10-19-24.png)

## Run all containers
>>>
>>> docker run -d --name=redis redis
>>> docker run -d --name=db postgres:9.4
>>> docker run -d --name=vote -p 5000:80 voting-app
>>> docker run -d --name=result -p 5001:80 result-app
>>> docker run -d --name=worker worker

## Link them together
>>>
>>> docker run -d --name=redis redis
>>> docker run -d --name=db postgres:9.4
>>> docker run -d --name=vote -p 5000:80 --link redis:redis voting-app
>>> docker run -d --name=result -p 5001:80 --link db:db result-app
>>> docker run -d --name=worker --link db:db --link redis:redis worker

docker swarm does better than links. Also see [[udemy-course-docker]]

## Voting app on kubernetes

![Goals](../attachments/2021-09-05-10-27-51.png)

Nothing needs to access the worker pod. Pod access the DBs.

![Service to expose Redis](../attachments/2021-09-05-10-31-10.png)

Can't use IPs so make a service (ClusterIP) to expose the Redis pod. Name is important because it is hard-coded in the Python and .net programs. (better to use env variable though)

![Service to expose front-end apps](../attachments/2021-09-05-10-34-15.png)

Similarly, need to make a service (NodePort) to expose the front-end apps.

Worker doesn't require a service because it doesn't need to be accessed by other apps.

## Configuring the app: PODs

``` yaml
# voting-app-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: voting-app-pod
  labels:
    name: voting-app-pod
    app: demo-voting-app
spec:
  containers:
    - name: voting-app
      image: kodekloud/examplevotingapp_vote:v1
      ports:
        - containerPort: 80
```

``` yaml
# result-app-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: result-app-pod
  labels:
    name: result-app-pod
    app: demo-voting-app
spec:
  containers:
    - name: result-app
      image: kodekloud/examplevotingapp_result:v1
      ports:
        - containerPort: 80
```

``` yaml
# redis-app-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis-pod
  labels:
    name: redis-pod
    app: demo-voting-app
spec:
  containers:
    - name: redis
      image: redis
      ports:
        - containerPort: 6379
```

``` yaml
# postgres-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres-pod
  labels:
    name: postgres-pod
    app: demo-voting-app
spec:
  containers:
    - name: postgres
      image: postgres
      ports:
        - containerPort: 5432
      env:
        - name: POSTGRES_USER # note better to use secrets instead
          value: "postgres"
        - name: POSTGRES_PASSWORD
          value: "postgres"
```

``` yaml
# worker-app-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-app-pod
  labels:
    name: worker-app-pod
    app: demo-voting-app
spec:
  containers:
    - name: worker-app
      image: kodekloud/examplevotingapp_worker:v1
```

## Configuring the app: Services

### Internal services

``` yaml
# redis-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
  labels:
    name: redis-service
    app: demo-voting-app
spec:
  ports:
    - port: 6379
      targetPort: 6379
  selector:
    name: redis-pod
    app: demo-voting-app
```

``` yaml
# postgres-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: db
  labels:
    name: postgres-service
    app: demo-voting-app
spec:
  ports:
    - port: 5432
      targetPort: 5432
  selector:
    name: postgres-pod
    app: demo-voting-app
```

### External services

``` yaml
# voting-app-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: voting-service
  labels:
    name: voting-service
    app: demo-voting-app
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30004
  selector:
    name: voting-app-pod
    app: demo-voting-app
```

``` yaml
# result-app-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: result-service
  labels:
    name: result-service
    app: demo-voting-app
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30005
  selector:
    name: result-app-pod
    app: demo-voting-app
```

## Running

one by one:

+ run the pod
+ run the service

## Running using Deployments

Use deployments to ease the app creation. Deployments automatically create ReplicaSets so no need to define those.

``` yaml
# voting-app-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: voting-app-deploy
  labels:
    name: voting-app-deploy
    app: demo-voting-app
spec:
  replicas: 1
  selector:
    matchLabels: voting-app-pod
    app: demo-voting-app
  template:
    metadata:
      name: voting-app-pod
      labels:
        name: voting-app-pod
        app: demo-voting-app
    spec:
      containers:
        - name: voting-app
          image: kodekloud/examplevotingapp_vote:v1
          ports:
            - containerPort: 80
```

... and do the same for Redis, and other apps

So to run it after, run deployments and services.

+ `kubectl create -f voting-app-deploy.yaml`
+ `kubectl create -f voting-app-service.yaml`

If you go on the site after, every once in a while, the vote is handled by a different pod.

# Section 10: Kubernetes on Cloud

# Section 11: Conclusion

# Section 12: Appendix - Setup Multi Node cluster using Kubeadm

# Convert docker-compose.yml to kubernetes

<https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/>

# Cheatsheet

<https://kubernetes.io/docs/reference/kubectl/cheatsheet/>

[containerization]: containerization.md "Containerization"
[docker]: docker.md "Docker"
[k3s]: k3s.md "k3s"
[udemy-course-docker]: udemy-course-docker.md "Udemy Course Docker"

[//begin]: # "Autogenerated link references for markdown compatibility"
[containerization]: containerization.md "Containerization"
[docker]: docker.md "Docker"
[k3s]: k3s.md "k3s"
[dramble]: dramble.md "Raspberry Pi Dramble"
[udemy-course-docker]: udemy-course-docker.md "Udemy Course Docker"
[//end]: # "Autogenerated link references"