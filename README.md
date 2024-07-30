# CRUD API WITH DJANGO REST FRAMEWORK

## Requirements
- Python 3.12.4
- Django 5.0.7
- Django REST Framework

## Installation

```
python -m venv env
```

```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```

create a user 
```
python manage.py createsuperuser
```

update db conection
```
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": <DB_NAME>,
        "USER": <DB_USER>,
        "PASSWORD": <USER_PASSWORD>,
        "HOST": <IP_SERVER>,
        "PORT": <DB_PORT>,
    }
```
https://docs.djangoproject.com/en/5.0/ref/settings/#databases


## Endpoint

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product
`products/create`| POST | CREATE | Create a new product
`products/:id/update` | PUT | UPDATE | Update a product
`products/:id/delete` | DELETE | DELETE | Delete a product
`providers` | GET | READ | Get all providers
`providers/:id` | GET | READ | Get a single provider
`providers/create`| POST | CREATE | Create a new provider
`providers/:id/update` | PUT | UPDATE | Update a provider
`provider/:id/delete` | DELETE | DELETE | Delete a provider
