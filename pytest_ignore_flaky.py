"""
pytest-ignore-flaky : ignore failures from flaky tests (pytest plugin)
https://pypi.python.org/pypi/pytest-ignore-flaky

The MIT License - see LICENSE file
Copyright (c) 2015 Eduardo Naufel Schettino
"""

import pytest

class PluginIgnoreFlaky(object):

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(self, item, call):
        '''Turn failures into xfail if test is marked as "flaky".'''
        outcome = yield
        if item.get_closest_marker('flaky'):
            report = outcome.get_result()
            if report.outcome == 'failed':
                report.outcome = 'skipped'
                report.wasxfail = 'skip flaky test failure'


def pytest_addoption(parser):
    '''py.test hook: register argparse-style options and config values'''
    group = parser.getgroup("ignore-flaky", "ignore flaky tests")
    group.addoption(
        '--ignore-flaky', action="store_true",
        dest="ignore_flaky", default=False,
        help="ignore flaky tests ")


def pytest_configure(config):
    '''Register plugin only if any of its option is specified
    '''
    if config.option.ignore_flaky:
        config.pluginmanager.register(PluginIgnoreFlaky())
