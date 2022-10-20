#! /bin/bash

echo "Logging into Azure..."
az login --service-principal -u $AZ_USR -p $AZ_PSW

echo "Connecting to AKS..."
az aks get-credentials --resource-group streamlit_project --name streamlit-aks
