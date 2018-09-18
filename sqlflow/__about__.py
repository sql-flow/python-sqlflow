# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from pkg_resources import get_distribution, DistributionNotFound

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "sqlflow"
__summary__ = "Workflow engine in SQL"
__uri__ = "https://github.com/sql-flow/python-sqlflow"

__author__ = "Christophe CHAUVET"
__email__ = "christophe.chauvet@gmail.com"

__license__ = "BSD"
__copyright__ = "Copyright 2017-2018 %s" % __author__

try:
    __version__ = get_distribution('sqlflow').version
except DistributionNotFound:
    # package is not installed
    __version__ = None
