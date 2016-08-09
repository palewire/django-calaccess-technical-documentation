Management commands
===================

The `downloads-website <apps/calaccess_downloads_site>`_ app includes the following commands for updating and publishing the website's content.

Our website is one of those trendy static content sites that you've probably heard a lot about lately. This just means that, instead of generating HTML on-the-fly with each request from a user's browser, we create and save all the web pages ahead of time by executing Python code against the database backend once a day.

This process is often called "baking", and there's a `really handy app <https://django-bakery.readthedocs.io/en/latest/>`_ that we rely on to make all this work.

As with any Django app management command, these can be invoked on the command line or `called within your Python code <https://docs.djangoproject.com/en/1.9/ref/django-admin/#running-management-commands-from-your-code>`_.

----------------------

.. _updatedownloadswebsite:

updatedownloadswebsite
~~~~~~~~~~~~~~~~~~~~~~

Update to the latest CAL-ACCESS snapshot and bake static website pages.

This is the master command that performs the entire daily routine of downloading, processing and archiving the latest raw data, then re-building the downloads website's content.

.. code-block:: sh

    $ python manage.py updatedownloadswebsite


In order to publish this content to the S3 bucket where it's served, you can invoke the ``--publish`` option:

.. code-block:: sh

    $ python manage.py updatedownloadswebsite --publish


Also, this command is a sub-class of the `raw-data app's <apps/calaccess_raw/managementcommands.html#updatecalaccessrawdata>`_ ``updatecalaccessrawdata`` command, so it inherits all the options of the parent command. For example, if you want to keep copies of the latest raw data files on the app's server, you can:

.. code-block:: sh

    $ python manage.py updatedownloadswebsite --keep-files


The other options are below.

Options
```````

.. code-block:: sh

    usage: manage.py updatedownloadswebsite [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [--keep-files] [--noinput] [--test]
                                            [-a APP_NAME] [--publish]

    Update to the latest CAL-ACCESS snapshot and bake static website pages

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.
      --keep-files          Keep zip, unzipped, TSV and CSV files
      --noinput             Download the ZIP archive without asking permission
      --test, --use-test-data
                            Use sampled test data (skips download, clean a load)
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app with models into which data will be
                            imported (if other not calaccess_raw)
      --publish             Publish baked content

----------------------


createlatestlinks
~~~~~~~~~~~~~~~~~

Save copies of data files from the most recently completed update in a latest/
directory in the Django project's default file storage.

.. code-block:: sh

    $ python manage.py createlatestlinks

This command will also clear out any objects currently saved under latest/ before saving new ones.

Options
```````

.. code-block:: sh

    usage: manage.py createlatestlinks [-h] [--version] [-v {0,1,2,3}]
                                       [--settings SETTINGS]
                                       [--pythonpath PYTHONPATH] [--traceback]
                                       [--no-color]

    Save copies of data files from the most recently completed updatein a latest
    directory in the Django project's default file storage.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Raise on CommandError exceptions
      --no-color            Don't colorize the command output.

