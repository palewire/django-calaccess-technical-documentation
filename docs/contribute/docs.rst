For documentation writers
=========================

We're maintaining a single `repository <https://github.com/california-civic-data-coalition/django-calaccess-technical-documentation>`_
for all documents related to the Django CAL-ACCESS project. This section is for
anyone who wants to contribute to these documents.

---------------


Do I need to know Python (or Django)?
-------------------------------------

No. But you should be familiar with the syntax of `reStructuredText <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_, since that's the format in which these documents are written.

---------------


Which files should I edit?
--------------------------

Generally, you should be editing the ``.rst`` files in ``docs/`` directory, rather than any of the ``.html`` files in the ``_build/`` directory. The ``.html`` files are compiled using Python's `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ documentation framework (for more on this, see `Viewing Local Changes <#viewing-local-changes>`_).

---------------


Editing Database Tables or Filing Forms Docs
--------------------------------------------

The docs inside the `Database tables <calaccess/dbtables.html>`_ and `Filing forms <filingforms.html>`_ sections are generated programmatically, rather than being typed out. So, for instance, if you make a change to ``./docs/calaccess/db_tablescampaign_tables.rst``, that change will likely be over-written. 

Probably your edit will require a change somewhere in the `raw-data <https://github.com/california-civic-data-coalition/django-calaccess-raw-data>`_ app. If you can't figure it out on your own, feel free to `file an issue <https://github.com/california-civic-data-coalition/django-calaccess-technical-documentation/issues>`_ with us, and we'll get on it.

(If you interested in how this works, check out the management commands in ``src/toolbox`` inside the `technical documentation <https://github.com/california-civic-data-coalition/django-calaccess-technical-documentation>`_ repo).

---------------


Preparing a local environment
-----------------------------

If you want to work on changes to the documentation on your own machine (as opposed to making edits via GitHub's interface), this guide will walk you through the setup process.

Much like `contributors to our apps <app_devs.html>`_, we recommend you work on these docs in a virtual environment.

One way to accomplish is with Python's ``virtualenv`` tool and its helpful companion ``virtualenvwrapper``. If you have that installed a new project can be started with the following:

.. code-block:: bash

    $ mkproject django-calaccess-technical-documentation

That will jump into a new folder in your code directory, where you can clone our code repository from `GitHub <https://github.com/california-civic-data-coalition/django-calaccess-technical-documentation>`_ after you make a fork of your own. Don't know what that means? `Read this <https://guides.github.com/activities/forking/>`_.

.. code-block:: bash

    $ git clone https://github.com/<YOUR-USERNAME>/django-calaccess-technical-documentation.git .

Next install the other Python libraries our code depends on.

.. code-block:: bash

    $ pip install -r requirements.txt

---------------


Viewing changes locally
-----------------------

After you make changes to your local versions of the ``.rst`` files in the ``docs/`` directory, you can view your edits as they will appear on ReadTheDocs:

.. code-block:: bash

    $ make html

This will invoke the sphinx command to compile the ``.html`` and ``.doctree`` files as they will be when deployed to ReadTheDocs. These files are then saved in ``docs/_build/html``, where you can open them with your favorite web browser and see how they look.

However, you might instead prefer to see your edits as you're making them:

.. code-block:: bash

    $ make livehtml

This will start serving the docs on http://127.0.0.1:8000, where you can point your favorite web browser. While the server is running, Sphinx will also detect any change you make to the ``.rst`` files and, on save, automatically re-build the ``.html`` files.

