Fab tasks index
===============

Below is the complete list of Fabric tasks available for administering the `downloads website <apps/calaccess_downloads_site.html>`_.

.. Note::
    
    Fabric allows you to run one task after the other in a single fab command-line call like so:

    .. code-block:: bash

        $ fab task1:pos_arg1 task2:opt_arg=some_value

    Which can be useful for chaining tasks together for ad-hoc administrative processes. Read more `here <http://docs.fabfile.org/en/1.11/usage/fab.html>`_.

--------------------------------------------

Amazon
------

Tasks for managing Amazon Web Service (AWS) resources.

``createec2``
~~~~~~~~~~~~~

Spin up a new Ubuntu 14.04 server on Amazon EC2. Returns the id and public address.

.. code-block:: bash

    $ fab createrds

The address for your new EC2 instance will also be added to your current environment's configurations (stored in ``.env``). If you already have EC2 host set in your current env, its address will be replaced.

Optional arguments:

* ``instance_name`` (default is ``calaccess_website``)
* ``block_gb_size`` (default is ``100``)
* ``instance_type`` (default is ``c3.large``)
* ``ami`` (default is ``ami-978dd9a7``)

``createkey``
~~~~~~~~~~~~~

Creates an EC2 key pair and saves it to a .pem file.

The ``name`` for the key is the only positional argument:

.. code-block:: bash

    $ fab createkey:ccdc-key

You'll be stopped if you try to re-use an existing key pair name.

A new key pair will then be stored in ``~/.ec2/<your-key-name>.pem``, and the key pair name will be added to your current environment's configurations (stored in ``.env``). If you already have a key name set in your current env, it will be replaced.

``createrds``
~~~~~~~~~~~~~

Spin up a new database backend with Amazon RDS.

The ``instance_name`` is the only positional argument:

.. code-block:: bash

    $ fab createrds:downloads-website

This may take several minutes.

The address for your new RDS instance will be added to your current environment's configurations (stored in ``.env``). If you already have RDS host set in your current env, its address will be replaced.

Optional arguments:

* ``database_port`` (default is ``5432``)
* ``block_gb_size`` (default is ``100``)
* ``instance_type`` (default is ``db.t2.large``)

``copydb``
~~~~~~~~~~

Copy the most recent snapshot on the source AWS RDS instance to the destination RDS instance.

The positional arguments are:
* ``src_db_instance_id``, which identifies the source from which to create a copy
* ``dest_db_instance_id``, which identifies the destination of the copy.

This action will delete the current database on the destination instance.

This task can be useful, for example, if you want to replicate the production database to a dev instance.

.. code-block:: bash

    $ fab copyrds:prod-db,dev-db

The process may take several minutes to complete.

If you would like to create a new snapshot of the source db instance before making a copy, you can pass in `` make_snapshot=True``.


--------------------------------------------

App
---

Tasks for deploying and managing the Django app.

``collectstatic``
~~~~~~~~~~~~~~~~~

Roll out the Django app's latest static files.

.. code-block:: bash

    $ fab collectstatic


``deploy``
~~~~~~~~~~

Run a full deployment of code to the remote server.

.. code-block:: bash

    $ fab deploy

More specifically, this task executes the following sub-tasks in order:

1. ``pull``
2. ``rmpyc``
3. ``pipinstall``
4. ``migrate``
5. ``collectstatic``

``manage``
~~~~~~~~~~

Run a manage.py command inside the Django virtualenv.

The only positional argument is ``cmd``. For example, if you wanted to kickstart the CAL-ACCESS raw data `update <apps/managementcommands.html#updatecalaccessrawdata>`_ process:

.. code-block:: bash

    $ fab manage:updatecalaccessrawdata

``migrate``
~~~~~~~~~~

Migrate the database:

.. code-block:: bash

    $ fab migrate


``pipinstall``
~~~~~~~~~~~~~~

Install the Python requirements inside the virtualenv:

.. code-block:: bash

    $ fab pipinstall


``pull``
~~~~~~~~

Pull the lastest changes from the GitHub repo:

.. code-block:: bash

    $ fab pull


``rmpyc``
~~~~~~~~

Erases pyc files from the app's code directory.

.. code-block:: bash

    $ fab rmpyc


--------------------------------------------

Chef
----

Tasks relate to installing and executing `Chef <https://www.chef.io/chef/>`_, the Ruby framework we use to set up the Ubuntu server that hosts the Django project.

``bootstrap``
~~~~~~~~~~~~~

Install Chef and use it to install the app on an EC2 instance.

.. code-block:: bash

    $ fab bootstrap

More specifically, this task executes the following sub-tasks in order:

1. ``rendernodejson``
2. ``installchef``
3. ``cook``
4. ``copyconfig``
5. ``migrate``
6. ``collectstatic``

This task also sets the environment in which the website will run on the server based on your current local ``CALACCESS_WEBSITE_ENV`` environment variable (defaults to ``DEV`` if this env var is not set).

``cook``
~~~~~~~~

In order to do its thing, Chef requires a `cookbook <https://docs.chef.io/cookbooks.html>`_ that contains `recipes <https://docs.chef.io/recipes.html>`_ (basically, short Ruby scripts) that outline the configuration scenario on the remote server. You can see our cookbook for this project `here <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website/tree/master/chef/cookbooks/ccdc>`_.

This task updates the Chef cookbook on the server and executes it.

.. code-block:: bash

    $ fab cook

``installchef``
~~~~~~~~~~~~~~~

Install all the dependencies to run a Chef cookbook. 

.. code-block:: bash

    $ fab installchef

More specifically, this task:

* Updates apt-get
* Installs git
* Installs Ruby (the language in which Chef is written)
* Installs Chef

``rendernodejson``
~~~~~~~~~~~~~~~~~~

Render chef's node.json file from a template.

.. code-block:: bash

    $ fab rendernodejson

In addition to the cookbook, some of the settings Chef requires are stored in a local ``node.json`` file, which is rendered from a `template <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website/blob/master/chef/node.json.template>`_.

This template file is where you can, for example, change the run times for the crontab job that updates the download website with the latest CAL-ACCESS data export. 

In order for any changes you make to node.json.template to take effect on the server, you need to execute both the ``rendernodejson`` and ``cook`` tasks.

--------------------------------------------

Configure
---------

Tasks for configuring the downloads website Django environment.

``createconfig``
~~~~~~~~~~~~~~~~

Prompt users for settings to be stored in the config_file.

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


``copyconfig``
~~~~~~~~~~~~~~

Copy current configurations in local .env file to the ec2 instance.

.. code-block:: bash

    $ fab copyconfig


``printconfig``
~~~~~~~~~~~~~~~

Print out the configuration settings for the local environment.

.. code-block:: bash

    $ fab printconfig


``printenv``
~~~~~~~~~~~~

Print out the Fabric env settings.

.. code-block:: bash

    $ fab printenv


``setconfig``
~~~~~~~~~~~~~

Add or edit a key-value pair in the .env configuration file.

.. code-block:: bash

    $ fab setconfig:key=<new-variable-name>,value=<some-value>

Note that these changes will only take affect locally. In order to copy your new configurations to the EC2 instance, execute the ``copyconfig`` task.


--------------------------------------------

Dev
---

Tasks for connecting to and running the server.

``rs``
~~~~~~

Start up the Django runserver.

.. code-block:: bash

    $ fab rs


``ssh``
~~~~~~~

Log into the EC2 instance using SSH.

.. code-block:: bash

    $ fab ssh

