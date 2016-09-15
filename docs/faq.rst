Frequently asked questions
==========================

Questions and answers about the technical aspects of our work. A broader FAQ about the CAL-ACCESS database
and our work with it can be found `here <http://calaccess.californiacivicdata.org/documentation/>`_.

----------------------

How do the Django applications fit together?
--------------------------------------------

The :doc:`/apps/calaccess_raw` application is intended as the base layer below more sophisticated apps,
like :doc:`/apps/calaccess_processed`, that transform the source data and load it into simplified models to serve as a
platform for investigative analysis.

----------------------


Why does django-calaccess-raw-data use loading techniques not supported by Django?
----------------------------------------------------------------------------------

Because the CAL-ACCESS database is huge. With more than 35 million records sprawled across 80 tables,
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

No, :doc:`/apps/calaccess_raw` supports the use of automatic database routing,
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
