from setuptools import setup, find_packages
from os import path, environ
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

environ["TRAVIS"] = 'true'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='ClauseWizard',
    version='0.3.1',
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=['pyparsing'],
    url='https://github.com/Shadark/ClauseWizard',
    license='GNU GPLv3',
    author='Shadark',
    author_email='fauglir@gmail.com',
    description='Python-based JSON parser for files from the Clausewitz engine, used in multiple Paradox Interactive games.',
    keywords='clausewitz paradoxinteractive parser'
)
