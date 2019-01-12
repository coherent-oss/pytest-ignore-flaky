import os.path

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as fp:
    README_TEXT = fp.read()


setup(name = 'pytest-ignore-flaky',
      description = 'ignore failures from flaky tests (pytest plugin)',
      version = '1.0.0',
      license = 'MIT',
      author = 'Eduardo Naufel Schettino, Marcos Alfredo Camargo Leal Pinto',
      author_email = 'schettino72@gmail.com, marcos.alfredo@gmail.com',
      url = 'http://pypi.python.org/pypi/pytest-ignore-flaky',
      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Operating System :: POSIX',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Topic :: Software Development :: Testing',
                     ],
      py_modules = ['pytest_ignore_flaky'],
      install_requires = [
          'pytest>=3.7',
      ],
      entry_points = {
        'pytest11': ['pytest_ignore_flaky = pytest_ignore_flaky'],
        },
      long_description = README_TEXT,
      )
