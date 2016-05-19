Database tables
===============

This section outlines the record layouts of the tab-delimited text files published by California's Secretary of State. Each raw file is loaed by django-calaccess-raw-data into your local database as a table with the same name.

The categories for these tables are based on what's found in the `ReadMe <officialdocumentation.html#readme-zip>`_ file for the .ZIP database export file and the `mapping <officialdocumentation.html#mapcalformat2fields>`_ of .CAL format to database fields. However, in cases where this official documentation was incomplete or inconsistent, we've either listed the table under whichever category is most obviously relevant or listed it under "Other".

.. toctree::
   :maxdepth: 2
   :glob:

   dbtables/*