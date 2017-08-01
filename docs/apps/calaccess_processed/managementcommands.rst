Management commands
===================

The processed-data app includes the following commands for refining data extracted and scraped from CAL-ACCESS. Specifically, the raw data is loaded into the following types of models:

* ``Filing`` models that surface the most recent version of data included on a campaign-finance filing form, schedule or line item (e.g., a `Form 460`_, its Schedule A or Line 1 on that schedule).
* ``FilingVersion`` models that surface every version of a campaign-finance filing form, schedule or line item.
* Models that implement the core data types of the `Open Civic Data specification`_ (e.g., ``Person``, ``Organization``, ``Post`` and ``Membership``).
*  Models that implement election-related data types that have been `provisionally included`_ in the Open Civic Data specification (e.g., ``Election``, ``CandidateContest`` and ``Candidacy``).

As with any Django app management command, these can be invoked on the command line or `called within your Python code`_.

.. note::

    Before using any of the commands below, make sure you need to download and extract the raw CAL-ACCESS data:

    .. code-block:: none

      $ python manage.py updatecalaccessrawdata

    And scrape supplementary data from the CAL-ACCESS website:

    .. code-block:: none

      $ python manage.py scrapecalaccess    

----------------------

processcalaccessdata
~~~~~~~~~~~~~~~~~~~~

This is the master command. It brings together all of the other management commands listed below to load data into processed CAL-ACCESS models.

If your Django project is configured for archiving (`details here`_), this command also will export a csv file for each loaded model.

Examples
````````

Running the entire routine is as simple as this.

.. code-block:: none

    $ python manage.py processcalaccessdata

If a previous processing job stalled for any reason, ``processcalaccessdata`` will pick up wherever you left off. You can override this behavior by invoking the ``force-restart`` option.

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


----------------------

archivecalaccessprocessedfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export and archive a .csv file for a given model.

Examples
````````
You must provide the ``model_name`` as the first and only positional argument. For example, here's how you archive the ``Form460Filing`` model:

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile Form460Filing

Or the ``Candidacy`` model, which is one Open Civic Data's election-related data types:

.. code-block:: none

    $ python manage.py archivecalaccessprocessedfile Candidacy


Options
```````

.. code-block:: none

    usage: manage.py archivecalaccessprocessedfile [-h] [--version] [-v {0,1,2,3}]
                                                   [--settings SETTINGS]
                                                   [--pythonpath PYTHONPATH]
                                                   [--traceback] [--no-color]
                                                   model_name

    Export and archive a .csv file for a given model.

    positional arguments:
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

Load the CAL-ACCESS ``Filing`` and ``FilingVersion`` models. A component of the master ``processcalaccessdata`` command.

If your Django project is configured for archiving (`details here`_), this command also will export a csv file for each loaded model.

Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py loadcalaccessfilings


This command will skip any ``Filing`` or ``FilingVersion`` models already loaded with raw data from the current CAL-ACCESS snapshot. You can override this behavior by invoking the ``force-restart`` option.

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

Load OCD elections models with data extracted and scraped from CAL-ACCESS. A component of the master ``processcalaccessdata`` command.

This command runs the following management commands, in order:

#. ``loadocdparties``
#. ``loadocdballotmeasureelections``
#. ``loadocdballotmeasurecontests``
#. ``loadocdretentioncontests``
#. ``loadocdcandidateelections``
#. ``loadocdcandidatecontests``
#. ``mergeocdpersonsbyfilerid``
#. ``loadocdcandidaciesfrom501s``
#. ``mergeocdpersonsbycontestandname``
#. ``loadocdincumbentofficeholders``

If your Django project is configured for archiving (`details here`_), this command also will export a csv file for each loaded model.

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

    Load OCD elections models with data extracted and scraped from CAL-ACCESS.

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

loadocdballotmeasureelections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the OCD ``Election`` model from the scraped ``PropositionElection`` model. A component of the ``loadocdelections`` command.

Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py loadocdballotmeasureelections


Options
```````

.. code-block:: none

    usage: manage.py loadocdballotmeasureelections [-h] [--version] [-v {0,1,2,3}]
                                                   [--settings SETTINGS]
                                                   [--pythonpath PYTHONPATH]
                                                   [--traceback] [--no-color]

    Load the OCD Election model from the scraped PropositionElection model

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

Load OCD ``BallotMeasureContest`` and related models with scraped CAL-ACCESS data. A component of the ``loadocdelections`` command.

.. note::

    Use ``loadocdballotmeasureelections`` before using ``loadocdballotmeasurecontests``.

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

    Load OCD BallotMeasureContest and related models with scraped CAL-ACCESS data

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

Load the OCD ``Election`` model with data from the scraped ``CandidateElection`` model. A component of the ``loadocdelections`` command.

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

    Load the OCD Election model with data from the scraped CandidateElection model.

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

Load the OCD ``CandidateContest`` and related models with scraped CAL-ACCESS data. A component of the ``loadocdelections`` command.

This command loads data from the ``IncumbentElection`` and ``CandidateElection`` models in ``calaccess_scraped``.

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

    Load the OCD CandidateContest and related models with scraped CAL-ACCESS data

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

Load the OCD ``Candidacy`` model with data extracted from the ``Form501Filing`` model. A component of the ``loadocdelections`` command.

This command fills in ``Candidacy`` records with data missing on the CAL-ACCESS website (e.g., the candidate's party in each contest). It also adds additional ``Candidacy`` records.

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

    Load the OCD Candidacy model with data extracted from the Form501Filing model.

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

Load the OCD ``Membership`` model with data from the scraped Incumbent model. A component of the ``loadocdelections`` command.

.. note::

    Use ``loadocdcandidateelections`` before using ``loadocdincumbentofficeholders``.

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

    Load the OCD Membership model with data from the scraped Incumbent model

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

Load OCD ``RetentionContest`` and related models with data scraped from CAL-ACCESS. A component of the ``loadocdelections`` command.

.. note::

    Use ``loadballotmeasureelections`` before using ``loadocdretentioncontests``.

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

    Load OCD RetentionContest and related models with data scraped from CAL-ACCESS

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

Load OCD ``Organization`` model with parties extracted from raw CAL-ACCESS data. A component of the ``loadocdelections`` command.

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

    Load OCD Organization model with parties extracted from raw CAL-ACCESS data.

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

Find and merge OCD ``Person`` records that share a name and ``CandidateContest``. A component of the ``loadocdelections`` command.


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

    Find and merge OCD Person records that share a name and CandidateContest

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

Find and merge OCD ``Person`` records that share the same CAL-ACCESS filer_id. A component of the ``loadocdelections`` command.

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

    Find and merge OCD Person records that share the same CAL-ACCESS filer_id

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


.. _called within your Python code: https://docs.djangoproject.com/en/1.10/ref/django-admin/#running-management-commands-from-your-code
.. _Form 460: https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/
.. _Form 497: https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f497/
.. _Open Civic Data specification: https://opencivicdata.readthedocs.io/en/latest/#
.. _provisionally included: https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html
.. _details here: /settings.html#calaccess-store-archive