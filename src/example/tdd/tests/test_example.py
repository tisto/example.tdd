import unittest2 as unittest

from example.tdd.testing import \
    EXAMPLE_TDD_INTEGRATION_TESTING


class ExampleIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_TDD_INTEGRATION_TESTING

    def setUp(self):
        pass

    def test_success(self):
        sum = 1 + 3
        self.assertEqual(sum, 4)
