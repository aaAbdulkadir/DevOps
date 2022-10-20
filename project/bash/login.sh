#! /bin/bash

echo "Logging into ACR..."
docker login streamlitcontainerregistry.azurecr.io -u $ACR_USR -p $ACR_PSW