Changelog
=========

1.6.0 (July 2017)
---------------------

* Deprecate ``--test, --use-test-data`` options from ``updatecalaccessrawdata`` command.
* Renamed custom Django project setting ``CALACCESS_DOWNLOAD_DIR`` to ``CALACCESS_DATA_DIR``.
* Removed ``CALACCESS_TEST_DOWNLOAD_DIR`` project setting.
* Extract and track any .TSV file regardless of location in download .ZIP directory tree.


1.5.2 (April 2017)
---------------------

* Fix duplicate updates. Only create a new ``RawDataVersion`` if:

  - ``Content-length`` from ``HEAD`` differs from ``expected_size`` on previous version, or,
  - ``Last-modified`` is at least five minutes more recent than ``release_datetime`` on previous version.


1.5.1 (April 2017)
---------------------

* Proceed with download of ZIP file as long as last-modified datetimes in ``HEAD`` and ``GET`` requests are within five minutes of each other.


1.5.0 (April 2017)
---------------------

* Django 1.11 compatibility.
* Fix check for existing clean zipped file when resuming.
* Fix message on response status code log.
* Skip dropping/re-adding of database table constraints and indexes when loading into MySQL (`transactional DDL statements <https://wiki.postgresql.org/wiki/Transactional_DDL_in_PostgreSQL:_A_Competitive_Analysis>`_ are not supported).


1.4.9 (March 2017)
---------------------

* Reset auto-increment fields after truncating database tables in postgres.
* Add prefixes on tracking model admins.
* When making requests to sos.ca.gov, log HTTP status code and reason and raise HTTP error if bad status.

1.4.8 (January 2017)
---------------------

* Upgrade to ``csvkit`` version 1.0.

1.4.7 (December 2016)
---------------------

* Fixed search field on admins for models with ``ForeignKey`` fields.

1.4.6 (November 2016)
---------------------

* Upgraded to latest version of django-postgres-copy
* Small improvements to CAL-ACCESS field documentation
* Small expansion of unittests
* Clean up of migrations

1.4.5 (September 2016)
----------------------

* Copyediting of CAL-ACCESS form documentation

1.4.2 (late-August 2016)
------------------------

* Docstring edits

1.4.1 (late-August 2016)
------------------------

* Increase max character length on ``ReceivedFilingsCd`` fields.
* Prevent unnecessary download of zip when resuming ``updatecalaccessrawdata``.
* Include release datetimes in log when ``downloadcalaccessrawdata`` and ``updatecalaccessrawdata`` versions are incompatible.

1.4.0 (mid-August 2016)
-----------------------

* Added zipping up and archiving of cleaned CSVs and error logs.

  * Added ``RawDataVersion.clean_zip_archive`` FileField.
  * Renamed ``RawDataVersion.zip_file_archive`` to ``RawDataVersion.download_zip_archive``.

* Smaller clean data files (removed unnecessary quote characters).
* Improvements to tracking models

  * Replaced ``RawDataCommand`` model with datetime fields and related properties

    * Added to ``RawDataVersion`` instances

      * ``.update_start_datetime`` and ``.update_finish_datetime`` to store version's most recent update start and finish datetimes.
      * ``.update_completed`` returns ``True`` if most recent update to version started and finished.
      * ``.update_stalled`` returns ``True`` if most recent update to version started but did not finish.
      * ``.download_start_datetime`` and ``.download_finish_datetime`` to store version's most recent download start and finish datetimes.
      * ``.download_completed`` returns ``True`` if most recent download of version started and finished.
      * ``.download_stalled`` returns ``True`` if most recent download version started but did not finish.
      * ``.completed()`` QuerySet method to ``RawDataVersion`` to get all versions where the update completed.

    * Added to ``RawDataFile`` instances

      * ``.clean_start_datetime`` and ``.clean_finish_datetime`` to store raw file's most recent clean start and finish datetimes.
      * ``.load_start_datetime`` and ``.load_finish_datetime`` to store raw file's most recent load start and finish datetimes.

  * Expanded file size tracking

    * Renamed ``.size`` to ``.expected_size`` on ``RawDataVersion`` instances.
    * Added ``.download_zip_size`` to ``RawDataVersion`` instances.
    * Added ``.clean_zip_size`` to ``RawDataVersion`` instances.
    * Added methods to get a pretty version (e.g., ``723M``) of each file size field

      * Added to ``RawDataVersion`` instances

        * ``.pretty_expected_size()``
        * ``.pretty_download_size()``
        * ``.pretty_clean_size()``

      * Added to ``RawDataFile`` instances

        * ``.pretty_download_file_size()``
        * ``.pretty_clean_file_size()``

    * Raise ``CommandError`` if completed download file size is not the same as expected size.

    * Added ``RawDataVersion`` properties to calculate file and record counts:

      * ``.download_file_count``
      * ``.download_record_count``
      * ``.clean_file_count``
      * ``.clean_record_count``
      * ``.error_file_count``
      * ``.error_count``

