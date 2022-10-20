#!/bin/bash

# Docker
sudo apt-get update
sudo apt-get install docker.io
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# Docker compose
cd | mkdir bin
cd bin
wget https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64 -O docker-compose
chmod +x docker-compose
echo "export PATH='${HOME}/bin:${PATH}'" >> ~/.bashrc
source ~/.bashrc

# Java
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt update
sudo apt install openjdk-11-jre

# Jenkins
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins
