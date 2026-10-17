import pytest


def test_ok():
    assert 3 == 1 + 2


@pytest.mark.flaky
def test_mf():
    assert 3 == 2  # noqa: PLR0133 (deliberately failing sample test)
