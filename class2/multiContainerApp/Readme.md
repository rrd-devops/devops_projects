Goal
Backend API returns random jokes; frontend calls backend and displays a joke. Both containers connected to same custom network.

Run the below commands
# create network
docker network create mynet
# build images
docker build -t rramado/jokes-backend:latest ./backend
docker build -t rramado/jokes-frontend:latest ./frontend
# run backend on the network
docker run -d --name backend --network mynet rramado/jokes-backend:latest
# run frontend on same network, publish port 8080
docker run -d --name frontend --network mynet -p 8080:80 rramado/jokes-frontend:latest

Test:
```bash
docker exec -it frontend sh

/ # curl http://backend:5000/joke
{"joke":"Why did the programmer quit his job? Because he didn't get arrays."}
/ # curl http://backend:5000/joke
{"joke":"There are 10 types of people: those who understand binary and those who don't."}
```

Both the frontend and backend docker images are pushed to the Dockerhub. 
https://hub.docker.com/repositories/rramado
