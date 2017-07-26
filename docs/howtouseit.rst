Installation Guide
==================

This guide will walk you through the process of installing the latest official release of :doc:`apps/calaccess_processed` so that you can incorporate CAL-ACCESS data into your own Django project.

If, instead, you want to install the raw source code or contribute as a developer please refer to the `"How to contribute"`_ tutorial.

.. warning::

    This library is intended to be plugged into a project created with the Django web framework. Before you can begin, you'll need to have one up and running. If you don't know how, `check out the official Django documentation`_.

------------------


Installing the Django apps
--------------------------

The latest version of the application can be installed from the Python Package Index using ``pip``.

.. code-block:: bash

    $ pip install django-calaccess-processed-data

Like most Django applications, the app then needs to be added to the
``INSTALLED_APPS`` in your ``settings.py`` configuration file. You also need to include other Django apps it depends on:

.. code-block:: python

    INSTALLED_APPS = (
        # ... other apps up here ...
        'calaccess_raw',
        'calaccess_scraped',
        'calaccess_processed',
        'opencivicdata.core.apps.BaseConfig',
        'opencivicdata.elections.apps.BaseConfig',
    )

A little more about these dependencies:

``calaccess_raw``
    This app downloads and extracts the raw data files `exported each night`_ from the CAL-ACCESS database. The app then loads these files into your Django project's database with minimal transformations. For more details, see the :doc:`apps/calaccess_raw` section.

``calaccess_scraped``
    This app scrapes the CAL-ACCESS website and loads additional data not included in the nightly exports. For more details, see the :doc:`apps/calaccess_scraped` section.

``opencivicdata.core``
    This app includes Django models and admin panels for the core data types of the `Open Civic Data`_ specification, including ``Person``, ``Organization``, ``Post`` and ``Membership``.

``opencivicdata.elections``
    This app includes Django models and admins panels for election-related data types that have been `provisionally included`_ in the Open Civic Data specification.

------------------


Connecting to a local database
------------------------------

Also in the ``settings.py`` file, you will need to configure Django so it can connect to your database.

.. note::

    Unlike a typical Django project, this application only supports PostgreSQL database backends. This is because we enlist specialized tools to load the immense amount of source data more quickly than Django typically allows. We haven't developed those routines for SQLite and the other Django backends yet, but we might someday.


Before you begin, make sure you have a PostgreSQL server installed. If you don't, now is the time to hit Google and figure out how. The `official PostgreSQL documentation`_ is another good place to start.

Once that's handled, add a database connection string like this to your ``settings.py``.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess_processed',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

Return to the command line. This will create a PostgreSQL database to store the data.

.. code-block:: bash

    $ createdb calaccess_processed

.. note::

    If you'd prefer to load the CAL-ACCESS outside your default database, check out our guide to working with Django's system for
    `multiple databases`_.

------------------


Loading the data
----------------

Now you're ready to create the database tables with Django using its ``manage.py`` utility belt.

.. code-block:: sh

    $ python manage.py migrate

Once everything is set up, the updatecalaccessrawdata_ command will download the latest bulk data release from `the Secretary of State's website`_ and load it into your location database.

.. code-block:: sh

    $ python manage.py updatecalaccessrawdata

.. warning::

    This will take an hour or more. Go grab some coffee.

Because the nightly raw export is incomplete, we have to scrape additional data from the `CAL-ACCESS website`_. Use the scrapecalaccess_ command to kick off this process, either after ``updatecalaccessrawdata`` finishes or in a separate terminal window:

.. code-block:: sh

    $ python manage.py scrapecalaccess

Once the raw CAL-ACCESS data is loaded and the scrape has finished, you can transform all this messy data and load into a more simplified structure with the processcalaccessdata_ command:

.. code-block:: bash

    $ python manage.py processcalaccessdata


.. _"How to contribute": /howtocontribute.html
.. _check out the official Django documentation: https://docs.djangoproject.com/en/1.11/intro/tutorial01/
.. _exported each night: 
.. _the Secretary of State's website: http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/
.. _Open Civic Data: https://opencivicdata.readthedocs.io/en/latest/#
.. _provisionally included: https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html
.. _official PostgreSQL documentation: https://wiki.postgresql.org/wiki/Detailed_installation_guides
.. _multiple databases: /faq.html#do-i-have-to-load-the-cal-access-data-into-my-default-database
.. _updatecalaccessrawdata: apps/calaccess_raw/managementcommands.html#updatecalaccessrawdata
.. _scrapecalaccess: /apps/calaccess_scraped/managementcommands.html#scrapecalaccess
.. _processcalaccessdata: /apps/calaccess_processed/managementcommands.html#processcalaccessdata
.. _CAL-ACCESS website: http://cal-access.sos.ca.gov/Campaign/