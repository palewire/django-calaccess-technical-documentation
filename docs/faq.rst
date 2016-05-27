Frequently asked questions
==========================

Questions and answers about this project and the underlying the CAL-ACCESS database

----------------------

Why is all this necessary?
--------------------------

California’s jumbled, dirty and difficult campaign-finance database, known as CAL-ACCESS,
sprawls across 80 database tables and weighs in at more than 650 megabytes.

A significant effort is required to understand its esoteric structure and
prepare the records for meaningful analysis. 

That barrier blocks anyone seeking to interpret the information. The challenge of
untangling the database requires weeks of study and significant guesswork,
discouraging most analysts from daring—and raising the risk that those who do will make a critical error.

That is the problem we aim to solve by leading an open-source effort to perfect
the numerous transformations, filters and computer operations necessary to
refine the raw data into an easy-to-use product.

----------------------

What is the California Civic Data Coalition?
--------------------------------------------

The California Civic Data Coalition is a loosely coupled team of journalists from the Los Angeles Times Data Desk,
the Washington Post, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

The coalition was formed in 2014 by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ and Agustin Armendariz to lead the development of open-source software
that makes California's public data easier to access and analyze. The effort has drawn hundreds of contributions
from developers and journalists at dozens of competing news outlets.

Its primary focus is refining CAL-ACCESS, the jumbled, dirty and difficult government database that tracks
campaign finance and lobbying activity in California politics.

Read more at `californiacivicdata.org <http://www.californiacivicdata.org>`_.

----------------------

Who is funding the coalition's work?
-------------------------------------

In 2015 the coalition was `named a winner of the Knight News Challenge <http://www.californiacivicdata.org/2015/07/22/knight-news-challenge/>`_ and
awarded $250,000 in philanthropic funding from the Knight Foundation, the Democracy Fund,
the William and Flora Hewlett Foundation and the Rita Allen Foundation.

----------------------

How can I get in contact with the developers?
---------------------------------------------

Find us on the #california-civic-data channel of the `News Nerdery Slack <http://newsnerdery.org/>`_ or via the contact
options listed `here. <http://www.californiacivicdata.org/about>`_ Bug reports and pull requests are always welcome
`on GitHub <https://github.com/california-civic-data-coalition>`_.

----------------------

How far back does the CAL-ACCESS database go?
---------------------------------------------

According to an `FAQ document <https://www.documentcloud.org/documents/2711615-FAQ/pages/1.html>`_
provided by the California Secretary of State, electronic disclosure documents
started being filed in CAL-ACCESS on Jan. 1, 2000. Historical analysis of the database,
should start from that date, the documentation says.

----------------------

Do the daily exports include *all* tables in the CAL-ACCESS database?
---------------------------------------------------------------------

No. We've compared the list of tables in the daily exports to what's described in the `official documentation <https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb.html#document/p2>`_ provided by the Secretary of State, there as many 73 tables excluded from the daily exports.

Some of these missing tables have names or descriptions suggesting they could contain sensitive information, such as user credentials and bank account numbers. It's understandable that these tables would not be released.

However, many of these tables contain information that should be publicly available. For instance, there's a series of tables that describe elections, races and candidates that are not included in the daily exports, even though the list of candidates for the current election is `published <http://cal-access.ss.ca.gov/Campaign/Candidates/#assembly>`_ on the CAL-ACCESS website.

When we `reached out <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/62#issuecomment-58655390>`_ to the Secretary of State, asking that they include any elections-related tables in the daily exports, we were told that "[g]iven our current resource constraints, staff cannot modify the database export to include that other data."

