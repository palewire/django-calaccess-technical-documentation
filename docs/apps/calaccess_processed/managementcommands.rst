Management commands
===================

The processed-data app includes the following commands for loading the raw CAL-ACCESS data into simplified models.

As with any Django app management command, these can be invoked on the command line or `called within your Python code <https://docs.djangoproject.com/en/1.10/ref/django-admin/#running-management-commands-from-your-code>`_.

----------------------

processcalaccessdata
~~~~~~~~~~~~~~~~~~~~

Load data into processed CAL-ACCESS models, archive processed files and ZIP.

Examples
````````

Running the entire routine is as simple as this.

.. code-block:: none

    $ python manage.py processcalaccessdata


Options
```````

.. code-block:: none

    usage: manage.py processcalaccessdata [-h] [--version] [-v {0,1,2,3}]
                                          [--settings SETTINGS]
                                          [--pythonpath PYTHONPATH] [--traceback]
                                          [--no-color] [--force-restart]
                                          [--no-scrape]

    Load data into processed CAL-ACCESS models, archive processed files and ZIP.

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
      --force-restart, --restart
                            Force re-start (overrides auto-resume).
      --no-scrape           Skip scraping.


----------------------

archivecalaccessprocessedfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export and archive a .csv file for a given model.

Examples
````````

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile


Options
```````

.. code-block:: none

    usage: manage.py archivecalaccessprocessedfile [-h] [--version] [-v {0,1,2,3}]
                                                   [--settings SETTINGS]
                                                   [--pythonpath PYTHONPATH]
                                                   [--traceback] [--no-color]
                                                   app_name model_name

    Export and archive a .csv file for a given model.

    positional arguments:
      app_name              Name of the app with the model
      model_name            Name of the model to archive

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


loadcalaccessfilings
~~~~~~~~~~~~~~~~~~~~

Load and archive the CAL-ACCESS Filing and FilingVersion models.

Examples
````````

.. code-block:: none

    $ python manage.py loadcalaccessfilings


Options
```````

.. code-block:: none

    usage: manage.py loadcalaccessfilings [-h] [--version] [-v {0,1,2,3}]
                                          [--settings SETTINGS]
                                          [--pythonpath PYTHONPATH] [--traceback]
                                          [--no-color] [--force-restart]

    Load and archive the CAL-ACCESS Filing and FilingVersion models.

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
      --force-restart, --restart
                            Force re-start (overrides auto-resume).


loadocdelections
~~~~~~~~~~~~~~~~

Load data extracted from scrape and raw data snapshot into OCD elections models.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdelections


Options
```````

.. code-block:: none

    usage: manage.py loadocdelections [-h] [--version] [-v {0,1,2,3}]
                                      [--settings SETTINGS]
                                      [--pythonpath PYTHONPATH] [--traceback]
                                      [--no-color]

    Load data extracted from scrape and raw data snapshot into OCD elections models.

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


loadocdballotmeasurecontests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load OCD BallotMeasureContest and related models with data scraped from the CAL-ACCESS website.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdballotmeasurecontests


Options
```````

.. code-block:: none

    usage: manage.py loadocdballotmeasurecontests [-h] [--version] [-v {0,1,2,3}]
                                                  [--settings SETTINGS]
                                                  [--pythonpath PYTHONPATH]
                                                  [--traceback] [--no-color]
                                                  [--flush]

    Load OCD BallotMeasureContest and related models with data scraped from the CAL-ACCESS website

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
      --flush               Flush the database tables filled by this command.


loadocdcandidaciesfrom501s
~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the Candidacy models from records extracted from Form501Filings.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdcandidaciesfrom501s


Options
```````

.. code-block:: none

    usage: manage.py loadocdcandidaciesfrom501s [-h] [--version] [-v {0,1,2,3}]
                                                [--settings SETTINGS]
                                                [--pythonpath PYTHONPATH]
                                                [--traceback] [--no-color]

    Load the Candidacy models from records extracted from Form501Filings.

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


