======================
Cookiecutter Simple PyPackage
======================

.. image:: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/
    :alt: Updates

.. image:: https://travis-ci.org/audreyfeldroy/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.org/github/audreyfeldroy/cookiecutter-pypackage
    :alt: Build Status

.. image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
    :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/ZordoC/cookiecutter-simple-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``pytest``.
* Formatting (black, docformatter, isort).
* Linting (flake8, pylint).
* Pre-commit configured.
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/ZordoC/cookiecutter-simple-pypackage/

Dev Container (VScode)
----------------------
There's a development Dockerfile stored in `docker/`, highly recommend having distinct Dockerfiles for different enviroments.
You need to have remote-container VScode extension installed, once you have that:

1. `cd <package>`
2. Open Pallet `CMD + SHIFT + P` (MacOS).
3. Select `Remote-Containers: Reopen in container`.
4. Develop your features.


Local development
-----------------

    cd <package-name>;

    python -m venv .venv

    ..venv/bin/activate

    make venv-dev

    git init

    pre-commit install

    git add .

    git commit -m "First commit"


Run tests, linters & formatters.
-----------------------

    make tests

    make format

    make lint


Documentation
-----------------------
Pre-built documentation setup!

    make docs



Distribute your package
-----------------------
You can distribute via wheel file (https://www.reddit.com/r/learnpython/comments/78xtap/eli5_python_wheels/).

    make dist







.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

