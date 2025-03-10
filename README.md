# Django REST framework - JWT Token authentication with Social providers

This is an example fullstack project of Django REST framework API using JWT Authentication with Google sign in.  

## Technologies

**API**
 - Python 3
 - Django 5
 - Django REST Framework
 - dj-rest-auth

Frontend
- React
- react-router-dom
- yarn
- Typescript

## Getting started

**Django API**

Create a new Python virtual environment
```shell
python -m venv .venv
```

Activate the virtual environment
```shell
source .venv/bin/activate
```

Install required packages
```shell
python -m pip install -r requirements.txt
```

Run Django server
```shell
python manage.py runserver
```

Frontend application

1. Make sure you have Node installed
2. Install modules `yarn install`
3. Create `.env.local` file and provide Google Client ID
4. Run `yarn dev`
