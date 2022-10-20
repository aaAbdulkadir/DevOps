#!/bin/bash

# Docker
sudo apt-get update
sudo apt-get install docker.io
sudo usermod -aG docker $USER
newgrp docker

# Docker compose
cd | mkdir bin
cd bin
wget https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64 -O docker-compose
chmod +x docker-compose
echo "export PATH='${HOME}/bin:${PATH}'" >> ~/.bashrc
source ~/.bashrc
sudo groupadd docker-compose

# Java
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt update
sudo apt install openjdk-11-jre

# Jenkins
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins

# # Minikube
# curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
# sudo install minikube-linux-amd64 /usr/local/bin/minikube
# minikube start --driver docker

# Kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
sudo groupadd kubectl

# Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash



# Configure access
sudo usermod -aG docker jenkins
sudo usermod -aG docker-compose jenkins
sudo usermod -aG kubectl jenkins
sudo service jenkins restart