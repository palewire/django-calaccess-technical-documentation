Management commands
===================

The processed-data app includes the following commands for refining the raw CAL-ACCESS data. Specifically, the raw data is loaded into the following types of models:

* ``Filing`` models that surface the most recent version of data included on a campaign-finance filing form, schedule or line item (e.g., a `Form 460`_, its Schedule A or Line 1 on that schedule).
* ``FilingVersion`` models that surface every version of campaign-finance filing form, schedule or line item.
* Models that implement the core data types of the `Open Civic Data specification`_ (e.g., ``Person``, ``Organization``, ``Post`` and `Membership``).
*  Models that implement election-related data types that have been `provisionally included`_ in the Open Civic Data specification (e.g., `Election`, `CandidateContest` and `Candidacy`).

As with any Django app management command, these can be invoked on the command line or `called within your Python code <https://docs.djangoproject.com/en/1.10/ref/django-admin/#running-management-commands-from-your-code>`_.

.. note::

    Before using any of the commands below, make sure you need to download and extract the raw CAL-ACCESS data:

    .. code-block:: none

      $ python manage.py updatecalaccessrawdata

    And scraped supplementary data from the CAL-ACCESS website:

    .. code-block:: none

      $ python manage.py scrapecalaccess    

----------------------

processcalaccessdata
~~~~~~~~~~~~~~~~~~~~

This is the master command. It brings together all of the other management commands listed below to load data into processed CAL-ACCESS models.

This command also exports a csv file for each model it loads, if you're Django project is configured for archiving (`read more`_).

Examples
````````

Running the entire routine is as simple as this.

.. code-block:: none

    $ python manage.py processcalaccessdata

If a previous processing attempt stalled for any reason, ``processcalaccessdata`` will pick up wherever you left off. You can override this behavior by invoking the ``force-restart`` option.

.. code-block:: none

    $ python manage.py processcalaccessdata --force-restart


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

You must pass in the ``app_name`` and ``model_name`` as the first two positional arguments. For example, here's how you archive the ``Form460Filing`` model:

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile calaccess_processed Form460Filing

Or the ``Person`` model, which is one Open Civic Data's core data types:

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile core Person

Pass ``elections`` for the OCD election-related data types (e.g., ``Candidacy``):

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile elections Candidacy


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

----------------------

loadcalaccessfilings
~~~~~~~~~~~~~~~~~~~~

Load the CAL-ACCESS ``Filing`` and ``FilingVersion`` models.

This command also exports a csv file for each model it loads, if you're Django project is configured for archiving (`read more`_).

Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py loadcalaccessfilings


This command will skip any `Filing` or `FilingVersion` models already loaded with raw data from the current CAL-ACCESS snapshot. You can override this behavior by invoking the ``force-restart`` option.

.. code-block:: none

    $ python manage.py processcalaccessdata --force-restart


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

----------------------

loadocdelections
~~~~~~~~~~~~~~~~

Load data extracted from scraped and raw data snapshot into OCD elections models.

This command runs the following management commands, in order:

#. ``loadocdparties``
#. ``loadocdballotmeasurecontests``
#. ``loadocdretentioncontests``
#. ``loadocdcandidateelections``
#. ``loadocdcandidatecontests``
#. ``mergeocdpersonsbyfilerid``
#. ``loadocdcandidaciesfrom501s``
#. ``mergeocdpersonsbycontestandname``
#. ``loadocdincumbentofficeholders``

This command also exports a csv file for each model it loads, if you're Django project is configured for archiving (`read more`_).

Examples
````````

Here is how to run the command.

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


----------------------

loadocdballotmeasurecontests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the OCD ``BallotMeasureContest`` and related models with data scraped from the CAL-ACCESS website.

Examples
````````

Here is how to run the command.

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


----------------------

loadocdcandidateelections
~~~~~~~~~~~~~~~~~~~~~~~~~

Load OCD ``Election`` models with candidate-related data scraped from the CAL-ACCESS website.

Examples
````````

Here is how to run the command.


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


----------------------

loadocdcandidatecontests
~~~~~~~~~~~~~~~~~~~~~~~~

Load the OCD ``CandidateContest`` and related models with data scraped from the CAL-ACCESS website.

.. note::

    Use ``loadocdcandidateelections`` before using ``loadocdcandidatecontests``.

Examples
````````

Here is how to run the command.

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


----------------------

loadocdcandidaciesfrom501s
~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the OCD ``Candidacy`` model from records extracted from ``Form501Filing`` records.

This command fills in `Candidacy` records with data missing on the CAL-ACCESS website (e.g., the candidate's party in each contest). It also adds additional `Candidacy` records.

Examples
````````

Here is how to run the command.

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


----------------------

loadocdincumbentofficeholders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load incumbent candidate data scraped from the CAL-ACCESS website into OCD models.

Examples
````````

Here is how to run the command.

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


----------------------

loadocdretentioncontests
~~~~~~~~~~~~~~~~~~~~~~~~

Load OCD RetentionContest and related models with data scraped from the CAL-ACCESS website.

Examples
````````

Here is how to run the command.

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


----------------------

loadocdparties
~~~~~~~~~~~~~~

Load OCD ``Organization`` model with political parties from ``LOOKUP_CODES_CD`` table in raw CAL-ACCESS data.

Examples
````````

Here is how to run the command.

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

Find and merge ``Person`` records linked that share a name and ``CandidateContest``.


Examples
````````

Here is how to run the command.

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

Find and merge `Person` records that share the same CAL-ACCESS filer_id.

Examples
````````

Here is how to run the command.

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


.. _Form 460: https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/
.. _Form 497: https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f497/
.. _Open Civic Data specification: https://opencivicdata.readthedocs.io/en/latest/#
.. _provisionally included: https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html
.. _read more: /settings.html#calaccess-store-archive