Django Shipments REST API
============================

Requirements
------------

  * Docker;
  * Docker-Compose;

Installation
------------

Clone the main repository locally.

```bash
$ git clone https://github.com/LeikoDmitry/django-shipment.git
$ cd django-shipment
```
Rename `.env.example` to `.env` and update values.

Usage
-----
There's no need to configure anything to run the application
```bash
$ docker-compose up -d --build
```
Then access the application in your browser at the given URL (http://127.0.0.1:8080 VueJS and http://127.0.0.1:8000 Django REST API).

After that you can go to admin area `http://127.0.0.1/admin`, but before you need create the user via command:

```bash
$ docker-compose run --rm python python manage.py createsuperuser
```
And the last step is to create `shipments` in admin area.

Test
----
```bash
$ docker-compose run --rm python python manage.py test
```