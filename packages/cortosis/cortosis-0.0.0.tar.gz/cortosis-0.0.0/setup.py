# -*- coding: utf-8 -*-
#
# This file is part of cortosis.
#
# Copyright (C) 2025 Interstellio IO (PTY) LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import sys
from importlib.machinery import SourceFileLoader

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Requires `setuptools` to be installed')
    print('`pip install setuptools`')
    exit()

# DEFINE ROOT PACKAGE NAME
PACKAGE = 'cortosis'

##############################################################################
# DO NOT EDIT CODE BELOW THIS POINT ##########################################
##############################################################################

MYDIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIRECTORY = os.path.join(MYDIR, PACKAGE)
sys.path.insert(0, MYDIR)
os.chdir(MYDIR)

# Load Metadata from PACKAGE
metadata = SourceFileLoader(
    'metadata', os.path.join(MYDIR, CODE_DIRECTORY,
                             'metadata.py')).load_module()


# Miscellaneous helper functions
def requirements(path):
    dependency = []
    if os.path.exists(os.path.join(os.path.dirname(__file__), path)):
        with open(os.path.join(os.path.dirname(__file__), path)) as req:
            dependency = req.read().splitlines()

    return dependency


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


# install-requires.txt as install_requires
# minimal dependencies to run.
install_requires = requirements('requirements.txt')

# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.author,
    author_email=metadata.email,
    maintainer=metadata.author,
    maintainer_email=metadata.email,
    license=metadata.license,
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=metadata.classifiers,
    packages=find_packages(exclude=()),
    install_requires=install_requires,
    zip_safe=False,  # don't use eggs
    python_requires='>=3.10',
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
