import sys


if sys.version_info < (3, 12):
    from importlib_resources import files
else:
    from importlib.resources import files


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


TEST_SAMPLE = files().joinpath('sample.py').read_text(encoding='utf-8')


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


TEST_SAMPLE_SUCCEED = files().joinpath('sample succeed.py').read_text(encoding='utf-8')


def test_success_flaky(testdir, capsys):
    test = testdir.makepyfile(TEST_SAMPLE_SUCCEED)
    rec = testdir.inline_run('--ignore-flaky', test)
    results = get_results(rec)
    assert results['test_flaky_ok', 'call'] == 'passed'
