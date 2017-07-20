Custom Project Settings
=======================

The settings listed below allow you to customize the behavior our apps to suit your needs. They should be declared in your Django project's ``settings.py`` file. 

Read more about Django settings `here <https://docs.djangoproject.com/en/1.11/topics/settings/>`_.

----------------------


CALACCESS_DATA_DIR
----------------------
The local directory where the ``calaccess_raw`` and ``calaccess_processed`` management commands will download, extract and write files. By default, this is will be ``{BASE_DIR}/data/``, where ``BASE_DIR`` is a setting pre-populated in ``settings.py`` when you set up a new Django project.

.. note::

    If you modify this setting, make sure the directory you specify is one to which all users have write and execute permissions.


CALACCESS_STORE_ARCHIVE
---------------------------
Enable archiving of all ``.ZIP``, ``.TSV`` and ``.CSV`` files in order to preserve each snapshot of the raw and processed CAL-ACCESS data. Be default, archiving is *disabled*.

If you enable archiving, files will be saved in your Django project's default storage system, specified in ``DEFAULT_FILE_STORAGE`` in your ``settings.py`` file. For example, we use `django-storages <https://django-storages.readthedocs.io/en/latest/>`_ to upload our archived files to an `AWS Simple Service Storage (S3) <https://aws.amazon.com/s3/>`_ bucket. 

If you enable archiving without configuring ``DEFAULT_FILE_STORAGE``, files will be stored in the directory specified in your Django project's ``MEDIA_ROOT``. 

You can read more about how Django manages file storage `here <https://docs.djangoproject.com/en/1.11/topics/files/>`_.
