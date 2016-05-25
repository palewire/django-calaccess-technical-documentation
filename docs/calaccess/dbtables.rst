===============
Database tables
===============

This section outlines the record layouts of the tab-delimited text files
`released daily by California's Secretary of State <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_.
Each raw file is loaded by :doc:`/apps/calaccess_raw` into your local database
as a table with the same name.

.. toctree::
   :maxdepth: 2
   :glob:

   dbtables/*
   
.. warning::

    Most definitions in this section are drawn from the spotty and incomplete
    :doc:`state documentation </calaccess/officialdocumentation>`.
    We cannot vouch for its accuracy in all circumstances.

    To be absolutely certain about what each table and field contains, you should compare the electronic data to the underlying paper records published by the state.
