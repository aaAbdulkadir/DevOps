#! /bin/bash

# build image 
echo "Building docker image..."
cd project/streamlitapp/ 
docker-compose build
