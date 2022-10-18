#! /bin/bash

echo "setup stage"

#apt
apt-get update

#installing docker
if [ ! -f "/usr/bin/docker" ]; then
    curl https://get.docker.com | bash
    usermod -aG docker jenkins
fi