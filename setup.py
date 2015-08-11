import os.path

from distutils.core import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as fp:
    README_TEXT = fp.read()


setup(name = 'pytest-ignore-flaky',
      description = 'ignore failures from flaky tests (pytest plugin)',
      version = '0.1.0',
      license = 'MIT',
      author = 'Eduardo Naufel Schettino',
      author_email = 'schettino72@gmail.com',
      url = 'http://pypi.python.org/pypi/pytest-ignore-flaky',
      classifiers = ['Development Status :: 4 - Beta',
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
                     'Topic :: Software Development :: Testing',
                     ],
      py_modules = ['pytest_ignore_incremental'],
      install_requires = [
          'pytest>=2.7',
      ],
      entry_points = {
        'pytest11': ['pytest_ignore_flaky = pytest_ignore_flaky'],
        },
      long_description = README_TEXT,
      )

