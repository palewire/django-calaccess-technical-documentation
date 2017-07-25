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

Exploring the data
------------------

Finally, start the development server and visit `localhost:8000/admin/ <http://localhost:8000/admin/>`_ in your browser to inspect the CAL-ACCESS data in your Django administration panel.

.. code-block:: bash

    $ python example/manage.py runserver

If you don't have a super user that can log into the admin you might need to return to the command line and make one.

.. code-block:: bash

    $ python example/manage.py createsuperuser

------------------

Testing
-------

Our code is tested using `Django's built-in unittesting`_ system via the TravisCI_ continuous integration service.

In addition, prior to the Django unittests, code is evaluated using Python's
pep8_ and pyflakes_ style-guide enforcement tools.

When a commit or pull request is made with our repository, those tests are
rerun with the latest code. We try not to be too uptight, but we generally
expect the tests to be pass before we will merge a request.

------------------

Now what?
---------

You now have a complete copy of the database at your fingertips, more than 35 million records chronicling money in California politics back to the year 2000.

To figure where to work on the raw data application, check out the `GitHub issue tracker`_ where plenty of work awaits.

You might also consider contributing to other components of our project:

* While it's more or less in maintenance mode, you might :doc:`contribute to django-calaccess-raw-data </contribute/calaccess_raw>`, the app that downloads, extracts and loads the nightly exports of raw CAL-ACCESS data.
* If you have strong opinions about what campaign-finance and lobbying-activity data *should* look like, check out this guide on how to :doc:`contribute to django-calaccess-processed-data </contribute/calaccess_processed>`, where we're striving to design and load more user-friendly data models.
* We also maintain an online archive that saves and republishes every day's dump. If you want to move on to get involved with those efforts, check out our guide on how to :doc:`contribute to django-calaccess-downloads-website </contribute/calaccess_website>`.


.. _GitHub: https://github.com/california-civic-data-coalition/django-calaccess-scraped-data
.. _Read this: https://guides.github.com/activities/forking/
.. _multiple databases: /faq.html#do-i-have-to-load-the-cal-access-data-into-my-default-database
.. _scrapecalaccess: /apps/calaccess_scraped/managementcommands.html#scrapecalaccess
.. _CAL-ACCESS website: http://cal-access.sos.ca.gov/Campaign/
.. _Django's built-in unittesting: https://docs.djangoproject.com/en/1.9/topics/testing/
.. _TravisCI: https://travis-ci.org/california-civic-data-coalition/django-calaccess-scraped-data
.. _pep8: https://pypi.python.org/pypi/pep8
.. _pyflakes: https://pypi.python.org/pypi/pyflakes
.. _Github issue tracker: https://github.com/california-civic-data-coalition/django-calaccess-scraped-data/issues