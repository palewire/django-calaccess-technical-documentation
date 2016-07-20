For website admins
==================

The infrastructure for our `downloads website <apps/calaccess_downloads_site.html>`_ is hosted on Amazon Web Services. More specifically:

* The raw data files exported daily from CAL-ACCESS are uploaded to a `Simple Storage Service <https://aws.amazon.com/s3/>`_ (S3) bucket.
* The website's PostgreSQL backend is hosted on a `Relational Database Service <https://aws.amazon.com/rds/>`_ (RDS) instance.
* The application code that downloads, processes and archives the daily CAL-ACCESS exports runs on an `Elastic Compute Cloud <https://aws.amazon.com/ec2/>`_ (EC2) instance.

We deploy and manage this infrastructure via tasks defined using `Fabric <http://www.fabfile.org/>`_. This makes processes like deploying the entire downloads website as simple as invoking a few commands from the command-line.

.. toctree::
   :maxdepth: 2

   calaccess_website/env-prep
   calaccess_website/deployment-walkthru
   calaccess_website/fab-task-index
