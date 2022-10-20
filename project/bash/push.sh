#! /bin/bash

# push docker image to ACR
echo "Pushing docker image..."
cd project/streamlitapp/
docker-compose push