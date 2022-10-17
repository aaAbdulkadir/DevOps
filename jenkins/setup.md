# Pipeline

- Make a Jenkins pipeline that builds my webapp docker image, logs into dockerhub and pushes it.

## Method

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