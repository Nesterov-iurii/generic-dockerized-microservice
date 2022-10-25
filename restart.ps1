docker stop generic-app
docker rm generic--app
docker build --ssh gitlab_ssh_key="Path\.ssh\key1" -t generic- .
docker run -it -p 5000:5000 --restart=always --name generic--app generic-
