Testing
=======

Our code is tested using `Django's built-in unittesting`_ system via the TravisCI_
continuous integration service.

In addition, prior to the Django unittests, code is evaluated using Python's pep8_ and pyflakes_ style-guide enforcement tools.

When a commit or pull request is made with our repository, those tests are
rerun with the latest code. We try not to be too uptight, but we generally
expect the tests to be pass before we will merge a request.

You can also run these tests locally. Change your directory into your local copy of any of our repos, and then:

.. code-block:: sh

    $ make test


.. _Django's built-in unittesting: https://docs.djangoproject.com/en/1.11/topics/testing/
.. _TravisCI: https://travis-ci.org/california-civic-data-coalition
.. _pep8: https://pypi.python.org/pypi/pep8
.. _pyflakes: https://pypi.python.org/pypi/pyflakes