# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Code (regular expresssions and NTLK) to tokenise (remove) Private Personal Information (PPI) in Python.',
    long_description=readme,
    author='Lindsay Smith',
    author_email='wapdat@gmail.com',
    url='https://github.com/wapdat/ppi-sanitise',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)