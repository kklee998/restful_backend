# Simple RESTful backend with Django REST framework and JWT

Simple todo list REST API built with Django, DRF and JWT

## Getting started

First create your virtual environment ...
```bash
python3 -m virtualvenv venv
source venv/bin/activate 
```
... then install all the required packages

```bash
pip install -r requirements.txt
```
Lastly, run the migrations

```bash
python manage.py makemigrations
```

To start the development server, run 

```bash
python manage.py runserver
```

Navigate to [localhost:8000](localhost:8000) to browse the API

## Creating superuser

To create a new admin:

```bash
python manage.py createsuperuser
```

You can login and make use of the admin panel at [localhost:8000/admin](localhost:8000/admin)
