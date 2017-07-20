Models for tracking updates
===========================

The processed-data app also keeps track of each snapshot of CAL-ACCESS database it processes. This tracking information is stored in the data tables outlined below.

.. note::

    By default, the processed-data app does *not* archive previous versions of the CAL-ACCESS database. Rather, with each call to the management commands, the data files they process are overwritten.

    You can configure the raw-data app to keep each copy of the zip file downloaded from the California Secretary of State as well as the indivdual raw .csv files and cleaned .tsv files by flipping the ``CALACCESS_STORE_ARCHIVE`` to ``True`` in ``settings.py``:

    .. code-block:: python

        # in settings.py
        CALACCESS_STORE_ARCHIVE = True

    By default, the older copies of these files will be saved to the path specified by your Django project's ``MEDIA_ROOT`` setting (more on that `here <https://docs.djangoproject.com/en/1.11/ref/settings/#media-root>`_). However, if you've implemented a `custom storage system <https://docs.djangoproject.com/en/1.10/howto/custom-file-storage/>`_ or installed a third-party app (such as `django-storages <https://django-storages.readthedocs.io/en/latest/>`_), that should work too.

----------------------

ProcessDataVersion
~~~~~~~~~~~~~~~~~~

Versions of CAL-ACCESS raw source data, typically released every day.

Fields
******

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">


        <tr>
            <td>id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Auto-incrementing unique identifer of versions</td>
        </tr>


        <tr>
            <td>raw_version_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Foreign key referencing the raw data version processed</td>
        </tr>


        <tr>
            <td>process_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the processing of the CAL-ACCESS version started</td>
        </tr>


        <tr>
            <td>process_finish_datetime</td>
            <td>Integer</td>
            <td>No</td>
            <td>Date and time when the processing of the CAL-ACCESS version finished</td>
        </tr>

        <tr>
            <td>zip_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive zip of processed files</td>
        </tr>

        <tr>
            <td>zip_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>The expected size (in bytes) of the zip of processed files</td>
        </tr>


    </tbody>
    </table>
    </div>


Instance methods and properties
*******************************

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">


        <tr>
            <td><code>.update_completed</code></td>
            <td>Check if the database update to the version completed. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>.update_stalled</code></td>
            <td>Check if the database update to the version started but did not complete. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>.pretty_expected_size()</code></td>
            <td>Returns a prettified version (e.g., "725M") of the expected size of the downloaded zip.</td>
        </tr>


    </tbody>
    </table>
    </div>


ProcessedDataFile
~~~~~~~~~~~

A data file included in a processed version of CAL-ACCESS.

Fields
******

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">


        <tr>
            <td>id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Auto-incrementing unique identifer of the file</td>
        </tr>


        <tr>
            <td>version_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Foreign key referencing the processed version of CAL-ACCESS</td>
        </tr>


        <tr>
            <td>file_name</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Name of the processed data file without extension</td>
        </tr>


        <tr>
            <td>process_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the processing of the file started</td>
        </tr>


        <tr>
            <td>process_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the processing of the file finished</td>
        </tr>


        <tr>
            <td>records_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of records in the processed file</td>
        </tr>


        <tr>
            <td>file_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive of the processed file</td>
        </tr>

        <tr>
            <td>file_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>Size of the processed file (in bytes)</td>
        </tr>
       
   	</tbody>
    </table>
    </div>


Instance methods and properties
*******************************

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">

        <tr>
            <td><code>.pretty_file_size()</code></td>
            <td>Returns a prettified version (e.g., "725M") of the downloaded file's size.</td>
        </tr>


    </tbody>
    </table>
    </div>
