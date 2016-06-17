"""Packaging entry point."""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().split()

with open('requirements-test.txt') as f:
    test_requirements = f.read().split()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    name='Scraper',
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='scraper.tests',
)
