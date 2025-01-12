#!/usr/bin/env python
"""Conftest for `{{ cookiecutter.project_slug }}` package."""
import pytest
import requests


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return requests.get("https://github.com/audreyr/cookiecutter-pypackage")
