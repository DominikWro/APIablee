APIable Django
=======================

.. image:: https://travis-ci.org/DominikWro/APIable.svg?branch=master
    :target: https://travis-ci.org/DominikWro/APIable
    :alt: Build Status

.. image:: https://coveralls.io/repos/github/DominikWro/APIable/badge.svg?branch=master
    :target: https://coveralls.io/github/DominikWro/APIable?branch=master



APIable is an app written in Django that allows you to mock any API.


Usage
------

First, get APIable. Trust me, it's awesome::

    $ git clone https://github.com/DominikWro/APIablee.git APIablee
    $ python -m venv venv
    $ source venv/bin/activate
    $ cd APIablee
    $ pip install -r requirements.txt
    $ cd APIablee
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

Production ready config is based on this article
http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html

Only modification:
  Current config SQLite instead of PostgreSQL

Production::

    $ git clone https://github.com/DominikWro/APIablee.git APIablee
    $ cd APIablee
    $ docker-compose build
    $ docker-compose up

If you wish to use SQLite with docker-compose to run migrations do::

    $ docker ps
    $ docker exec -t -i CONTAINER ID bash
    $ cd APIablee
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
