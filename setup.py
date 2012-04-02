#!/usr/bin/env python
#
#  Copyright (c) 2011-2012 Corey Goldberg (http://goldb.org)
#
#  This file is part of linux-metrics
#
#  License :: OSI Approved :: MIT License:
#      http://www.opensource.org/licenses/mit-license
# 
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#


""" setup/install script for linux-metrics """



import os
from distutils.core import setup

from linux_metrics import __version__


this_dir = os.path.abspath(os.path.dirname(__file__))
long_desc = '\n%s' % open(os.path.join(this_dir, 'README.rst')).read()


setup(
        name = 'linux-metrics',
        version = __version__,
        description = 'linux-metrics - System Metrics/Stats for Linux',
        author = 'Corey Goldberg',
        author_email = 'corey@goldb.org',
        url = 'https://github.com/cgoldberg/linux-metrics',
        download_url = 'http://pypi.python.org/pypi/linux-metrics',
        packages = ['linux_metrics'],
        platforms = ['Linux'],
        license = 'MIT',
        classifiers = [
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Monitoring',
            ]
     )
     
