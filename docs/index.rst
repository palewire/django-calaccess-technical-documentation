Django CAL-ACCESS Project
=========================

A collection of apps and resources developed and distributed to open up California's campaign finance and lobbyist disclosure data.

.. toctree::
   :hidden:
   :maxdepth: 1

   howtouseit
   apps
   calaccess
   faq
   howtocontribute

What is this?
-------------

This is the complete documentation for an open civic data project focused on making California state campaign finance and lobbyist disclosure data more easily available and usable.

The project includes a suite of apps, developed in Python's popular `Django <https://www.djangoproject.com/>`_ framework, that together form a pipeline to download, extract, load, clean, transform and republish data stored in the `CAL-ACCESS <http://cal-access.ss.ca.gov/>`_ system, which is maintained by the California Secretary of State.

This is an open-source, community-driven project. It's also an active work-in-progress.

Why?
----

Even among state govenment information systems, which are notoriously archaic and challenging to use, `CAL-ACCESS is the worst <http://www.sacbee.com/opinion/opn-columns-blogs/joyce-terhaar/article31239362.html>`_.

That's not just our opinion; it's the universal consensus of statehouse reporters, political scientists and public interest groups who've complained for years about the state government's slow, clunky and crash-prone system. Even the last two California Secretaries of State publicly acknowledged that their own system was past due for a modernization.

Still, a few journalists have wrestled with this behemoth in the past and reported incredible public interest stories:

* About Speaker John Pérez `doling out the choicest committee assignments <http://cironline.org/reports/california-speaker-gives-assemblys-juiciest-jobs-biggest-fundraisers-4501>`_ to the biggest campaign donors (from The Center for Investigative Reporting)
* About Gov. Jerry Brown's `switch from big money hater to big money taker <http://www.latimes.com/local/politics/la-me-pol-brown-money-20141031-story.html#page=1>`_ (from the Los Angeles Times)
* About political party committees `circumventing candidate contribution limits <http://www.sacbee.com/news/investigations/the-public-eye/article9471695.html>`_ (from the Sacramento Bee)

Yet each of these investigations required months of dedicated time by already overworked newsroom staff. That's because the nightly dumps of data published by the Secretary of State's office include over 36 million records spread out across 76 files, with cryptic column names and the occasional missing delimiter or escape character.

Like we said: The worst.

But why should every newsroom waste resources on this boring, time-consuming work? Why should each of us suffer the solitary pain of preparing these data for the creative, analytical work we would all rather be doing? Why have dozens of mediocre versions of scripts to extract, transform and load CAL-ACCESS data, when we could have one stable, user-friendly and open-source API?

Borrowing from Django's ethos or reusable, "pluggable" apps, we aim to make accessing CAL-ACCESS data as simple as installing our apps into your existing project. As a result, we expect to kickstart more, deeper investigations into the money behind California state and local politics.

Where to go next?
-----------------

* This `guide <howtouseit.html>`_ will walk you through the entire process of plugging CAL-ACCESS data into your existing Django project.

* For more advanced users interested in the entire feature set of each of apps in the pipeline, see `this section <apps.html>`_.

* Want to learn more about the data in CAL-ACCESS? Our `documentation <calaccess.html>`_ is the most complete and up-to-date you will find anywhere.

* Got a specific question? Check our `FAQs <faq.html>`_.

* Are you a civic data hacker with some free time on our hands? Learn `how to contribute <howtocontribute.html>`_ to this project!

Who is this?
------------

This project is authored and maintained by the California Civic Data Coalition, a team of journalists from the Los Angeles Times Data Desk, the Washington Post, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

In 2015 the coalition was named a winner of the Knight News Challenge and awarded $250,000 in philanthropic funding from the Knight Foundation, the Democracy Fund, the William and Flora Hewlett Foundation and the Rita Allen Foundation.

Read more about us at `californiacivicdata.org <http://www.californiacivicdata.org>`_. Find us on the #california-civic-data channel of the `News Nerdery Slack <http://newsnerdery.org/>`_.
