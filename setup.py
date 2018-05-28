# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='PPI Sanitiser',
    long_description=readme,
    author='Lindsay Smith',
    author_email='wapdat@gmail.com',
    url='https://github.com/wapdat/ppi-sanitise',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)