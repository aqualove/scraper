"""Packaging entry point."""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().split()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    name='Scraper',
    version=version,
    packages=find_packages(),
    setup_requires=requirements,
)
