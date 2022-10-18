#!/bin/bash


# Docker
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce -y


# Configure access
usermod -aG docker jenkins
usermod -aG docker azureuser
sudo touch /var/lib/jenkins/jenkins.install.InstallUtil.lastExecVersion
service jenkins restart
