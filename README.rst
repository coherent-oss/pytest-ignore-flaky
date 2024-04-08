.. image:: https://img.shields.io/pypi/v/pytest-ignore-flaky.svg
   :target: https://pypi.python.org/pypi/pytest-ignore-flaky

.. image:: https://img.shields.io/pypi/pyversions/pytest-ignore-flaky.svg
   :target: https://pypi.python.org/pypi/pytest-ignore-flaky

.. image:: https://github.com/coherent-oss/pytest-ignore-flaky/actions/workflows/main.yml/badge.svg
   :target: https://github.com/coherent-oss/pytest-ignore-flaky/actions?query=workflow%3Atests


pytest-ignore-flaky
====================

ignore failures from flaky tests (pytest plugin)

A "flaky" test is a test that usually pass but sometimes it fails.
You should always avoid flaky tests but not always possible.

This plugin can be used to optionally ignore failures from flaky tests.

First "mark" your tests with the `flaky` marker::

  import random
  import pytest

  @pytest.mark.flaky
  def test_mf():
      assert 0 == random.randint(0, 1)

By default this mark is just ignored, unless the plugin is activated from the
command line (or `py.test` config file)::

  py.test --ignore-flaky

If a flaky test pass it will be reported normally as test succeed.
If the test fails, instead of being reported as failure it will be reported as
a `xfail`.


pytest compatibility
====================

Tested with pytest 6.2 (2021-04-23).


Project Details
===============

 - Project code + issue track on github - https://github.com/coherent-oss/pytest-ignore-flaky
 - PyPI - https://pypi.python.org/pypi/pytest-ignore-flaky


license
=======

The MIT License
Copyright (c) 2015-2019 Eduardo Naufel Schettino and Marcos Alfredo Camargo Leal Pinto

see LICENSE file
