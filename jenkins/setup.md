# Pipeline

- Make a Jenkins pipeline that builds my webapp docker image, logs into dockerhub and pushes it.

## Method

- Make a Vagrant VM to test product on a new linux environment.

- Download jenkins, docker and docker compose:

Download docker
```
sudo apt-get update
sudo apt-get install docker.io

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Download docker-compose in bin directory
```
cd /bin/

sudo wget https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64 -O docker-compose

sudo chmod +x docker-compose

nano .bashrc
   export PATH="/bin:${PATH}"
source .bashrc
```

Install Java for Jenkins
```
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt update
sudo apt install openjdk-11-jre
```

Install Jenkins

- ERROR: GPG: "GPG: no valid OpenPGP data found" when trying to download
```
wget --no-check-certificate -qO - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -


```

Note: Issues with certification when trying to download Jenkins, so will use local instead.

Note 2: Running jenkins docker image, git is installed but docker is not when going into bash of the container. Download docker onto the bash.

Setup:


- Create a pipeline project:
    - Add Github repo with jenkins file as the script under pipeline in configure (pipeline script from SCM)
    - Public repo so do not need credentials.
    - Change branch to main
- Create environment variable to log into dockerhub:
    - Go to dockerhub and under security, create an access token.
    - Dockerhub tells you to run this by typing the follwoing command:
        - docker login -u {username}
        - add password at the end of the line to automate it and copy the password given. Use that password in jenkins as username password setup credential.
        - ID: {username}-dockerhub
- Put dockerhub environment variable in jenkins file.


Note: turn jenkins on and off on windows:
- Go to path where the jenkins folder is and run:
    - jenkins.exe stop

In this case, I ran jenkins as a docker container and the pipeline worked.