#! /bin/bash

echo "setup stage"

#apt
sudo apt-get update
sudo apt-get install -y curl jq python3-venv

#installing docker
if [ ! -f "/usr/bin/docker" ]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker jenkins
fi

# install docker compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose