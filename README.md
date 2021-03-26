## Car API

## Table of contents

-   [General info](#general-info)
-   [API Endpoints](#api-endpoints)
-   [Technologies](#technologies)
-   [Setup](#setup)

## General info

Car Retailer is a REST API built with Flask & SQLAlchemy to operate CRUD operation on the database. The different routes are described below in the API Endpoint section.

## API Endpoints

### GET

Return JSON with cars.

> http://127.0.0.1:5000/api/cars

> http://127.0.0.1:5000/api/car/1

### POST

Create a car from JSON Content-Type: application/json

```
Body: {"brand": "brand", "color": "color", "matriculation": "matriculation", "price": "price"}
```

> http://127.0.0.1:5000/api/cars

### PUT

Update a car from JSON Content-Type: application/json

```
Body: {"brand": "brand", "color": "color", "matriculation": "matriculation", "price": "price"}
```

> http://127.0.0.1:5000/api/car/1

### DELETE

Delete a car from ID

> http://127.0.0.1:5000/api/car/1

## Technologies

Project is created with:

-   Python v3.8.5
-   astroid v2.4.2
-   click v7.1.2
-   colorama v0.4.4
-   Flask v1.1.2
-   isort v5.6.4
-   itsdangerous v1.1.0
-   Jinja2 v2.11.2
-   lazy-object-proxy v1.4.3
-   MarkupSafe v1.1.1
-   mccabe v0.6.1
-   pylint v2.6.0
-   six v1.15.0
-   toml v0.10.2
-   Werkzeug v1.0.1
-   wrapt v1.12.1

## Setup

```
$ git clone https://github.com/antoineratat/car_API.git
$ py -3 -m venv venv
$ venv\Script\Activate
$ cd car_api
$ pip install -r requirements.txt
$ python run.py
```
