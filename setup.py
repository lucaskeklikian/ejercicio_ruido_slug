#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/ejercicio_ruido_slug.svg
        :target: https://pypi.python.org/pypi/ejercicio_ruido_slug
.. image:: https://img.shields.io/travis/lkeklikian/ejercicio_ruido_slug.svg
        :target: https://travis-ci.org/lkeklikian/ejercicio_ruido_slug

Agregar ruido 


Links:
---------
* `Github <https://github.com/lkeklikian/ejercicio_ruido_slug>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', "numpy>=1.23.3"]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="lkeklikian",
    author_email='lkeklikian@leafnoise.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Agregar ruido ",
    entry_points={
        'console_scripts': [
            'ejercicio_ruido_slug=ejercicio_ruido_slug.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='ejercicio_ruido_slug',
    name='ejercicio_ruido_slug',
    packages=find_packages(include=['ejercicio_ruido_slug']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lkeklikian/ejercicio_ruido_slug',
    version='0.1.0',
    zip_safe=False,
)
