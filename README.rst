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

    $ git clone https://github.com/DominikWro/APIable.git .

Production ready config is based on this article
http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html

Only modification:
  Current config assumes slqlite instead of postgress

Production::

    $ docker-compose build
    $ docker-compose up


For your use only::

    $ cd /app_folder
    $ python manage.py migrate
    $ python manage.py runserver
