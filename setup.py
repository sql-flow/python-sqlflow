# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


def rst(filename):
    return open(path.join(here, filename), encoding='utf-8').read()


# Get the long description from the README file and CHANGELOG
long_description = '\n'.join((
    rst('README.rst'),
    rst('CHANGELOG.rst'),
    ''
))


def version_scheme(version):
    from setuptools_scm.version import guess_next_dev_version
    version = guess_next_dev_version(version)
    return version.lstrip("v")


setup(
    name='sqlflow',
    setup_requires=[
        'setuptools_scm'
    ],
    use_scm_version={
        'write_to': "sqlflow/version.py",
        'version_scheme': version_scheme,
    },

    description='sqlflow management in python',
    long_description=long_description,

    url='https://github.com/sql-flow/python-sqlflow',

    author='Mirounga Team',
    author_email='info@mirounga.net',

    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='workflow, sql',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'psycopg2-binary==2.7.5',
    ],
)
