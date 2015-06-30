from unittest import TestCase

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from faker.generator import random
from nose.plugins import PluginTester

from seedfaker import SeedFaker


class TestSeedFaker(PluginTester, TestCase):

    activate = '--with-seed-faker'
    plugins = [SeedFaker()]

    @patch.object(random, 'seed')
    def setUp(self, mock_seed):
        self.mock_seed = mock_seed
        super(TestSeedFaker, self).setUp()

    def test_calls_seed(self):
        expected_arg = __name__ + '.Test.runTest'
        self.mock_seed.assert_called_once_with(expected_arg)

    def makeSuite(self):
        class Test(TestCase):
            def runTest(self):
                pass
        return [Test('runTest')]
