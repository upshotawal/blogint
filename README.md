# blogint

## how to run the django application
First
<h1>Create a virtual env Using</h1>
pipenv shell
<h1>install requirements using</h1>
pip install -r requirements.txt
<br/>
py manage.py runserver

# For webscraping go to the SCRAPER folder and CTRL+F5 the python script you want to learn.
# to load the csv file
Put the csv file in app folder and run this command:
<br/>
<h1> py manage.py runscript product_load</br>
# Then You will have a csv file after the scape and out the file in the blog-app folder and run the python script inside the SCRIPTS FOLDER inside Blog folder.

<h2>to run the docker-compse.yml file folow this commands</h2>
docker-compose run --rm app django-admin startproject core <br/>
docker-compose up

<h2>to build image on docker</h2>
docker build --tag python-django .

<h2>to publish it into a container</h2>
docker run --publish 8000:8000 python-django