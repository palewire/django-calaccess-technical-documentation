Getting started
===============

In order to contribute to `django-calaccess-raw-data <apps/calaccess_downloads_site.html>`_, you first need to set up your development environment, install the source code and configure a few inital settings.

---------------


Preparing a development environment
-----------------------------------

It is not required, but it is recommended that development of the library be
done from within a contained virtual environment.

One way to accomplish that is with a two related Python packages: ``virtualenv`` and ``virtualenvwrapper``. If you have both of these installed, a new project can be started with the following:

.. code-block:: bash

    $ mkproject django-calaccess-downloads-website

That will jump into a new folder in your code directory, where you can clone our
code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-raw-data>`_
after you make a fork of your own. Don't know what that means? `Read this <https://guides.github.com/activities/forking/>`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-downloads-website.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Switching website env modes
---------------------------

By default, the downloads website will be configured in ``DEV`` mode. If you need to configure it in ``PROD`` or any other mode, you can set this via the ``CALACCESS_WEBSITE_ENV`` environment variable:

.. code-block:: bash

    $ export CALACCESS_WEBSITE_ENV=PROD

If you are using virtualenv and virtualenvwrapper (as we recommend), you might add the above line of code to your ``$VIRTUAL_ENV/bin/postactivate`` script so that whenever you start the project's virtual environment (like so):

.. code-block:: bash

    $ workon django-calaccess-downloads-website

This variable will be set automatically. You might also also add this line:

.. code-block:: bash

    $ unset CALACCESS_WEBSITE_ENV

To your ``$VIRTUAL_ENV/bin/postdeactivate`` script in order to remove it whenever you deactivate the virtual environment (from the command line, simply type ``deactivate``).

---------------


Configuring the app environment
-------------------------------

Next, you need to set a few configurations necessary for running and deploying the app. There's a Fabric task for that:

.. code-block:: bash

    $ fab createconfig

You will prompted to provide:

* An AWS Access Key ID and Secret Access Key (read more `here <https://aws.amazon.com/developers/access-keys/>`_).
* An AWS region (defaults to 'us-west-2').
* An SSH key-pair file name (defaults to 'my-key-pair'). This assumes you have a key pair stored in ``~/.ec2/my-key-pair.pem`` (if not, you should create one).
* The name of the PostgreSQL database that will serve as the backend for the downloads website (defaults to 'calaccess_website').
* The name of the database user the django app will use to connect to the database (defaults to ccdc).
* The password for the database user.
* The name of the S3 bucket where the data files will be archived (defaults to 'django-calaccess-dev-data-archive').
* The name of the S3 bucket where the "baked" content files will stored (defaults to 'django-calaccess-dev-baked-content')
* The host email address and password (press ENTER to skip, if not desired).
* Addresses for the RDS and EC2 instances, in case these servers are already up and running. If now, press ENTER to skip for now, and spin them up later.

These configurations will be stored in a ``.env`` file (ignored by git) along with settings for other envs you have configured, each denoted by a section header such as ``[DEV]`` and ``[PROD]``.

If necessary, you can overwrite a specific configuration or append a new one:

.. code-block:: bash

    $ fab setconfig:key=<new-variable-name>,value=<some-value>

You can also print out all your current app environment's configurations:

.. code-block:: bash

    $ fab printconfig

Or everything in the Fabric environment:

.. code-block:: bash

    $ fab printenv

---------------


Now what?
---------

Now you are ready to `deploy the website <deployment-walkthru.html>`_ and juggle other `administrative tasks <fab-task-index>`_.