* Added ``extractcalaccessrawfiles`` management command for unzipping and extracting raw data files from downloaded CAL-ACCESS database export.

    * Start and finish times stored in ``.start_extract_datetime`` and ``.finish_extract_datetime`` on ``RawDataVersion`` instances.

* Bug fixes.

  * In``downloadcalaccessrawdata``, skip download if the size of the local zip file is equal to or bigger than the expected zip file size.
  * Because the server hosting the ZIP doesn’t always provide the most up-to-date resource (as we have `documented <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/1487>`_), a ``CommandError`` will be raised under any of the following conditions:

    * If ``downloadcalaccessrawdata`` is not called from the command-line (presumably, then, it was called by ``updatecalaccessrawdata``), and the ``RawDataVersion`` instance of the download command doesn't match the most recently started update.
    * If the ``ETag`` in the initial HEAD request made by ``downloadcalaccessrawdata`` does not match the ``ETag`` in the subsequent GET request.
    * If the actual size of the ZIP does not match the value of the ``Content-Length`` in the HEAD response.

  * If ``downloadcalaccessrawdata`` raises any of the above errors, ``updatecalaccessrawdata`` will wait five minutes and try again.
  * When archiving zips and files, open in binary (``'rb'``) mode.
  * In ``cleancalaccessrawfile``, fixed skipping of empty lines for Python 3.5.

* Support for Django 1.10.


1.3.0 (July 2016)
-----------------

* Now distributing on wheels.
* Added error_count to output ``reportcalaccessrawdata`` and excluded any unspecified fields.
* Added model property to RawDataFile that returns the CalAccess model object.

1.2.0 (July 2016)
-----------------

* Enhancements to tracking models

  * Zero pad datetime parts of archive dir (for better sorting)
  * Calculate and store load_columns_count and load_records_count in ``loadcalaccessrawfile``
  * Added error_count and error_log_archive fields to RawDataFile in order to track bad line parses during ``cleancalaccessrawfile``.
  * Added download_file_size and clean_file_size to RawDataFile.

* Enhancements to CalAccess models

  * Added inactive models group for CAL-ACCESS tables that are empty or apparently no longer in use.
  * Added a CalAccessMetaClass to automatically configure meta attributes common to all models.
  * Added a custom admin for every model.
  * Model verbose names are pre-fixed with model groups
  * Edits to model doc strings.

* Enhancements to management commands

  * Added standard logging.
  * Added a logger.info to the end of the ``updatecalaccessrawdata`` command to allow sending of emails when finished
  * Edits to command doc strings.

* More tests

  * Test to confirm that any field included in a model's ``UNIQUE_KEY`` attribute actually exists on the model.
  * Test to confirm that every model has a custom admin.

* Bug fixes

  * Fixed numbers in clean_records_count for RawDataFile.
  * Fixed line numbers logged in errors.csv files.
  * Write output of ``reportcalaccessrawdata`` to data directory instead of ``REPO_DIR``, which may not be in settings.

1.1.0 (late June 2016)
----------------------

* When `--noinput` is invoked for ``updatecalaccessrawdata``, exit if previously updated to the currently available version.
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
* Improved docs, admins and configuration for some campaign-finance models
* Numerous small bug fixes and documentation corrections


0.0.7 (August 2014)
-------------------

* Complete set of models that cover 100% of source CSV files
* Management commands that prep and load the data for MySQL backends
* Administration panels for previewing the data
