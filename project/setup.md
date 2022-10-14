# Plan of the project


## Diagram 

Something among these lines

![image](images/plan2.png)

CI/CD using Jenkins on Azure Container Service (AKS)

## Diagram Explained

- Change application source code.
- Commit code to GitHub.
- Continuous Integration Trigger to Jenkins.
- Jenkins triggers a build job using Azure Container Service (AKS) for a dynamic build agent.
- Jenkins builds and pushes Docker container Azure Container Registry.
- Jenkins deploys new containerized app to Kubernetes on Azure Container Service (AKS).
- Grafana displays visualization of infrastructure and application metrics via Azure Monitor.
- Monitor application and make improvements.


## Method

- Create a Terraform plan to deploy:
    - A virtual machine for jenkins
    - AKS for the kubernetes cluster of the webapp
    - ACR to push the image of the webapp to this rather than dockerhub
    - App service plan
- After creating plan, download jenkins on the VM and connect it to the github repository with the webapp and configure webhook.
    - Build the image of the webapp, test, deploy.
- Deploy webapp to App service so it can be used. Maybe requires Jenkins connection to AKS, ACR.

Jenkins:
- Clones the GitHub repository
- Builds a new container image
- Pushes the container image to the ACR registry
- Updates the image used by the AKS deployment



## References: 
- https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/container-cicd-using-jenkins-and-kubernetes-on-azure-container-service
- https://learn.microsoft.com/en-us/azure/developer/jenkins/configure-on-linux-vm
- https://github.com/Azure-Samples/azure-voting-app-redis
- https://learn.microsoft.com/en-us/azure/developer/jenkins/deploy-from-github-to-aks

## Walkthrough

### Terraform

- Create a terraform file with the following:
    - Resource group
    - Container registry
    - Kubernetes cluster
    - App service plan (change size)
    - Virtual machine

    where the container registry is attached to the kubernetes cluster in the tfplan.

    Once the file is ready, run the following:

    ```
    az login
    ```
    Log into Azure CLI so that terraform can push plan to Azure to account.

    ```
    terraform init

    terraform plan -out main.tfplan

    terraform apply main.tfplan
    ```

### Setting up files

#### Docker

- The Dockerfile exposes port 8501 which is the port streamlit listens in at. However, to make it run on Azure, the port needs to be mapped:
    - Using a docker-compose file, make the host port 80 for 
    Azure map onto the container port 8501 for streamlit.

- Before running the docker-compose file, it needs to be given an image name that is tagged with the necessary azure extension:
    - Add image under webapp service with the correct name
    - Tag the image with the container registry name + .azure.io + /{image_name}:
        - streamlit_container_registry.azure.io/portfolio-app:latest

- Once the docker image is created with the correct tag, it needs to be pushed to the container registry, which will be set up on the jenkins server as on the server, it will build the image and then be pushed to the container registry.

#### Kubernetes

- Make the image container the same as the docker image that is going to be pushed to the container registry.

### Setting up server

- Log into the VM created and download 
