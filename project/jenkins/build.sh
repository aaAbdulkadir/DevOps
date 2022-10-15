#! /bin/bash

# get files onto jenkins server
echo "Cloning repo..."
git clone https://github.com/aaAbdulkadir/DevOps.git

# run docker-compose 
echo "Building docker image..."
cd project/streamlitapp/ 
docker-compose build

echo "Running docker image..."
docker-compose up -d