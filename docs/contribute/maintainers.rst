Version release checklist
=========================

The steps to follow each time release a new version of a Django package.

* Update the changelog
* Update ``setup.py`` with new version and any new dependencies

    * Consider including RC (release candidate) in release name until we're sure we're uploading a package with all tiny details accounted for

* Update ``requirements.txt`` with any new dependencies
* Run ``python setup.py sdist bdist_wheel``, make sure their aren't any errors
* Spotcheck new release package in dist/ to make sure all files made it in.
* Run ``python setup.py sdist bdist_wheel upload``
* Release on GitHub

    * ``git commit`` final change and run ``git tag "v#.#.#"`` with whatever the release number is
    * Run ``git push origin master --tags``
    * Add list of changes to the page release on GitHub
