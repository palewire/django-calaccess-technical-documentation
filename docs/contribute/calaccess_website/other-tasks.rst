Other admin tasks
=================

In addition to `deploying the website <deployment-walkthru.html>`_, we've developed the Fabric tasks described below for handling other admin duties.

Key Pair
--------

If need be, you can generate a new `key pair <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html?icmpid=docs_ec2_console>`_ for connecting to your EC2 instance. You'll need to provide key name, for example ``ccdc-key``:

.. code-block:: bash

    $ fab createkey:ccdc-key


You'll be preventing from re-using a name of an existing key pair.

A new key pair will then be stored in ``~/.ec2/<your-key-name>.pem``, and the key pair name will be added to your current configurations (stored in ``.env``). The key pair name set here will be added to any new EC2 instances you create and will be used when connecting to those servers via SSH.


Config
------

You can also overwrite a specific configuration or append a new one not specified when executing ``fab createconfig``:

.. code-block:: bash

    $ fab setconfig:key=<new-variable-name>,value=<some-value>


Of course, these changes will only take affect locally. In order to copy your new configurations to the EC2 instance:

.. code-block:: bash

    $ fab copyconfig


You can also print out all your current configurations:

.. code-block:: bash

    $ fab copyconfig


Or everything in the Fabric environment:

.. code-block:: bash

    $ fab printenv


Chef
----

`Chef <https://www.chef.io/chef/>`_ is the Ruby framework we use to set up Ubuntu server that hosts the Django project, as explained in the `bootstrap step <deployment-walkthru.html#step-4-bootstrap-the-django-project>`_ of the website deployment walk-through.

If you need to install Chef and its dependencies separate from the entire ``bootstrap`` task, you can:

.. code-block:: bash

    $ fab installchef


In order to do its thing, Chef requires a `cookbook <https://docs.chef.io/cookbooks.html>`_ that contains `recipes <https://docs.chef.io/recipes.html>`_ (basically, short Ruby scripts) that outline the configuration scenario on the remote server. You can see our cookbook for this project `here <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website/tree/master/chef/cookbooks/ccdc>`_.

In addition to the cookbook, some of the settings Chef requires are stored in a local ``node.json`` file, which is rendered from a `template <https://github.com/california-civic-data-coalition/django-calaccess-downloads-website/blob/master/chef/node.json.template>`_: 

.. code-block:: bash

    $ fab rendernodejson


This template file is where you can, for example, change the run times for the cron job that updates the download website's with the latest CAL-ACCESS data export. In order for this sort of change to take effect on the server, you need actually put the Chef recipes to use:

.. code-block:: bash

    $ fab cook


App
---

Run a full deployment of code to the remote server

.. code-block:: bash

    $ fab deploy

Sub-tasks
~~~~~~~~~

Pull the lastest changes from the GitHub repo:

.. code-block:: bash

    $ fab pull


Migrate the database:

.. code-block:: bash

    $ fab migrate


Install the Python requirements inside the virtualenv:

.. code-block:: bash

    $ fab pipinstall


Roll out the Django app's latest static files

.. code-block:: bash

    $ fab collectstatic

