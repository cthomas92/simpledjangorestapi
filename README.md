# SIMPLE DJANGO REST API

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/thirstywolf92/simpledjangorestapi.git
$ cd simpledjangorestapi
```

Install python 3.9 and Create a virtual environment to install dependencies in and activate it:

```sh
$ mkvirtualenv restapi
$ workon restapi
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Dont forget to install mongodb and restore dump:
if want to change credential to connect django to mongodb go to simpledjangorestapi/settings.py
and search djongo

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/simpleapi/user/`.

Write with Python Django
```sh
Credential 

username : admin
password : admin123

username : user
password : passuser

```

