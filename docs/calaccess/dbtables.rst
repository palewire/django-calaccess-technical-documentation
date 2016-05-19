Database tables
===============

The 80 tab-delimited database exports published by California's Secretary of State and loaded by this Django application.

The categories for these tables are based on what's found in the `ReadMe <officialdocumentation.html#readme-zip>`_ file for the .ZIP database export file and the `mapping <officialdocumentation.html#mapcalformat2fields>`_ of .CAL format to database fields. However, in cases where this official documentation was incomplete or inconsistent, we've either listed the table under whichever category is most obviously relevant or listed it under "Other".

.. toctree::
   :maxdepth: 2

   dbtables/campaign_tables
   dbtables/lobbying_tables
   dbtables/common_tables
   dbtables/other_tables