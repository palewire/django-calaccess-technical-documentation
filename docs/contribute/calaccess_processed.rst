Contribute to django-calaccess-processed-data
=======================================

This walkthrough is for developers who want to contribute to :doc:`/apps/calaccess_processed`, a Django app to transform and refine campaign-finance and lobbying-activity data from the California Secretary of State’s CAL-ACCESS database.

It will show you how to install the source code of this application to fix bugs and develop new features.

---------------


Preparing a development environment
-----------------------------------

It is not required, but it is recommended that development of the library be
done from within a contained virtual environment.

One way to accomplish that is with Python's ``virtualenv`` tool and its helpful companion ``virtualenvwrapper``.
If you have that installed, a new project can be started with the following:

.. code-block:: bash

    $ mkproject django-calaccess-processed-data

That will jump into a new folder in your code directory, where you can clone our
code repository from GitHub_ after you make a fork of your own. Don't know what that means? `Read this`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-processed-data.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Connecting to a local database
------------------------------

Unlike a typical Django project, this application only supports the MySQL and
PostgreSQL database backends. This is because we enlist specialized tools to load
the immense amount of source data more quickly than Django typically allows.

.. note::

    Unlike a typical Django project, this application only supports PostgreSQL database backends. This is because we enlist specialized tools to load the immense amount of source data more quickly than Django typically allows. We haven't developed those routines for SQLite and the other Django backends yet, but we might someday.

~~~~~~~~~~~~

Create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess_processed -U postgres

Create a file at ``example/project/settings_local.py`` to save your custom database credentials. That might look something like this.

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'calaccess_processed',
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

Once everything is set up, the updatecalaccessrawdata_ command will download the latest
bulk data release from `the Secretary of State's website <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ and load it into your local database.

.. code-block:: bash

    $ python example/manage.py updatecalaccessrawdata

.. warning::

    This will take a while. Go grab some coffee.

Because the nightly raw export is incomplete, we have to scrape additional data from the `CAL-ACCESS website`_. Use the scrapecalaccess_ command to kick off this process, either after ``updatecalaccessrawdata`` finishes or in a separate terminal window:

.. code-block:: sh

    $ python manage.py scrapecalaccess

Once the raw CAL-ACCESS data is loaded and the scrape has finished, you can transform all this messy data you've collected into our easy-to-understand, well-documented models with the processcalaccessdata_ command:

.. code-block:: bash

    $ python manage.py processcalaccessdata


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
* Interested in web scraping? Check out how to :doc:`contribute to django-calaccess-scraped-data </contribute/calaccess_scraped>` and help us fill in the gaps we've found in the nightly raw data exports.
* We also maintain an online archive that saves and republishes every day's dump. If you want to move on to get involved with those efforts, check out our guide on how to :doc:`contribute to django-calaccess-downloads-website </contribute/calaccess_website>`.



.. _GitHub: https://github.com/california-civic-data-coalition/django-calaccess-raw-data
.. _Read this: https://guides.github.com/activities/forking/
.. _the Secretary of State's website: http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/
.. _official PostgreSQL documentation: https://wiki.postgresql.org/wiki/Detailed_installation_guides
.. _multiple databases: /faq.html#do-i-have-to-load-the-cal-access-data-into-my-default-database
.. _updatecalaccessrawdata: /apps/calaccess_raw/managementcommands.html#updatecalaccessrawdata
.. _scrapecalaccess: /apps/calaccess_scraped/managementcommands.html#scrapecalaccess
.. _processcalaccessdata: /apps/calaccess_processed/managementcommands.html#_processcalaccessdata
.. _CAL-ACCESS website: http://cal-access.sos.ca.gov/Campaign/
.. _pep8: https://pypi.python.org/pypi/pep8
.. _pyflakes: https://pypi.python.org/pypi/pyflakes
.. _Github issue tracker: https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues