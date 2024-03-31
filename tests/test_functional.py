pytest_plugins = ('pytester',)


def get_results(recorder):
    '''filter records to get only call results'''
    results = {}
    for result in recorder.getreports():
        when = getattr(result, 'when', None)
        if when is None:
            continue
        test_name = result.nodeid.split('::')[-1]
        results[test_name, when] = result.outcome
    return results


TEST_SAMPLE = """
import pytest

def test_ok():
    assert 3 == 1 + 2

@pytest.mark.flaky
def test_mf():
    assert 3 == 2
"""


def test_ignore_flaky(testdir, capsys):
    test = testdir.makepyfile(TEST_SAMPLE)
    rec = testdir.inline_run('--ignore-flaky', test)
    results = get_results(rec)
    assert results['test_ok', 'call'] == 'passed'
    assert results['test_mf', 'call'] == 'skipped'


def test_fail_flaky(testdir, capsys):
    test = testdir.makepyfile(TEST_SAMPLE)
    rec = testdir.inline_run(test)
    results = get_results(rec)
    assert results['test_ok', 'call'] == 'passed'
    assert results['test_mf', 'call'] == 'failed'


TEST_SAMPLE_SUCCEED = """
import pytest

@pytest.mark.flaky
def test_flaky_ok():
    assert 3 == 3
"""


def test_success_flaky(testdir, capsys):
    test = testdir.makepyfile(TEST_SAMPLE_SUCCEED)
    rec = testdir.inline_run('--ignore-flaky', test)
    results = get_results(rec)
    assert results['test_flaky_ok', 'call'] == 'passed'
