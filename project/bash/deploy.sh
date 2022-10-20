#! /bin/bash

echo "Deploying to kubernetes cluster..."

cd project/streamlitapp/ 
kubectl apply -f k8-app.yaml