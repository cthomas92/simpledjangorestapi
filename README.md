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
(restapi)$ pip install -r requirements.txt
```

Dont forget to install mongodb and restore dump:
if want to change credential to connect django to mongodb go to simpledjangorestapi/settings.py
and search like this

```sh
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'api', 
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost', #change to your db server location
            'port': 27017, # change to your port of db server 
            'username': 'userapi', #change to your username db server 
            'password': 'api231users', #change to your password db server 
            #'authSource': 'chris_training', # db name
            'authMechanism': 'SCRAM-SHA-1'
            
      #'authSource': 'yourcollection', # usually admin
    } 
    }
}
```

Once `pip` has finished downloading the dependencies:
```sh
(restapi)$ cd project
(restapi)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/simpleapi/user/`.
To show your static file you can serve that with nginx
and the location of static files in nginx/static and the conf is nginx/local.conf.

finally, if you want to running with docker. you can use Dockerfile in main folder. 
and for nginx in docker/nginx/Dockerfile

If you want to run in kubernetes go to kubernetes folder for the yaml file. 


Write with Python Django
```sh
Credential 

username : admin
password : admin123

username : user
password : passuser

```

