Contribute to django-calaccess-downloads-website
================================================

This walkthrough is for developers who want to contribute to :doc:`/apps/calaccess_downloads_site`, a open-source archive of
campaign-finance and lobbying-disclosure data from the California Secretary of State's :doc:`CAL-ACCESS </calaccess>` database.

It will show you how to install the source code of this application to fix bugs, develop new features and deploy an archive to the Internet
using Amazon Web Services.

---------------

-----------------------------------
Preparing a development environment
-----------------------------------

In order to contribute you first need to set up a local development environment by installing the source code and configuring a few settings.

While not required, we recommend that development be done within a contained virtual environment.

One way to accomplish that is with a two related Python packages: ``virtualenv`` and ``virtualenvwrapper``. If you have
both of these installed, a new project can be easily created like so:

.. code-block:: bash

    $ mkproject django-calaccess-downloads-website

That will jump into a new folder in your code directory, where you can fork our
code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website>`_. Don't know what that means? `Read this <https://guides.github.com/activities/forking/>`_.

Once you've created a fork, you should clone it to your computer.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-downloads-website.git .

Next, install the other Python libraries our code depends on, like the `Django web framework <https://www.djangoproject.com/>`_.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Configuring settings
--------------------

Many of the settings in this project can vary depending on where the code is being run. For instance, your local installation of the code will
likely connect to a different database than the public website.

To keep these different environments straight and avoid including sensitive passwords in public repositories we have developed
a system for storing many of the configuration options in a file named ``.env`` at the project's root.

The file is excluded from Git's version control system and needs to be created fresh each time the code is installed.

How .env works
~~~~~~~~~~~~~~

The ``.env`` file is expected to contain a separate section for each environment, using the structure favored by Python's `ConfigParser module <https://docs.python.org/2/library/configparser.html>`_. Here's a simple example:

.. code-block:: ini

    [DEV]
    database_name=calaccess
    mysecretpassword=password

    [PROD]
    database_name=calaccess
    mysecretpassword=hotpockets


By default, the source code will draw settings from a section name ``DEV``. To configure it to use a different set of variables
(like the``PROD`` section above), you must set the ``CALACCESS_WEBSITE_ENV`` environment variable.

.. code-block:: bash

    $ export CALACCESS_WEBSITE_ENV=PROD

If you are using virtualenv and virtualenvwrapper, you could add the above line of code to ``$VIRTUAL_ENV/bin/postactivate`` so that
whenever you start the project's virtual environment, the variable will be exported automatically.

.. note::

    You could also add the following line to your ``$VIRTUAL_ENV/bin/postdeactivate`` script to clear the variable
    whenever you deactivate the virtual environment:

    .. code-block:: bash

        $ unset CALACCESS_WEBSITE_ENV

---------------


Connecting to a local database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike a typical Django project, this application only supports the MySQL and
PostgreSQL database backends. This is because we enlist specialized tools to load
the immense amount of source data more quickly than Django typically allows.

If you choose MySQL
```````````````````

Create a new database named ``calaccess_website`` like this:

.. code-block:: bash

    mysqladmin -h localhost -u root -p create calaccess_website

If you choose PostgreSQL
````````````````````````

Create the database the PostgreSQL way.

.. code-block:: bash

    $ createdb calaccess_website -U postgres

---------------


Creating an archive on Amazon S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even a development project that will run only on your computer needs an account with Amazon Web Services to
store archived files in its S3 file service.

If you don't already have an AWS account, `make one now <https://aws.amazon.com/>`_ and `request <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html>`_ a
key pair that lets you access its services via Python.

Then create a new `S3 "bucket" <http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html>`_
to store files archived by this project.

---------------


Filling in .env for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The development environment can be created in the ``.env`` file by running a `Fabric <http://www.fabfile.org/>`_ task that will ask you to provide a value for all
of this project's settings.

.. code-block:: bash

    $ fab createconfig

You will prompted to provide the project's full list of settings, though some of them are only necessary when deploying the code
and site with Amazon Web Services.

======================= ======================= =================================================================================================
Setting                 Required in development Definition
======================= ======================= =================================================================================================
db_name                 Yes                     Name of your database.
db_user                 Yes                     Database user.
db_password             Yes                     Database password.
db_host                 Yes                     Database host location.
aws_access_key_id       Yes                     Shorter secret key for accessing Amazon Web Services.
aws_secret_access_key   Yes                     The longer secret key for accessing Amazon Web Services.
aws_region_name         Yes                     Amazon Web Services region where you resources are located.
s3_archived_data_bucket Yes                     Amazon S3 bucket where archived CAL-ACCESS data will be stored.
s3_baked_content_bucket No                      Amazon S3 bucket where the public-facing website will be stored.
key_name                No                      Name of the SSH ``.pem`` file associated with Amazon Web Services. Should be found in ``~/.ec2``.
ec2_host                No                      Public address of website's Amazon EC2 instance.
email_user              No                      Gmail account for sending error emails.
email_password          No                      Gmail password for sending error emails.
======================= ======================= =================================================================================================

