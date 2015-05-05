#!/usr/bin/env python3
#
# Copyright (C) 2015 Tomas Radej <tradej@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

def _get_requirements():
    with open('requirements.txt') as fh:
        packages = fh.readlines()
    return [p.strip() for p in packages if not p.strip().startswith('#')]

setup(
    name='nulecule_validator',
    version='0.0.1',
    description='Validator library for the Nulecule application spec',
    long_description=''.join(open('README.md').readlines()),
    keywords='nulecule,validation',
    author='Tomas Radej',
    author_email='tradej@redhat.com',
    license='GPLv3',
    packages=find_packages(),
    install_requires=_get_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ]
)
