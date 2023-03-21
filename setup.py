#! /usr/bin/env python
"""
Setup for mymodule
"""
from setuptools import setup

requirements = ['numpy>=1.0']

setup(
    name='mymodule',
    version=0.1,
    # install_requires=get_requirements(),
    install_requires=requirements,
    python_requires='>=3.7',
    entry_points={'console_scripts': ['sky_sim=mymodule.sky_sim:main']}
)