#! /bin/bash

cd jenkins
docker build -t app:latest .
docker tag app:latest streamlit-jenkins:latest