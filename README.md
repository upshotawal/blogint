# blogint

<h2>to run the docker-compse.yml file folow this commands</h2>
docker-compose run --rm app django-admin startproject core
docker-compose up

<h2>to build image on docker</h2>
docker build --tag python-django .

<h2>to publish it into a container</h2>
docker run --publish 8000:8000 python-django