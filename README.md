This application creates a fibonacci sequence creator using flask and nginx.
The pipelines created will have two effects.
First Effect (Build-Push-Docker-Images-Docker-Hub-Pipeline.txt) - Check out from GIT, build docker image using Dockerfile under flask_app and nginx directories, pushes to DockerHub, Tests deploy of application and then performs cleanup.
Second Effect (Jenkins-Pipeline-Login.txt) - Pulls Image from DockerHub, creates container and keeps the container running for consumption.
