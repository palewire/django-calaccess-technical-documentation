Deploying the website
=====================

This guide will walk you through the specific tasks, in order, necessary to deploy the `downloads website <apps/calaccess_downloads_site.html>`_.

--------------------------------------------

Step 1: Configure the environment
---------------------------------

First, you need to set a few configurations:

.. code-block:: bash

    $ fab createconfig

You will prompted to provide:

* An AWS Access Key ID and Secret Access Key (read more `here <https://aws.amazon.com/developers/access-keys/>`_).
* An AWS region (defaults to 'us-west-2').
* An SSH key-pair file name (defaults to 'my-key-pair'). This assumes you have a key pair stored in ``~/.ec2/my-key-pair.pem`` (if not, you should create one).
* The name of the S3 bucket where the data files will be archived (defaults to 'django-calaccess').
* The name of the PostgreSQL database that will serve as the backend for the download's website (defaults to 'calaccess_website').
* The name of the database user the django app will use to connect to the database (defaults to ccdc).
* The password for the database user.

You will also be prompted to provide addresses for an RDS and EC2 instance in case these servers are already up and running. Otherwise, press ENTER to skip for now.

These configurations will be stored locally in a ``.env`` file (ignored by git). When needed, these settings will be read into the environment in which Fabric or the Django project is running.

--------------------------------------------

Step 2: Create an RDS instance
------------------------------

Second (unless you already have one up and running), you need to spin up a PosgreSQL server which will be the database backend for the website. You're required to provide an instance name, ``download-website`` for example:

.. code-block:: bash

    $ fab createrds:download-website

Then wait several minutes while the server is provisioned.

By default, the new database server will have 100 GBs of disk space allocated on a t2.large RDS `class instance <https://aws.amazon.com/rds/postgresql/details/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createrds:download-website,block_gb_size=80,instance_type:db.m4.large

Note that the address for the RDS host will automatically be added to your configurations stored in ``.env``. If you already had an RDS host set, its address will be over-written.

--------------------------------------------

Step 3: Create and EC2 Instance
-------------------------------

Next, you need to spin up a new Ubuntu 14.04 server to host the Django project.

.. code-block:: bash

    $ fab createec2

By default, the server will have 100 GBs of disk space allocated on a c3.large `class instance <https://aws.amazon.com/ec2/instance-types/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createec2,block_gb_size=80,instance_type:c3.xlarge

You can also override our default `Amazon machine image (AMI) <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_:

.. code-block:: bash

    $ fab createec2,ami:<some-other-ami-id>

As with creating an RDS instance, the address for your new EC2 instance will automatically be added to your configurations stored in ``.env``. If you already had an EC2 host set, its address will be over-written.

--------------------------------------------

Step 4: Bootstrap the Django project
------------------------------------

Finally, you're ready to bootstrap the Django project on the Ubuntu server:

.. code-block:: bash

    $ fab bootstrap

After connecting to your current EC2 instance, a framework called `Chef <https://www.chef.io/chef/>`_ and its dependencies, including Ruby, will be installed on the server. Chef is used to configure the server and install the downloads website code.

The ``bootstrap`` task also sets up a crontab job to execute the raw-data app's ``updatecalaccessrawdata`` command every six hours, effectively automating the collection, extraction and processing of the daily CAL-ACCESS database exports.

--------------------------------------------

Wrapping up
-----------

And that's it! If you like, you can start the Django site server:

.. code-block:: bash

    $ fab runserver


You can also connect directly to Ubuntu server via ssh:

.. code-block:: bash

    $ fab ssh
