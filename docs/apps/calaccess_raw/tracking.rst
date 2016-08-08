Models for tracking updates
===========================

The raw-data app also keeps track of each snapshot of the CAL-ACCESS database released by the California Secretary of State, including its release date and byte size, as well as the activity of the `management commands <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/managementcommands.html>`_ that process this data.

This tracking information is stored in the data tables outlined below.

.. note::

    By default, the raw-data app does *not* archive previous versions of the CAL-ACCESS database. Rather, with each call to the management commands, the data files they process are overwritten.

    You can configure the raw-data app to keep each copy of the zip file downloaded from the California Secretary of State as well as the indivdual raw .csv files and cleaned .tsv files by flipping the ``CALACCESS_STORE_ARCHIVE`` to ``True`` in ``settings.py``:

    .. code-block:: python

        # in settings.py
        CALACCESS_STORE_ARCHIVE = True

    By default, the older copies of these files will be saved to the path specified by your Django project's ``MEDIA_ROOT`` setting (more on that `here <https://docs.djangoproject.com/en/1.10/ref/settings/#media-root>`_). However, if you've implemented a `custom storage system <https://docs.djangoproject.com/en/1.10/howto/custom-file-storage/>`_ or installed a third-party app (such as `django-storages <https://django-storages.readthedocs.io/en/latest/>`_), that should work too.

----------------------

RawDataVersion
~~~~~~~~~~~~~~

Versions of CAL-ACCESS raw source data, typically released every day.

**Fields:**

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
            <td>release_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>(Unique) date and time the version of the CAL-ACCESS database was released (value of Last-Modified field in HTTP response header)</td>
        </tr>



        <tr>
            <td>expected_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>The expected size of the downloaded CAL-ACCESS zip, as specified in the content-length field in HTTP response header
        </tr>


        <tr>
            <td>update_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the update to the CAL-ACCESS version started</td>
        </tr>
        <tr>
            <td>update_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the update to the CAL-ACCESS version finished</td>
        </tr>
        <tr>
            <td>download_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the download of the CAL-ACCESS database export started</td>
        </tr>
        <tr>
            <td>download_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the download of the CAL-ACCESS database export finished</td>
        </tr>
        <tr>
            <td>extract_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when extraction of the CAL-ACCESS data files started</td>
        </tr>
        <tr>
            <td>extract_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when extraction of the CAL-ACCESS data files finished</td>
        </tr>
        <tr>
            <td>download_zip_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive of the original zipped file downloaded from CAL-ACCESS</td>
        </tr>
        <tr>
            <td>clean_zip_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive zip of cleaned (and error log) files</td>
        </tr>
        <tr>
            <td>clean_zip_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>The actual size of the downloaded CAL-ACCESS zip after the downloaded completed</td>
        </tr>
        <tr>
            <td>download_zip_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>The size of the zip containing all cleaned raw data files and error logs</td>
        </tr>


    </tbody>
    </table>
    </div>

**Instance methods and propertites:**

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">


        <tr>
            <td><code>RawDataVersion.download_completed</code></td>
            <td>Check if the download of the version's zip file completed. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.download_stalled</code></td>
            <td>Check if the download of the version's zip file started but did not complete. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.extract_completed</code></td>
            <td>Check if the extract of files from the downloaded zip completed. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.extract_stalled</code></td>
            <td>Check if the extract of files from the downloaded zip started but did not complete. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.update_completed</code></td>
            <td>Check if the database update to the version completed. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.update_stalled</code></td>
            <td>Check if the database update to the version started but did not complete. Return <code>True</code> or <code>False</code>.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.pretty_clean_size()</code></td>
            <td>Returns a prettified version (e.g., "725M") of the zip of clean data files and error logs.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.pretty_download_size()</code></td>
            <td>Returns a prettified version (e.g., "725M") of the actual size of the downloaded zip.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.pretty_expected_size()</code></td>
            <td>Returns a prettified version (e.g., "725M") of the expected size of the downloaded zip.</td>
        </tr>


    </tbody>
    </table>
    </div>


----------------------

RawDataFile
~~~~~~~~~~~

Data files included in the given version of the CAL-ACCESS raw source data.

**Fields:**

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
            <td>file_name</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Name of the raw source data file without extension</td>
        </tr>


        <tr>
            <td>download_records_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of records in the original file downloaded from CAL-ACCESS</td>
        </tr>


        <tr>
            <td>clean_records_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of records in the cleaned file generated by calaccess_raw</td>
        </tr>


        <tr>
            <td>load_records_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of records in the loaded from cleaned file into calaccess_raw's data model</td>
        </tr>


        <tr>
            <td>download_columns_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of columns in the original file downloaded from CAL-ACCESS</td>
        </tr>


        <tr>
            <td>clean_columns_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of columns in the cleaned file generated by calaccess_raw</td>
        </tr>


        <tr>
            <td>load_columns_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of columns on the loaded calaccess_raw data model</td>
        </tr>


        <tr>
            <td>download_file_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive of the original raw data file downloaded from CAL-ACCESS.</td>
        </tr>


        <tr>
            <td>clean_file_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive of the raw data file after being cleaned.</td>
        </tr>


        <tr>
            <td>clean_file_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>Size of the .CSV file</td>
        </tr>


        <tr>
            <td>download_file_size</td>
            <td>Integer</td>
            <td>No</td>
            <td>Size of the .TSV file</td>
        </tr>


        <tr>
            <td>error_log_archive</td>
            <td>FileField</td>
            <td>No</td>
            <td>An archive of the error log containing lines from the original download file that could not be parsed and are excluded from the cleaned file.</td>
        </tr>


        <tr>
            <td>error_count</td>
            <td>Integer</td>
            <td>No</td>
            <td>Count of records in the original download that could not be parsed and are excluded from the cleaned file.</td>
        </tr>


        <tr>
            <td>version_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Foreign key referencing the version of the raw source data in which the file was included.</td>
        </tr>


        <tr>
            <td>clean_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the cleaning of the file started</td>
        </tr>


        <tr>
            <td>clean_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the cleaning of the file finished</td>
        </tr>


        <tr>
            <td>load_start_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the loading of the file started</td>
        </tr>


        <tr>
            <td>load_finish_datetime</td>
            <td>DateTime</td>
            <td>No</td>
            <td>Date and time when the loading of the file finished</td>
        </tr>

       
   	</tbody>
    </table>
    </div>


**Instance methods and propertites:**

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">


        <tr>
            <td><code>RawDataVersion.model()</code></td>
            <td>Returns the RawDataFile's corresponding CalAccess database model object.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.pretty_clean_file_size</code></td>
            <td>Returns a prettified version of the clean_file_size size.</td>
        </tr>
        <tr>
            <td><code>RawDataVersion.pretty_download_file_size</code></td>
            <td>Returns a prettified version of the download_file_size size.</td>
        </tr>


    </tbody>
    </table>
    </div>
