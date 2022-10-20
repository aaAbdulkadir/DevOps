#! /bin/bash

echo "Logging into Azure..."
az login --service-principal -u $AZ_USR -p $AZ_PSW --tenant 01978399-4056-4dee-a3c4-43d8226119f6

echo "Connecting to AKS..."
az aks get-credentials --resource-group streamlit_project --name streamlit-aks
