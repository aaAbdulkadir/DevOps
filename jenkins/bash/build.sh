#! /bin/bash

docker build -t app:latest .
docker tag app:latest streamlit-jenkins:latest