Management commands
===================

The scraped-data app includes the following commands for scraping campaign finance data from the `CAL-ACCESS <http://www.sos.ca.gov/prd/cal-access/>`__ website.

As with any Django app management command, these can be invoked on the command line or `called within your Python code <https://docs.djangoproject.com/en/1.10/ref/django-admin/#running-management-commands-from-your-code>`_.

Raw content downloaded from CAL-ACCESS is stored in ``.scraper_cache/``, found in the directory specified by ``BASE_DIR`` in your Django project's `settings <https://docs.djangoproject.com/en/1.11/topics/settings/>`_.

----------------------


scrapecalaccess
~~~~~~~~~~~~~~~

This command runs the following management commands, in order:

1. ``scrapecalaccesspropositions``
2. ``scrapecalaccesscandidates``
3. ``scrapecalaccessincumbents``

These commands are defined in more detail below.

Examples
````````

The default behavior of the scraper commands is to avoid excessive downloads. As such, a CAL-ACCESS web page's content will only be downloaded if:

1. The page's content isn't cached; or
2. The byte size of the cached content differs from the size of the content on the server (as specified in ``Content-Length`` header).

You can override this default behavior by invoking the ``force-download`` option:

.. code-block:: none

    $ python manage.py scrapecalaccess --force-download

Alternatively, you can avoid making *any* network requests, parsing and storing data only from previously cached content. That's what you get by invoking the ``--cache-only`` option:

.. code-block:: none

    $ python manage.py scrapecalaccess --cache-only

By default, data saved from previous scrapes is preserved, or you can invoke the ``--flush`` option to start over with empty data tables:

.. code-block:: none

    $ python manage.py scrapecalaccess --flush


Options
```````

.. code-block:: none

    usage: manage.py scrapecalaccess [-h] [--version] [-v {0,1,2,3}]
                                     [--settings SETTINGS]
                                     [--pythonpath PYTHONPATH] [--traceback]
                                     [--no-color] [--flush] [--force-download]
                                     [--cache-only]

    Run all scraper commands

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
      --flush               Flush database tables
      --force-download      Force the scraper to download URLs even if they are cached
      --cache-only          Skip the scraper's update checks. Use only cached
                            files.


----------------------


scrapecalaccesscandidates
~~~~~~~~~~~~~~~~~~~~~~~~~

Scrape certified candidates for each election on the CAL-ACCESS site. A component of the ``scrapecalaccess`` command.

This command requests and parses content from the "certified" view of the ``Campaign/Candidates/list.aspx`` page (e.g., the `2016 General <http://cal-access.sos.ca.gov/Campaign/Candidates/list.aspx?view=certified&electNav=65>`_ certified candidates). Data parsed from these pages' content are saved in the ``CandidateElection`` and ``Candidate`` models.

Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py scrapecalaccesscandidates


Options
```````

.. code-block:: none

    usage: manage.py scrapecalaccesscandidates [-h] [--version] [-v {0,1,2,3}]
                                               [--settings SETTINGS]
                                               [--pythonpath PYTHONPATH]
                                               [--traceback] [--no-color]
                                               [--flush] [--force-download]
                                               [--cache-only]

    Scrape certified candidates for each election on the CAL-ACCESS site.

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
      --flush               Flush database tables
      --force-download      Force the scraper to download URLs even if they are
                            cached
      --cache-only          Skip the scraper's update checks. Use only cached
                            files.


----------------------


scrapecalaccesscandidatecommittees
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scrape each candidate's committees from the CAL-ACCESS site. 

This command requests and parses content from the "general" view of the ``Campaign/Candidates/Detail.aspx`` page for candidate's most recent "session" (e.g., `Edward T. Gaines <http://cal-access.sos.ca.gov/Campaign/Candidates/Detail.aspx?id=1265444&view=general&session=2017>`_ general information leading up to the 2016 General election). Data parsed from these pages' content are saved in the ``CandidateCommittee`` model.

.. note::

    The ``scrapecalaccesscandidatecommittees`` command is not currently included in the ``scrapecalaccess`` because of the number of CAL-ACCESS web pages it scrapes. This may change in the future.


Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py scrapecalaccesscandidatecommittees


Options
```````

.. code-block:: none

    usage: manage.py scrapecalaccesscandidatecommittees [-h] [--version]
                                                        [-v {0,1,2,3}]
                                                        [--settings SETTINGS]
                                                        [--pythonpath PYTHONPATH]
                                                        [--traceback] [--no-color]
                                                        [--flush]
                                                        [--force-download]
                                                        [--cache-only]

    Scrape each candidate's committees from the CAL-ACCESS site.

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
      --flush               Flush database tables
      --force-download      Force the scraper to download URLs even if they are
                            cached
      --cache-only          Skip the scraper's update checks. Use only cached
                            files.


----------------------


scrapecalaccessincumbents
~~~~~~~~~~~~~~~~~~~~~~~~~

Scrape list of incumbent state officials for each election on CAL-ACCESS site. A component of the ``scrapecalaccess`` command.

This command requests and parses content from the "incumbent" view of the ``Campaign/Candidates/list.aspx`` page (e.g., the `2017-2018 General <http://cal-access.sos.ca.gov/Campaign/Candidates/list.aspx?view=incumbent&session=2017>`_ incumbents). Data parsed from these pages' content are saved in the ``IncumbentElection`` and ``Incumbent`` models.

Examples
````````

Here is how to run the command.

.. code-block:: none

    $ python manage.py scrapecalaccessincumbents


Options
```````

.. code-block:: none

    usage: manage.py scrapecalaccessincumbents [-h] [--version] [-v {0,1,2,3}]
                                               [--settings SETTINGS]
                                               [--pythonpath PYTHONPATH]
                                               [--traceback] [--no-color]
                                               [--flush] [--force-download]
                                               [--cache-only]

    Scrape list of incumbent state officials for each election on CAL-ACCESS site.

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
      --flush               Flush database tables
      --force-download      Force the scraper to download URLs even if they are
                            cached
      --cache-only          Skip the scraper's update checks. Use only cached
                            files.


----------------------


scrapecalaccesspropositions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scrape links between filers and propositions from the official CAL-ACCESS site. A component of the ``scrapecalaccess`` command.

This command requests and parses content from the ``Campaign/Measures/list.aspx`` page (e.g., the `2015-2016 <http://cal-access.sos.ca.gov/Campaign/Measures/list.aspx?session=2015>`_ propositions and ballot measures) and "general" view of each propositions ``Campaign/Measures/Detail.aspx`` page (e.g., `Prop 60 <http://cal-access.sos.ca.gov/Campaign/Measures/Detail.aspx?id=1376195&session=2015&view=general>`_'s general information). Data parsed from these pages' content are saved in the ``PropositionElection``, ``Proposition`` and ``PropositionCommittee`` models.

Examples
````````



.. code-block:: none

    $ python manage.py scrapecalaccesspropositions


Options
```````

.. code-block:: none

    usage: manage.py scrapecalaccesspropositions [-h] [--version] [-v {0,1,2,3}]
                                                 [--settings SETTINGS]
                                                 [--pythonpath PYTHONPATH]
                                                 [--traceback] [--no-color]
                                                 [--flush] [--force-download]
                                                 [--cache-only]

    Scrape links between filers and propositions from the official CAL-ACCESS
    site.

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
      --flush               Flush database tables
      --force-download      Force the scraper to download URLs even if they are
                            cached
      --cache-only          Skip the scraper's update checks. Use only cached
                            files.
