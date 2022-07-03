#!/usr/bin/env python
"""Unit tests for `{{ cookiecutter.project_slug }}` package."""
import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def test_lowercase_input():
    """Simple test for lowercase_input demo function.
        You don't need to have both tests and doctest, one should be fine.
        Keep doctest for simple functions and use the testing module for
        elaborate code that may require some sort of setup
    """
    sentence = "Hi My Name is Jose"
    result = {{ cookiecutter.project_slug }}.lowercase_input(sentence)
    assert result == "hi my name is jose"