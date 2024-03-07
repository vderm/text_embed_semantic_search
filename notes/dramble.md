---
author: Vasken Dermardiros
categories: note
tags:
- programming
- training
title: Raspberry Pi Dramble
---

following: https://alexellisuk.medium.com/walk-through-install-kubernetes-to-your-raspberry-pi-in-15-minutes-84a8492dc95a

installed raspbian lite 64-bit using etcher

add `ssh` file in boot partition

did the setup using the raspberry pi imager program instead

copied my laptop's ssh id_rsa.pub key there and booted

`raspi-config` to resize video memory to 16 mb since this will be run headless

then added in `/boot/cmdline.txt`:
cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory

and also set the IP address and name there

# ran on laptop
## set up server node
export DRAMBLE_SERVER_IP=10.0.0.35
k3sup install --ip $SERVER_IP --user pi

## set up worker nodes
export DRAMBLE_WORKER1_IP=10.0.0.122
k3sup join --ip $DRAMBLE_WORKER_1_IP --server-ip $DRAMBLE_SERVER_IP --user pi

repeat for other nodes...

# setup
+ master : m0 label on device : 10.0.0.35
+ worker-1 : w1 label on device : 10.0.0.122 -> didn't do the override thing in /boot/cmdline.txt for any of the workers...
+ worker-2 : w2 label on device : 10.0.0.113
+ worker-3 : w3 label on device : 10.0.0.146


# check setup
`kubectl get node -o wide`