loadocdcandidatecontests
~~~~~~~~~~~~~~~~~~~~~~~~

Examples
````````

Load CandidateContest and related models with data scraped from the CAL-ACCESS website.

.. code-block:: none

    $ python manage.py loadocdcandidatecontests


Options
```````

.. code-block:: none

    usage: manage.py loadocdcandidatecontests [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color] [--flush]

    Load CandidateContest and related models with data scraped from the CAL-ACCESS website.

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
      --flush               Flush the database tables filled by this command.


loadocdcandidateelections
~~~~~~~~~~~~~~~~~~~~~~~~~

Load OCD Election models with data scraped from the CAL-ACCESS website.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdcandidateelections


Options
```````

.. code-block:: none

    usage: manage.py loadocdcandidateelections [-h] [--version] [-v {0,1,2,3}]
                                               [--settings SETTINGS]
                                               [--pythonpath PYTHONPATH]
                                               [--traceback] [--no-color]
                                               [--flush]

    Load OCD Election models with data scraped from the CAL-ACCESS website.

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
      --flush               Flush the database tables filled by this command.


loadocdincumbentofficeholders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load incumbent candidate data scraped from the CAL-ACCESS website into OCD models.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdincumbentofficeholders


Options
```````

.. code-block:: none

    usage: manage.py loadocdincumbentofficeholders [-h] [--version] [-v {0,1,2,3}]
                                                   [--settings SETTINGS]
                                                   [--pythonpath PYTHONPATH]
                                                   [--traceback] [--no-color]

    Load incumbent candidate data scraped from the CAL-ACCESS website into OCD models.

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


loadocdretentioncontests
~~~~~~~~~~~~~~~~~~~~~~~~

Load OCD RetentionContest and related models with data scraped from the CAL-ACCESS website.

Examples
````````

.. code-block:: none

    $ python manage.py loadocdretentioncontests


Options
```````

.. code-block:: none

    usage: manage.py loadocdretentioncontests [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color] [--flush]

    Load OCD RetentionContest and related models with data scraped from the CAL-ACCESS website.

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
      --flush               Flush the database tables filled by this command.


loadocdparties
~~~~~~~~~~~~~~

Examples
````````

.. code-block:: none

    $ python manage.py loadocdparties


Options
```````

.. code-block:: none

    usage: manage.py loadocdparties [-h] [--version] [-v {0,1,2,3}]
                                    [--settings SETTINGS]
                                    [--pythonpath PYTHONPATH] [--traceback]
                                    [--no-color] [--flush]

    Load OCD Party model from LOOKUP_CODES_CD table in raw CAL-ACCESS data

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
      --flush               Flush the database tables filled by this command.


mergeocdpersonsbycontestandname
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Merge duplicate Candidacies within the same CandidateContest.

Examples
````````

.. code-block:: none

    $ python manage.py mergeocdpersonsbycontestandname


Options
```````

.. code-block:: none

    usage: manage.py mergeocdpersonsbycontestandname [-h] [--version]
                                                     [-v {0,1,2,3}]
                                                     [--settings SETTINGS]
                                                     [--pythonpath PYTHONPATH]
                                                     [--traceback] [--no-color]

    Merge duplicate Candidacies within the same CandidateContest.

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


mergeocdpersonsbyfilerid
~~~~~~~~~~~~~~~~~~~~~~~~

Merge Persons that share the same CAL-ACCESS filer_id.

Examples
````````

.. code-block:: none

    $ python manage.py mergeocdpersonsbyfilerid


Options
```````

.. code-block:: none

    usage: manage.py mergeocdpersonsbyfilerid [-h] [--version] [-v {0,1,2,3}]
                                              [--settings SETTINGS]
                                              [--pythonpath PYTHONPATH]
                                              [--traceback] [--no-color]

    Merge Persons that share the same CAL-ACCESS filer_id

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
