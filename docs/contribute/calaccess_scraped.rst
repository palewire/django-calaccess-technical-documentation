Contribute to django-calaccess-scraped-data
===========================================

This walkthrough is for developers who want to contribute to :doc:`/apps/calaccess_scraped`, a Django app to scrape from the CAL-ACCESS website supplementary data not included in the California Secretary of State's nightly data dumps.

It will show you how to install the source code of this application to fix bugs and develop new features.

---------------


Preparing a development environment
-----------------------------------

It is not required, but it is recommended that development of the library be
done from within a contained virtual environment.

One way to accomplish that is with Python's ``virtualenv`` tool and its helpful companion ``virtualenvwrapper``. If you have that installed, a new project can be started with the following:

.. code-block:: bash

    $ mkproject django-calaccess-scraped-data

That will jump into a new folder in your code directory, where you can clone our
code repository from GitHub_ after you make a fork of your own. Don't know what that means? `Read this`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-scraped-data.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Connecting to a local database
------------------------------

The ``calaccess_scraped`` app doesn't have any specific database requirements. However, we recommend PostgreSQL 9.4 (or greater), which is a hard requirement of other apps in our tool chain.

Create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess_scraped -U postgres

Create a file at ``example/project/settings_local.py`` to save your custom database credentials. That might look something like this.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess_scraped',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username', # <-- Change this
            'PASSWORD': 'password', # <-- And this
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

.. note::

    If you'd prefer to load the CAL-ACCESS outside your default database, check out our guide to working with Django's system for `multiple databases`_.

---------------


Once the database is configured
-------------------------------

Now create the tables and get to work.

.. code-block:: bash

    $ python example/manage.py migrate

Now you're ready to scrape. The scrapecalaccess_ command will download, cache and parse content from the `CAL-ACCESS website`_:

.. code-block:: bash

    $ python example/manage.py scrapecalaccess

---------------

Welcome aboard!
---------------

Now that your development environment is set up, check out the `GitHub issue tracker`_ where plenty of work awaits.

As you submit your work, please pay attention to the results of our `integration tests`_ (more details :doc:`here </contribute/testing>`).


.. _GitHub: https://github.com/california-civic-data-coalition/django-calaccess-scraped-data
.. _Read this: https://guides.github.com/activities/forking/
.. _multiple databases: /faq.html#do-i-have-to-load-the-cal-access-data-into-my-default-database
.. _scrapecalaccess: /apps/calaccess_scraped/managementcommands.html#scrapecalaccess
.. _CAL-ACCESS website: http://cal-access.sos.ca.gov/Campaign/
.. _Github issue tracker: https://github.com/california-civic-data-coalition/django-calaccess-scraped-data/issues
.. _integration tests: https://travis-ci.org/california-civic-data-coalition/django-calaccess-scraped-data
