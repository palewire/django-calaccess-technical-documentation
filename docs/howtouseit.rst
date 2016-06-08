Getting started guide
=====================

This guide will walk you through the process of installing the latest official release
of `django-calaccess-raw-data <apps/calaccess_raw.html>`_, which will download and extract
the latest CAL-ACCESS archive before loading it into a local database.

If, instead, you want to install the raw source code or contribute as a developer please refer to
the :doc:`"How to contribute" </howtocontribute>` tutorial.

.. warning::

    This library is intended to be plugged into a project created with the Django web
    framework. Before you can begin, you'll need to have one up and running.
    If you don't know how, `check out the official Django documentation <https://docs.djangoproject.com/en/dev/intro/tutorial01/>`_.

------------------


Installing the Django app
-------------------------

The latest version of the application can be installed from the Python Package Index using ``pip``.

.. code-block:: bash

    $ pip install django-calaccess-raw-data

Like most Django applications, the app then needs to be added to the
``INSTALLED_APPS`` in your ``settings.py`` configuration file.

.. code-block:: python

    INSTALLED_APPS = (
        # ... other apps up here ...
        'calaccess_raw',
    )

------------------


Connecting to a local database
------------------------------

Also in the ``settings.py`` file, you will need to configure Django so it can connect to your database.

Unlike a typical Django project, this application only supports the MySQL and PostgreSQL database backends. This is because we enlist specialized tools to load the immense amount of source data more quickly than Django typically allows. We haven't developed those routines for SQLite and the other Django backends yet, but we're working on it.

Pick one of the two and continue below.

~~~~~~~~~~~~~~~~~~~


If you choose MySQL
~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you have a MySQL server installed. If you don't, now is the time to hit Google and figure out how. If you're using Apple's OSX operating system, you can `install via Homebrew <http://thisdotlife.com/2013/05/30/how-to-install-mysql-on-mac-os-x-using-homebrew-tutorial/>`_. `Here <http://dev.mysql.com/doc/refman/5.5/en/installing.html>`_ is the official MySQL documentation for how to get it done.

Once that's handled, add a database connection string like this to your ``settings.py``.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'calaccess_raw',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '3306',
            # You'll need this to use our data loading tricks
            'OPTIONS': {
                'local_infile': 1,
            }
        }
    }

Return to the command line. This will create a MySQL database to store the data.

.. code-block:: sh

    $ mysqladmin -h localhost -u your-username-here -p create calaccess_raw

And, if you don't have it already, you'll need to install a Python library that can access MySQL via Django. That can be done with `pip <https://pip.pypa.io/en/latest/installing.html>`_, a Python package management tool.

.. code-block:: sh

    $ pip install mysqlclient

~~~~~~~~~~~~~~~~~~


If you choose PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you have a PostgreSQL server installed. If you don't, now is the time to hit Google and figure out how. `Here <https://wiki.postgresql.org/wiki/Detailed_installation_guides>`_ is the official PostgreSQL documentation for how to get it done.

Once that's handled, add a database connection string like this to your ``settings.py``.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess_raw',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

Return to the command line. This will create a PostgreSQL database to store the data.

.. code-block:: bash

    $ createdb calaccess_raw

If you don't have it already, you'll need to install a Python library that can access PostgreSQL via Django. That can be done with `pip <https://pip.pypa.io/en/latest/installing.html>`_, a Python package management tool.

.. code-block:: bash

    $ pip install psycopg2

.. note::

    If you'd prefer to load the CAL-ACCESS outside your default database, check
    out our guide to working with Django's system for
    :ref:`multiple databases <faq-multi-databases>`.

------------------


Loading the data
----------------

Now you're ready to create the database tables with Django using its ``manage.py`` utility belt.

.. code-block:: sh

    $ python manage.py migrate

Once everything is set up, the :ref:`updatecalaccessrawdata` command will download the latest
bulk data release from `the Secretary of State's website <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ and load it into your location database.

.. code-block:: bash

    $ python manage.py updatecalaccessrawdata

.. warning::

    This will take a while. Go grab some coffee.

------------------


Exploring the data
------------------

Finally, start the development server and visit `localhost:8000/admin/ <http://localhost:8000/admin/>`_ in your browser to inspect the CAL-ACESS data in your Django administration panel.

.. code-block:: bash

    $ python manage.py runserver

If you don't have a super user that can log into the admin you might need to return to the command line and make one.

.. code-block:: bash

    $ python manage.py createsuperuser

------------------


Now what?
---------

You now have a complete copy of the database at your fingertips, more than 35 million records
chronicling money in California politics back to the year 2000. 

What you do with it is up to you. You can learn more how to navigate the system's 76
tables in our :doc:`database documentation </calaccess>`.

Our current mission is to start an online archive that saves and republishes every
day's dump. Then we aim to make the state's complex system easier to navigate
with tools that clean, transform and simplify the raw database. 

If you want to get involved with those efforts, check out our
:doc:`/apps/calaccess_downloads_site`
and :doc:`/apps/calaccess_processed` apps.
