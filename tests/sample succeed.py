import pytest


@pytest.mark.flaky
def test_flaky_ok():
    assert 3 == 3
