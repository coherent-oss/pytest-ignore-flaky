import os.path

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fp:
    README_TEXT = fp.read()


setup(name = 'pytest-ignore-flaky',
      description = 'ignore failures from flaky tests (pytest plugin)',
      version = '2.1.0',
      author = 'Eduardo Naufel Schettino, Marcos Alfredo Camargo Leal Pinto',
      author_email = 'schettino72@gmail.com, marcos.alfredo@gmail.com',
      url = 'https://github.com/schettino72/pytest-ignore-flaky',
      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Operating System :: POSIX',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                     'Programming Language :: Python :: 3.11',
                     'Programming Language :: Python :: 3.12',
                     'Topic :: Software Development :: Testing',
                     ],
      py_modules = ['pytest_ignore_flaky'],
      install_requires = [
          'pytest>=6.0',
      ],
      entry_points = {
        'pytest11': ['pytest_ignore_flaky = pytest_ignore_flaky'],
        },
      long_description = README_TEXT,
      python_requires = ">=3.6",
      )
