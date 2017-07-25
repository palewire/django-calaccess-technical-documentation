Contribute to our documentation
===============================

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
