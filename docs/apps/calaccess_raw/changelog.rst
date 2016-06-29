Changelog
=========

1.1.0 (late June 2016)
----------------------

* When `--noinput` is invoked for `updatecalaccessrawdata`, exit if previously updated to the currently available version.
* Enforce lowercase UNIQUE_KEY settings on models.
* Removed unnecessary pretty amount model methods as part of driving common.py models file test coverage up to 100%.

1.0.2 (early June 2016)
-----------------------

* Include migrations in official package.
* Fix ``verbose_name`` for ``RawDataFile.clean_file_archive``.

1.0.0 (May 2016)
----------------

* Enhanced resume behavior
  
  * Allow previously interrupted updates to resume at any stage of the process: downloading, cleaning or loading.
  * Users will be prompted to resume (if possible). User may decline and re-start the entire update.
  * Removed ``--resume-download`` option from ``updatecalaccessrawdata`` and ``downloadcalaccessrawdata`` in favor of prompting the user to resume.
  * Removed ``--database`` option from all commands. Multi-database users are encouraged to use Django's `database routers <https://docs.djangoproject.com/en/1.9/topics/db/multi-db/#using-routers>`_.

* Raw data file archiving

  * Added ``CALACCESS_STORE_ARCHIVE`` setting. When enabled, management commands will save each version of the downloaded .zip file, the extracted .tsv files and cleaned .csv files to the Django project's ``MEDIA_ROOT``.
  * Added FileFields to RawDataVersion and RawDataFile in order to link the database records with the archived files they reference.

* Completed documentation of all 80 raw data models and 1,467 fields

  * Defined hundreds of choices for 182 look-up fields.
  * Published expanded Django project documentation. Added re-directs from old app-specific documentation.
  * Integrated references to official documents and filing forms into data models. PDFs on DocumentCloud.

* Expanded unit testing of data model documentation

  * Wider scope of choice field testing.
  * Verify that each model has a ``UNIQUE_KEY`` attribute set.
  * Verify that each model has a document reference.
  * Verify that each choice field has a document reference.
  * Verify that each model with a form_type or form_id field (with a few exceptions) is linked to filing forms.
  * Introduced ``reportcalaccessrawdata`` command, which generates a report outlining the number / proportion of files / records cleaned and loaded.

* Model Re-modeling:

  * Moved ``BallotMeasuresCd`` from ``other.py`` to ``campaign.py``. Same with admin.
  * Moved remaining models in ``other.py`` to ``common.py``. Removed ``other.py``. Same with admins.
  * Re-ordered models into related groups.

* Bug fixes

  * Truncate time portions of raw datetime values (see `#1457 <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/1457>`_).
  * Strip newlines when loading into MySQL.

0.2.0 (January 2016)
---------------------

* Support for Python 3.5
* Support for Django 1.9
* Simplified downloadcalaccessrawdata. Now only downloads, unzips and preps
* Introduced updatecalaccessrawdata, which downloads, cleans and loads data
* Added --resume-download option in case download is interrupted
* Added --csv option to loadcalaccessrawfile so that users can load from a file other than the one specified for the given calaccess_raw model
* Added --keep-files option. Unless the option is invoked downloadcalaccessrawdata, cleancalaccessrawfile, loadcalaccessrawfile and updatecalaccessrawdata now clear out original and intermediate files  
* Support for multiple databases configured in Django DATABASE settings. Users can now load into a specified database using --database option
* Fixed verifycalaccessrawfile
* Updated management command options to most recent Django style, using argparse instead of optparse
* Hundreds of unique keys, field defs and choices patched by Code Rushers
* Automatically generated table documentation page
* Expanded documentation

0.1.2 (February 2015)
---------------------

* Substituted clint for progressbar
* Improved choices for form type fields

0.1.1 (January 2015)
--------------------

* Datetime support for MySQL fields
* Fixed bug that didn't allow null values in PostgreSQL datetime fields


0.1.0 (November 2014)
---------------------

* Support for PostgreSQL database backends
* Upgraded to Django 1.7
* Prettified management command output and logging
* Improved docs, admins and configuration for some campaign finance models
* Numerous small bug fixes and documentation corrections


0.0.7 (August 2014)
-------------------

* Complete set of models that cover 100% of source CSV files
* Management commands that prep and load the data for MySQL backends
* Administration panels for previewing the data