Here's a sampling of missing tables we think should be made public:

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Description</th>
        </tr>
    </thead>
    <tbody valign="top">
        <tr>
            <td>CASH_RECON_REPORT_WRK</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table. Cox - 4/28/2000"</td>
        </tr>
        <tr>
            <td>CODE_LIST</td>
            <td>This table contains a list of CAL file codes. Examples include entity codes, office codes and expense codes</td>
        </tr>
        <tr>
            <td>CORRESPONDENCE</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table. Cox - 4/28/2000"</td>
        </tr>
        <tr>
            <td>DISCLOSURE_PROCEDURES</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table."</td>
        </tr>
        <tr>
            <td>ELECTION_CANDIDATES</td>
            <td>This table indicates if a candidate for a given race is an incumbent.</td>
        </tr>
        <tr>
            <td>ELECTION_LINKS</td>
            <td>No description</td>
        </tr>
        <tr>
            <td>ELECTION_RACES</td>
            <td>No description</td>
        </tr>
        <tr>
            <td>ELECTION_TYPES</td>
            <td>This table links election types and their descriptions.</td>
        </tr>
        <tr>
            <td>ELECTIONS</td>
            <td>No description</td>
        </tr>
        <tr>
            <td>ERRORS_AND_OMISSIONS</td>
            <td>This table contains results of audit checks and the validation process.</td>
        </tr>
        <tr>
            <td>FEDERAL_FORMS</td>
            <td>Table used to log reciept of federal filings.</td>
        </tr>
        <tr>
            <td>FEES</td>
            <td>Fees, descriptions and their value</td>
        </tr>
        <tr>
            <td>FILER_CORRESPONDENCE_BUILD2</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table."</td>
        </tr>
        <tr>
            <td>FILER_ELECTIONS</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table. He indicates it is for future use."</td>
        </tr>
        <tr>
            <td>FILER_NOTICE_GENERATION_DEF</td>
            <td>"J M needs to describe this table. He indicates it is for future use."</td>
        </tr>
        <tr>
            <td>FILER_OBLIGATIONS</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table. He indicates it is for future use."</td>
        </tr>
        <tr>
            <td>FILER_TYPES_TO_FORMS</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table. It is in his list of tables designed for future releases."</td>
        </tr>
        <tr>
            <td>FILING_ERROR_TYPES</td>
            <td>This lookup table provides a cross reference for errors and their and messages.</td>
        </tr>
        <tr>
            <td>FILING_ERRORS</td>
            <td>This table contains the errors assocated with a given filing and each of it's amendments.</td>
        </tr>
        <tr>
            <td>FILING_ID_TEMP</td>
            <td>No description</td>
        </tr>
        <tr>
            <td>FORM_CODES</td>
            <td>This lookup table assocates record types to forms.</td>
        </tr>
        <tr>
            <td>FORMS</td>
            <td>This table describes the form set.</td>
        </tr>
        <tr>
            <td>LATE_CONT_IND_EXP_REPORT</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table."</td>
        </tr>
        <tr>
            <td>LOCAL_FORMS</td>
            <td>This table is used to log reciept of local paper filings.</td>
        </tr>
        <tr>
            <td>PRD_DATA_AUDIT</td>
            <td>No description</td>
        </tr>
        <tr>
            <td>PRD_FINE_DETAIL</td>
            <td>Detail information on how a fine was calculated.</td>
        </tr>
        <tr>
            <td>PRD_FINES</td>
            <td>Fine summary data table.</td>
        </tr>
        <tr>
            <td>PRD_LIMITS</td>
            <td>Table description contains this mysterious comment: "J M needs to describe this table."</td>
        </tr>
        <tr>
            <td>PRD_WAIVERS</td>
            <td>Table description contains this mysterious comment: "J Mo needs to describe this table."</td>
        </tr>
        <tr>
            <td>TVIEW_CONTRIBUTIONS3</td>
            <td>Campaign Disclosure reporting tables. "Need to get DH's Documentation to describe."</td>
        </tr>
    </tbody>
    </table>


----------------------


How do the Django applications fit together?
--------------------------------------------

The django-calaccess-raw-data application is intended as the base layer below more sophisticated apps,
like django-calaccess-processed-data, that transform the source data and load it into simplified models to serve as a
platform for investigative analysis.


Will django-calaccess-raw-data load *all* of the CAL-ACCESS data?
-----------------------------------------------------------------

No. The raw data provided by the state contains some errors in how values are escaped, quoted and delimited. The result is that a small number of records we
cannot yet automatically parse are lost during the loading process.

However, according to our own `tracking information <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/tracking.html>`_,
99.9998% of records in the downloaded source file will be loaded into the database.

For more information checkout:

* The `reportcalaccessrawdata <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/managementcommands.html#reportcalaccessrawdata>`_ command, which runs a several checks and produces a report on the current state of the CAL-ACCESS data
* The `list <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/calaccess_raw_files_report.csv>`_ of all CAL-ACCESS raw data files, including record and column counts at each stage of the process (this .CSV file is one of the outputs of ``reportcalaccessrawdata``)
* Records that could not be parsed by the ``cleancalaccessrawfile`` command are in ``<myproject>/data/log``

----------------------


Does django-calaccess-raw-data modify the source data?
------------------------------------------------------

