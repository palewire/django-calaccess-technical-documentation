Deploying the website
=====================

This guide will walk you through executing the specific Fabric tasks necessary to deploy the `downloads website <apps/calaccess_downloads_site.html>`_. 

Before proceeding, be sure to `prepare your development environment <env-prep.html>`_.

--------------------------------------------


Create an RDS instance
----------------------

Unless you already have one up and running, you need to spin up a PostgreSQL server which will be the database backend for the website. You're required to provide an instance name, for example, ``download-website``:

.. code-block:: bash

    $ fab createrds:download-website

Then, wait several minutes while the server is provisioned.

By default, the new database server will have 100 GB of disk space allocated on a t2.large RDS `class instance <https://aws.amazon.com/rds/postgresql/details/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createrds:download-website,block_gb_size=80,instance_type=db.m4.large

The address for the RDS host will automatically be added to the configuration for your current environment, which is stored in ``.env``. If you already had an RDS host set for your current env, its address will be overwritten.

--------------------------------------------

Create an EC2 Instance
----------------------

Next, you need to spin up a new Ubuntu 14.04 server to host the Django project.

.. code-block:: bash

    $ fab createec2

By default, the server will have 100 GB of disk space allocated on a c3.large `class instance <https://aws.amazon.com/ec2/instance-types/>`_. If need be, you can override these settings:

.. code-block:: bash

    $ fab createec2:block_gb_size=80,instance_type=c3.xlarge

You can also override our default Amazon Machine Image (`AMI <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_):

.. code-block:: bash

    $ fab createec2:ami=<some-other-ami-id>

As with creating an RDS instance, the address for your new EC2 instance will automatically be added to the configuration for your current environment, which is stored in ``.env``. If you already had an EC2 host set, its address will be overwritten.

--------------------------------------------

Bootstrap the Django project
----------------------------

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

    $ fab rs


You can also connect directly to Ubuntu server via ssh:

.. code-block:: bash

    $ fab ssh


You might also check out the `complete list <fab-task-index.html>`_ of Fabric tasks available for performing various website admin duties. 
