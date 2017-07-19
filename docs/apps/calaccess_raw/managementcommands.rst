Management commands
===================

The raw-data app includes the following commands for processing and verifying the raw data released in the CAL-ACCESS `nightly exports <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_.

As with any Django app management command, these can be invoked on the command line or `called within your Python code <https://docs.djangoproject.com/en/1.10/ref/django-admin/#running-management-commands-from-your-code>`_.

----------------------


updatecalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~~

This is the master command. It brings together all of the other management commands listed below to download, unzip, clean and load the latest snapshot of the CAL-ACCESS database.

Examples
````````

Running the entire routine is as simple as this.

.. code-block:: sh

    $ python manage.py updatecalaccessrawdata

This command will either:

* Update your copy of the CAL-ACCESS data to the latest snapshot on the California Secretary of State's website
* Or complete your previously interrputed update, if possible.

You can skip the download's confirmation prompt using Django's standard ``--noinput`` option.

.. code-block:: sh

    $ python manage.py updatecalaccessrawdata --noinput

The source files downloaded as part of the process will be deleted unless the ``--keep-files``
option is provided.

.. code-block:: sh

    $ python manage.py updatecalaccessrawdata --keep-files

The other options are below.

Options
```````

.. code-block:: sh

    usage: manage.py updatecalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [--keep-files] [--noinput]
                                            [-a APP_NAME]

    Download, unzip, clean and load the latest CAL-ACCESS database ZIP

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
      --noinput             Update or resume previous update without asking
                            permission
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app with models into which data will be
                            imported (if not calaccess_raw)

.. note::
    The ``updatecalaccessrawdata`` command overwrites the previously downloaded, extracted and cleaned files in the application's download directory.

----------------------


cleancalaccessrawfile
~~~~~~~~~~~~~~~~~~~~~

Clean a source CAL-ACCESS TSV file and reformat it as a CSV. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

Provide the name of the TSV file you would like to process. The command will
attempt to find it in the application's download directory.

.. code-block:: sh

    $ python manage.py cleancalaccessrawfile RCPT_CD.TSV

The original TSV file will be deleted in favor of the new CSV unless the ``--keep-file``
option is provided.

.. code-block:: sh

    $ python manage.py cleancalaccessrawfile RCPT_CD.TSV --keep-file

Options
```````

.. code-block:: sh

    usage: manage.py cleancalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color] [--keep-file]
                                           file_name

    Clean a source CAL-ACCESS TSV file and reformat it as a CSV

    positional arguments:
      file_name             Name of the TSV file to be cleaned and discarded for a
                            CSV

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
      --keep-file          Keep original TSV file

.. note::

    The ``cleancalaccessrawfile`` command overwrites the CSV files previously processed from the original TSV files.

----------------------


downloadcalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest CAL-ACCESS database ZIP. A component of the master ``updatecalaccessrawdata`` command.

Examples
````````

Here is how to run the command.

.. code-block:: sh

    $ python manage.py downloadcalaccessrawdata

You will then see a prompt with the release date and size of the latest zip of raw CAL-ACCESS data files available to download from the California Secretary of State.

If your previous download did not complete *and* the same snapshot is still available to download, you will be prompted to resume your previous download.

You can skip the download's confirmation prompt using Django's standard ``--noinput`` option.

.. code-block:: sh

    $ python manage.py downloadcalaccessrawdata --noinput

The other options are below.

The server hosting the ZIP doesn't always provide the most up-to-date resource (as we have `documented <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/1487>`_). As such, a ``CommandError`` will be raised under any of the following conditions:

* If ``downloadcalaccessrawdata`` is not called from the command-line (presumably, then, it was called by ``updatecalaccessrawdata``), and the ``RawDataVersion`` instance of the download command doesn't match the most recently started update.
* If the ``ETag`` in the initial HEAD request made by ``downloadcalaccessrawdata`` does not match the ``ETag`` in the subsequent GET request.
* If the actual size of the ZIP does not match the value of the ``Content-Length`` in the HEAD response.

