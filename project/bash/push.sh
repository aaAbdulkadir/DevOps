#! /bin/bash

echo "Pushing docker image to ACR..."
cd project/streamlitapp/
docker-compose push