Contribute to django-calaccess-downloads-website
================================================

This walkthrough is for developers who want to contribute to :doc:`/apps/calaccess_downloads_site`, a open-source archive of
campaign-finance and lobbying-disclosure data from the California Secretary of State's :doc:`CAL-ACCESS </calaccess>` database.

It will show you how to install the source code of this application to fix bugs, develop new features and administer an archive.

---------------

-----------------------------------
Preparing a development environment
-----------------------------------

In order to contribute you first need to set up a local development environment, install the source code and configure a few settings.

While not required, we recommend that development be done within a contained virtual environment.

One way to accomplish that is with a two related Python packages: ``virtualenv`` and ``virtualenvwrapper``. If you have both of these installed, a new project can be easily set up by invoking:

.. code-block:: bash

    $ mkproject django-calaccess-downloads-website

That will jump into a new folder in your code directory, where you can clone our
code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website>`_
after you make a fork of your own. Don't know what that means? `Read this <https://guides.github.com/activities/forking/>`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-downloads-website.git .

Next, install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Configuring development settings
--------------------------------

Many of the settings in this project vary depending on the environment. For instance, your local installation of the code will
likely connect to a different database than live website.

To keep these different environments straight and avoid including sensitive passwords in our public repositories we have developed
a system for storing many of the configuration options in a ``.env`` at the project's root. The file is excluded from tracking by Git.

How .env works
~~~~~~~~~~~~~~

The ``.env`` is expected to contain a separate section for each environment, using the structure favored by Python's `ConfigParser module <https://docs.python.org/2/library/configparser.html>`_. Here's a simple example:

.. code-block:: ini

    [DEV]
    database_name=calaccess
    mysecretpassword=password

    [PROD]
    database_name=calaccess
    mysecretpassword=hotpockets


By default, the source code will draw settings from a section name ``DEV``.To configure it to use ``PROD`` or any other set of variables,
set the ``CALACCESS_WEBSITE_ENV`` environment variable.

.. code-block:: bash

    $ export CALACCESS_WEBSITE_ENV=PROD

If you are using virtualenv and virtualenvwrapper, you could add the above line of code to ``$VIRTUAL_ENV/bin/postactivate`` so that
whenever you start the project's virtual environment, this variable will be exported automatically whenever you use ``workon`` to
begin work.

You might also also add this line to your ``$VIRTUAL_ENV/bin/postdeactivate`` script in order to remove the variable
whenever you deactivate the virtual environment:

.. code-block:: bash

    $ unset CALACCESS_WEBSITE_ENV

Filling in .env for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current ``CALACCESS_WEBSITE_ENV`` can be configure in ``.env`` by running a `Fabric <http://www.fabfile.org/>`_ task that will ask you to provide a value for all
of this project's mandatory settings.

.. code-block:: bash

    $ fab createconfig

You will prompted to provide the project's full array of settings, though some of them are only necessary when deploying the code
and site with Amazon Web Services.

======================= ======================= =================================================================================================
Setting                 Required in development Definition
======================= ======================= =================================================================================================
db_name                 Yes                     Name of your database.
db_user                 Yes                     Database user.
db_password             Yes                     Database password.
rds_host                Yes                     Database host location.
aws_access_key_id       No                      Shorter secret key for accessing Amazon Web Services.
aws_secret_access_key   No                      The longer secret key for accessing Amazon Web Services.
aws_region_name         No                      Amazon Web Services region where you resources are located.
s3_archived_data_bucket No                      Amazon S3 bucket where archived CAL-ACCESS data will be stored.
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
