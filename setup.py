from setuptools import setup, find_packages
from os import path, environ
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
import codecs
import re

environ["TRAVIS"] = 'true'

here = path.abspath(path.dirname(__file__))


def read(*parts):
    with codecs.open(path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='ClauseWizard',
    version=find_version("ClauseWizard", "__init__.py"),
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=['pyparsing'],
    url='https://github.com/Shadark/ClauseWizard',
    license='GNU GPLv3',
    author='Shadark',
    author_email='fauglir@gmail.com',
    description='Python-based JSON parser for files from the Clausewitz engine,'
                ' used in multiple Paradox Interactive games.',
    keywords='clausewitz paradoxinteractive parser',
    entry_points={
        'console_scripts': [
            'CWParser=sample:main',
        ],
    },
)
