# blogint

to run the docker-compse.yml file folow this commands
docker-compose run --rm app django-admin startproject core
docker-compose up

to build image on docker
docker build --tag python-django .

to publish it into a container
docker run --publish 8000:8000 python-django