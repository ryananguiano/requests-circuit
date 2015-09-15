import pytest
import unittest

import requests_circuit


class RequestsTestCase(unittest.TestCase):

    def setUp(self):
        """Create simple data set with headers."""
        pass

    def tearDown(self):
        """Teardown."""
        pass

    def test_entry_points(self):
        requests_circuit.breaker
