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
"""Project metadata

Information describing the project.
"""
from datetime import datetime

# The package name, which is also the "UNIX name" for the project.
package = 'cortosis'
project = package.title()
project_no_spaces = project.replace(' ', '')
# Please follow https://www.python.org/dev/peps/pep-0440/
version = '0.0.0'
description = project
author = 'Interstellio IO (PTY) LTD'
email = 'opensource@interstellio.io'
license = 'Apache 2.0'
copyright = '2025-%s %s' % (datetime.now().year, author,)
url = "https://github.com/interstellio/cortosis"
identity = project + ' v' + version

# Classifiers
# <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.10',
    'Topic :: Internet :: WWW/HTTP']
