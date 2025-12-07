
Goal: Flask app showing your name, current date/time, list of favorite movies; package in Docker and push to Docker Hub.

Docker Image: https://hub.docker.com/repository/docker/rramado/buildawebapp/general

How to run:

# This installs the docker, starts the app and waits for client request at the port 5000
docker run -d -p 5000:5000 --name assignment1 rramado/buildawebapp:latest

# Test - Run the below command in the browser.
http://localhost:5000/
# Output should show my name, favorite movies, current date and time. 



