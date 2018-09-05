import codecs
import os
import re

from setuptools import setup, find_packages

setup(
    name='user-query-optimizer',
<<<<<<< HEAD
    version='0.1.2',
=======
    version='0.1.0',
>>>>>>> ordering
    author='Swathi Iyer',
    author_email='swathii@stanford.edu',
    packages=['user_query_optimizer'],
    url='https://github.com/mozilla/user-query-optimizer',
    license='LICENSE.txt',
    description='SQL query optimization hints',
    long_description=open('README.md').read(),
)
