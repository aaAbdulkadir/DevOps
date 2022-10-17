#! /bin/bash

# get files onto jenkins server
echo "Cloning repo..."
git clone https://github.com/aaAbdulkadir/DevOps.git

# build image 
echo "Building docker image..."
cd ~/DevOps/project/streamlitapp/ 
docker-compose build