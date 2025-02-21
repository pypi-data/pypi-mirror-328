import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
VERSION = open(os.path.join(here, 'version')).read().strip()


setup(
    name='tfhealthchecks',
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    description='Library of health checks',
    long_description=README,
    long_description_content_type='text/markdown',
    author='sergey.yashchenko',
    author_email='sergey.yashchenko@takeoff.com',
    url='https://github.com/takeoff-com/tfhealthcheck-py',
    install_requires=[
        'requests',
        'pytest'
    ],
    test_suite='tests.tfhealthchecks'
)
