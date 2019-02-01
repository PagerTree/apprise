#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Chris Caron <lead2gold@gmail.com>
# All rights reserved.
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import platform
try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

from setuptools import find_packages

install_options = os.environ.get("APPRISE_INSTALL", "").split(",")
install_requires = open('requirements.txt').readlines()
if platform.system().lower().startswith('win'):
    # Windows Notification Support
    install_requires += open('win-requirements.txt').readlines()

libonly_flags = set(["lib-only", "libonly", "no-cli", "without-cli"])
if libonly_flags.intersection(install_options):
    console_scripts = []

else:
    # Load our CLI
    console_scripts = ['apprise = apprise.cli:main']

setup(
    name='apprise',
    version='0.5.2',
    description='A universal notification service',
    license='MIT',
    long_description=open('README').read(),
    url='https://github.com/caronc/apprise',
    keywords='push notifications email boxcar faast growl Join KODI '
        'Mattermost Prowl Pushalot PushBullet Pushjet '
        'Pushover Rocket.Chat Slack Toasty Telegram Twitter XBMC Stride '
        'Emby IFTTT Discord',
    author='Chris Caron',
    author_email='lead2gold@gmail.com',
    packages=find_packages(),
    package_data={
        'apprise': [
            'assets/NotifyXML-1.0.xsd',
            'assets/themes/default/*.png',
            'assets/themes/default/*.ico',
        ],
    },
    install_requires=install_requires,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ),
    entry_points={'console_scripts': console_scripts},
    python_requires='>=2.7',
    setup_requires=['pytest-runner', ],
    tests_require=open('dev-requirements.txt').readlines(),
)
