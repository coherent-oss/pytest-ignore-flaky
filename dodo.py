from doitpy.pyflakes import Pyflakes
from doitpy.package import Package


DOIT_CONFIG = {
    'default_tasks': [
        'pyflakes',
    ]
}


def task_pyflakes():
    flakes = Pyflakes()
    yield flakes.tasks('*.py')
    yield flakes.tasks('tests/*.py')


def task_package():
    """create/upload package to pypi"""
    pkg = Package()
    yield pkg.revision_git()
    yield pkg.manifest_git()
    yield pkg.sdist()
    yield pkg.sdist_upload()
