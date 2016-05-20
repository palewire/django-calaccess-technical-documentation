Django CAL-ACCESS documentation
===============================

.. include:: ../README.rst
   :start-line: 2
   :end-line: 9


Table of contents
-----------------

.. toctree::
   :maxdepth: 2

   howtouseit
   apps
   calaccess
   faq
   howtocontribute

----------------------


Why is all this necessary?
--------------------------

Journalists have reported important stories out of data found in CAL-ACCESS:

* About Speaker John Pérez `doling out the choicest committee assignments <http://cironline.org/reports/california-speaker-gives-assemblys-juiciest-jobs-biggest-fundraisers-4501>`_ to the biggest campaign donors (from The Center for Investigative Reporting)
* About Gov. Jerry Brown's `switch from big money hater to big money taker <http://www.latimes.com/local/politics/la-me-pol-brown-money-20141031-story.html#page=1>`_ (from the Los Angeles Times)
* About political party committees `circumventing candidate contribution limits <http://www.sacbee.com/news/investigations/the-public-eye/article9471695.html>`_ (from the Sacramento Bee)

Yet each of these investigations required months of dedicated time by already overworked newsroom staff.
That's because, even among state govenment information systems which are notoriously archaic and challenging to use,
CAL-ACCESS is `widely-considered <http://www.sacbee.com/opinion/opn-columns-blogs/joyce-terhaar/article31239362.html>`_ to be among the worst.

The nightly dumps of data `published <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ by
the Secretary of State's office include over 36 million records spread out across 76 files, with cryptic column names and
the occasional missing delimiter or escape character.

But why should every newsroom waste resources on this boring, time-consuming work? Why should each of us suffer the solitary pain of preparing these data for the creative, analytical work we would all rather be doing? Why have dozens of mediocre versions of scripts to extract, transform and load CAL-ACCESS data, when we could have one stable, user-friendly and open-source API?

Borrowing from Django's ethos or reusable, "pluggable" apps, we aim to make accessing CAL-ACCESS data as simple as installing our apps into your existing project. As a result, we expect to kickstart more, deeper investigations into the money behind California state and local politics.