We make every effort to carefully parse and load the bulk CAL-ACCESS data from the state "as is." Therefore, any undocumented modification of the data made during this process is considered a bug in the software.

Here's our one exception: We truncate the time part of any datetime field in the raw data, and load these into our models as DateFields. We consider this modification to be of little consequence since, for the most part, these raw datetime fields are effectively date fields anyway, with a time part of 12:00:00 AM for every value. Based on our own inspections of the raw data (details found `here <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/1457>`_), very little information is being lost and whatever is lost has questionable utility.

----------------------


Why does django-calaccess-raw-data use loading techniques not supported by Django?
----------------------------------------------------------------------------------

Because the CAL-ACCESS database is huge. With more than 35 million records sprawled across 76 tables,
it can take a long time to load into a database using `the standard Django tools <https://docs.djangoproject.com/es/1.9/topics/db/queries/#creating-objects>`_,
which insert one record at a time. In our early testing, it took as long as 24 hours to load all of CAL-ACCESS
into a database on a standard laptop computer.

To speed things up, our loading commands take advantage of the built-in bulk loading tools offered by PostgreSQL and MySQL,
which are not currently included in Django's system. These tools (``COPY`` in PostgreSQL and ``LOAD DATA INFILE`` in MySQL) insert CSV files from the file system
directly into the database in a small fraction of the time it would take to load them row by row.

As part of developing these tools we released `django-postgres-copy <http://django-postgres-copy.californiacivicdata.org/en/latest/>`_, a Django extension
that makes it easier for us and other developers to work with these valuable tools.

----------------------


Why does django-calaccess-raw-data only work with PostgreSQL and MySQL databases?
------------------------------------------------------------------------------------

Because of the answer above. To run our loading routines in an acceptable amount of time, we
need to take advantage of bulk file loading tools not currently supported by Django.

So far, we have only written custom loading routines for MySQL and PostgreSQL. We would
welcome contributions that would expand our database support to other systems, like SQLite
and Microsoft SQL Server. But we haven't got there yet.

----------------------

.. _faq-multi-databases:

Do I have to load the CAL-ACCESS data into my default database?
---------------------------------------------------------------

No, django-calaccess-raw-data supports the use of automatic database routing,
which Django's own documentation describes as "the easiest way to use multiple databases".

If you fall into this category, first of all, be sure you've carefully read
through Django's `multiple databases <https://docs.djangoproject.com/en/1.9/topics/db/multi-db/>`_ topic guide.

Next, configure your additional databases in ``settings.py``. Let's assume you want
two PostgreSQL databases: One for all CAL-ACCESS data called ``calaccess_raw``, and a default ``my_project`` database for everything else:

.. code-block:: python

    DATABASES = {
        'default': {
            'NAME': 'my_project',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '5432'
        },
        'calaccess_raw': {
            'NAME': 'calaccess',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your-username-here',
            'PASSWORD': 'your-password-here',
            'HOST': 'localhost',
            'PORT': '5432'
        },
    }

Then, create a ``routers.py`` file in your Django project's directory (same place as ``manage.py`` and ``settings.py``). Following from the above example, here's how you could implement a router to send calaccess-raw model data to their own database and everything else to ``default``:

.. code-block:: python

    class ExampleRouter(object):
        """
        Send calaccess_raw models to their own db. Everything else to default.
        """

        def get_db(self, model=None, app_label=None):
            app_label = app_label or model._meta.app_label
            if app_label == 'calaccess_raw'
                db_label = 'calaccess_raw'
            else:
                db_label = 'default'
            return db_label

        def db_for_read(self, model, **hints):
            """
            Attempts to read calaccess_raw models go to calaccess_raw db.
            """
            return self.get_db(model=model)

        def db_for_write(self, model, **hints):
            """
            Attempts to write calaccess_raw models go to calaccess_raw db.
            """
            return self.get_db(model=model)

        def allow_relation(self, obj1, obj2, **hints):
            """
            Allow relations if a model in the calaccess_raw app is involved.
            """
            return self.get_db(model=obj1) == self.get_db(model=obj2)

        def allow_migrate(self, db, app_label, model=None, **hints):
            """
            Make sure the calaccess_raw app only appears in the calaccess_raw
            database.
            """
            intended_db = self.get_db(app_label=app_label)
            return (db == intended_db) or (db == 'default' and intended_db is None)

Finally, configure the router in ``setting.py``:

.. code-block:: python

        DATABASE_ROUTERS = ['example.routers.ExampleRouter']

And everything should be ready.