Options
```````

.. code-block:: sh

    usage: manage.py downloadcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color]
                                              [--noinput] [--force-restart]

    Download the latest CAL-ACCESS database ZIP

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
      --noinput             Download the ZIP archive without asking permission
      --force-restart, --restart
                            Force re-start (overrides auto-resume).

.. note::

    The ``downloadcalaccessrawdata`` command overwrites the previously downloaded zip file.

----------------------


extractcalaccessrawfiles
~~~~~~~~~~~~~~~~~~~~~~~~

Extract the CAL-ACCESS raw data files from downloaded ZIP. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

Here is how to run the command.

.. code-block:: sh

    $ python manage.py extractcalaccessrawfiles


The downloaded zip file will be deleted unless the ``--keep-files`` option is provided.

.. code-block:: sh

    $ python manage.py extractcalaccessrawfiles --keep-files


Options
```````

.. code-block:: sh

    usage: manage.py extractcalaccessrawfiles [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color]
                                              [--keep-files]

    Extract the CAL-ACCESS raw data files from the database export ZIP

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
      --keep-files          Keep downloaded zipped files

.. note::

    The ``extractcalaccessrawfiles`` command overwrites the previously extracted TSV files.

----------------------


loadcalaccessrawfile
~~~~~~~~~~~~~~~~~~~~

Load clean CAL-ACCESS CSV file into a database model. A component of the
master ``updatecalaccessrawdata`` command.

Examples
````````

The command expects the name of the Django database model where the file
will be loaded.

.. code-block:: sh

    $ python manage.py loadcalaccessrawfile RcptCd

The model will attempt to load its default CSV file unless one is provided with the ``--csv`` argument.

.. code-block:: sh

    $ python manage.py loadcalaccessrawfile RcptCd --csv=/home/jerry/Data/MyFile.csv

Options
```````

.. code-block:: sh

    usage: manage.py loadcalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                          [--settings SETTINGS]
                                          [--pythonpath PYTHONPATH] [--traceback]
                                          [--no-color] [--c CSV] [--keep-file]
                                          [-a APP_NAME]
                                          model_name

    Load clean CAL-ACCESS CSV file into a database model

    positional arguments:
      model_name            Name of the model into which data will be loaded

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
      --c CSV, --csv CSV    Path to comma-delimited file to be loaded. Defaults to
                            one associated with model.
      --keep-file          Keep clean CSV file after loading
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app with models into which data will be
                            imported (if other not calaccess_raw)

.. note::

    The ``loadcalaccessrawfile`` command deletes any data previously loaded into the calaccess_raw models before loading in the current data.

----------------------


reportcalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~~

Generate report outlining the number / proportion of files / records cleaned and loaded.

The report will be saved as a CSV file in the application's download directory.

Examples
````````

.. code-block:: sh

    $ python manage.py reportcalaccessrawfile

Options
```````

.. code-block:: sh

    usage: manage.py reportcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]

    Generate report outlining the number / proportion of files / records cleaned
    and loaded

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


totalcalaccessrawdata
~~~~~~~~~~~~~~~~~~~~~

Print table and record counts from the CAL-ACCESS raw database

Examples
````````

.. code-block:: sh

    $ python manage.py totalcalaccessrawdata

Options
```````

.. code-block:: sh

    usage: manage.py totalcalaccessrawdata [-h] [--version] [-v {0,1,2,3}]
                                           [--settings SETTINGS]
                                           [--pythonpath PYTHONPATH] [--traceback]
                                           [--no-color]

    Print table and record counts from the CAL-ACCESS raw database

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

----------------------


verifycalaccessrawfile
~~~~~~~~~~~~~~~~~~~~~~

Logs row count of given model and compares against line count in cleaned CSV.

Examples
````````

The command expects to be provided with the name of a Django model to analyze.

.. code-block:: sh

    $ python manage.py verifycalaccessrawfile RcptCd

Options
```````

.. code-block:: sh

    usage: manage.py verifycalaccessrawfile [-h] [--version] [-v {0,1,2,3}]
                                            [--settings SETTINGS]
                                            [--pythonpath PYTHONPATH]
                                            [--traceback] [--no-color]
                                            [-a APP_NAME]
                                            model_name

    Logs row count of given model and compares against line count in cleaned CSV

    positional arguments:
      model_name            Name of model to verify

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
      -a APP_NAME, --app-name APP_NAME
                            Name of Django app with models into which data will be
                            imported (if other not calaccess_raw)
