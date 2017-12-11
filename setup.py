import os
from os import path
from setuptools import setup


README = open(path.join(path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(path.normpath(path.join(path.abspath(__file__), os.pardir)))

setup(
    name='django-accounts',
    version='0.3.1',  # major.minor[.patch][sub]
    packages=['accounts'],
    include_package_data=True,
    license='MIT License',
    description='Easy accounts integration for the Django web framework',
    long_description=README,
    url='https://github.com/AntycSolutions/django-accounts',
    author='Andrew Charles',
    author_email='andrew.charles@antyc.ca',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
