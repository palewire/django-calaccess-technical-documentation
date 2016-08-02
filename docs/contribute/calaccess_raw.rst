Contribute to django-calaccess-raw-data
=======================================

This walkthrough is for developers who want to contribute to :doc:`/apps/calaccess_raw`, a Django app to download, extract
and load campaign-finance and lobbying-activity data from the California Secretary of State’s CAL-ACCESS database.

It will show you how to install the source code of this application to fix bugs and develop new features.

---------------


Preparing a development environment
-----------------------------------

It is not required, but it is recommended that development of the library be
done from within a contained virtual environment.

One way to accomplish that is with Python's ``virtualenv`` tool and its helpful companion ``virtualenvwrapper``.
If you have that installed, a new project can be started with the following:

.. code-block:: bash

    $ mkproject django-calaccess-raw-data

That will jump into a new folder in your code directory, where you can clone our
code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-raw-data>`_
after you make a fork of your own. Don't know what that means? `Read this <https://guides.github.com/activities/forking/>`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-raw-data.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Connecting to a local database
------------------------------

Unlike a typical Django project, this application only supports the MySQL and
PostgreSQL database backends. This is because we enlist specialized tools to load
the immense amount of source data more quickly than Django typically allows.

We haven't developed similar routines for SQLite and the other Django backends yet,
but we're working on it. This might be something you could work on!

~~~~~~~~~~~~


If you choose MySQL
~~~~~~~~~~~~~~~~~~~

Create a new database named ``calaccess_raw`` like this:

.. code-block:: bash

    mysqladmin -h localhost -u root -p create calaccess_raw

Create a file at ``example/settings_local.py`` to save your custom database credentials. That might look something like this.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'calaccess_raw',
            'USER': 'yourusername', # <-- This
            'PASSWORD': 'yourpassword', # <-- And this
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'local_infile': 1,
            }
        }
    }

~~~~~~~~~~~~


If you choose PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~

Create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess_raw -U postgres

Create a file at ``example/project/settings_local.py`` to save your custom database credentials. That might look something like this.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess_raw',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

.. note::

    If you'd prefer to load the CAL-ACCESS outside your default database, check
    out our guide to working with Django's system for
    :ref:`multiple databases <faq-multi-databases>`.

---------------


Once the database is configured
-------------------------------

Now create the tables and get to work.

.. code-block:: bash

    $ python manage.py migrate

Once everything is set up, the :ref:`updatecalaccessrawdata` command will download the latest
bulk data release from `the Secretary of State's website <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ and load it into your location database.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata

.. warning::

    This will take a while. Go grab some coffee.

---------------

Exploring the data
------------------

Finally, start the development server and visit `localhost:8000/admin/ <http://localhost:8000/admin/>`_ in your browser to inspect the CAL-ACESS data in your Django administration panel.

.. code-block:: bash

    $ python manage.py runserver

If you don't have a super user that can log into the admin you might need to return to the command line and make one.

.. code-block:: bash

    $ python manage.py createsuperuser

------------------

Testing
-------

Our code is tested using `Django's built-in unittesting <https://docs.djangoproject.com/en/1.9/topics/testing/>`_ system via the `TravisCI <https://travis-ci.org/california-civic-data-coalition/django-calaccess-raw-data>`_
continuous integration service.

In addition, prior to the Django unittests, code is evaluated using Python's
`pep8 <https://pypi.python.org/pypi/pep8>`_ and `pyflakes <https://pypi.python.org/pypi/pyflakes>`_
style-guide enforcement tools.

When a commit or pull request is made with our repository, those tests are
rerun with the latest code. We try not to be too uptight, but we generally
expect the tests to be pass before we will merge a request.

------------------

Now what?
---------

You now have a complete copy of the database at your fingertips, more than 35 million records
chronicling money in California politics back to the year 2000.

What you do with it is up to you. You can learn more how to navigate the system's 76
tables in our :doc:`database documentation </calaccess>`.

To figure where to work on the raw data application, check out the `GitHub issue tracker <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues>`_
where plenty of work awaits.

Apart from that repository, our current mission is to start an online archive that saves and republishes every
day's dump. Then we aim to make the state's complex system easier to navigate
with tools that clean, transform and simplify the raw database.

If you want to get involved with those efforts, check out our
:doc:`/apps/calaccess_downloads_site`
and :doc:`/apps/calaccess_processed` apps.
