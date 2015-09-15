"""
Requests Circuit Breaker
~~~~~~~~~~~~~~~~~~~~~
A circuit breaker for Python requests.

:copyright: (c) 2015 by Ryan Anguiano.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'requests-circuit'
__version__ = '0.1.0'
__author__ = 'Ryan Anguiano'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Ryan Anguiano'


# Import entry points
from .breaker import breaker

from . import utils

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