If necessary, you can overwrite a specific setting or append a new one:

.. code-block:: bash

    $ fab setconfig:key=<new-variable-name>,value=<some-value>

You can also print your current app environment's configuration:

.. code-block:: bash

    $ fab printconfig

Or everything in the Fabric environment:

.. code-block:: bash

    $ fab printenv

---------------

Bootstrapping the project
-------------------------

Now that everything is configured, create the database tables.

.. code-block:: bash

    $ python manage.py migrate

Once everything is set up, the ``updatedownloadswebsite`` command will download the latest
bulk data release from `the Secretary of State's website <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ load it into your local database and archive the files on Amazon S3.

.. code-block:: bash

    $ python manage.py updatedownloadswebsite

.. warning::

    This will take a while. Go grab some coffee.

---------------

Exploring the site
------------------

Finally, start the development server and visit `localhost:8000/admin/ <http://localhost:8000/>`_ in your browser to inspect the site.

.. code-block:: bash

    $ python manage.py runserver

------------------

-----------------------------
Preparing a production server
-----------------------------

This section will walk you through deploy the :doc:`downloads website <apps/calaccess_downloads_site>` on
the Internet via Amazon Web Services. You will need to have completed the steps above.

Change your environment
-----------------------

As described above, the source code will draw settings from a section of the `.env` file named ``DEV``.

To switch to configuring your project for a production environment, you should set the ``CALACCESS_WEBSITE_ENV`` environment
variable to ``PROD``.

.. code-block:: bash

    $ export CALACCESS_WEBSITE_ENV=PROD

If you are using virtualenv and virtualenvwrapper, you could add the above line of code to ``$VIRTUAL_ENV/bin/postactivate`` so that
whenever you start the project's virtual environment, this variable will be exported automatically whenever you use ``workon`` to
begin work.

---------------

Creating an RDS database
------------------------

You will need to create a hosted database to store the data and keep tabs on the archive over time. Our recommended method
for doing this is using `Amazon's Relational Database Service <https://aws.amazon.com/rds/>`_.

You can spin up a PostgreSQL server there using our prepackaged Fabric commands. You're only required to provide a
name like ``download-website``:

.. code-block:: bash

    $ fab createrds:download-website

Then, wait several minutes while the server is provisioned.

By default, the new database server will have 100 GB of disk space allocated on a t2.large RDS `class instance <https://aws.amazon.com/rds/postgresql/details/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createrds:download-website,block_gb_size=80,instance_type=db.m4.large

The address for the RDS host will automatically be added to the configuration for your current environment, which is stored in ``.env``.
If you already had an RDS host set for your current env, its address will be overwritten.

---------------

Create an EC2 Instance
----------------------

Next you should create a new Ubuntu 14.04 server on `Amazon's Elastic Compute Cloud <https://aws.amazon.com/ec2/>`_ to host the Django project.

.. code-block:: bash

    $ fab createec2

By default, the server will have 100 GB of disk space allocated on a c3.large `class instance <https://aws.amazon.com/ec2/instance-types/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createec2:block_gb_size=80,instance_type=c3.xlarge

You can also override our default Amazon Machine Image (`AMI <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_):

.. code-block:: bash

    $ fab createec2:ami=<some-other-ami-id>

As with creating an RDS instance, the address for your new EC2 instance will automatically be added to the configuration for your current environment, which is stored in ``.env``. If you already had an EC2 host set, its address will be overwritten.

---------------

Filling in .env for the second time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you'll want to run our configuration command again, this time filling in the new details from your AWS account, database and server.
You may want to create a new set of S3 buckets separate from your development buckets.

.. code-block:: bash

    $ fab createconfig

Bootstrap the Django project
----------------------------

Finally, you're ready to bootstrap the Django project on the Ubuntu server.

.. code-block:: bash

    $ fab bootstrap

After connecting to your current EC2 instance, a framework called `Chef <https://www.chef.io/chef/>`_ and its dependencies, including Ruby,
will be installed on the server. Chef is used to configure the server and install the downloads website's code.

The ``bootstrap`` task also sets up a crontab job to execute run as command every six hours that will automate the collection, extraction and processing of the daily CAL-ACCESS database exports.

---------------

Wrapping up
-----------

And that's it! You know have a live CAL-ACCESS archive running in the cloud.

---------------
