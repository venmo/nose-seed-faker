from faker import Faker
from nose.plugins import Plugin

_fake = Faker()


class SeedFaker(Plugin):
    """A plugin for seeding faker for each test.

    Faker is seeded at the beginning of each test based
    on the test name, so each test that uses faker
    will use the same fake data between test runs,
    regardless of test order.

    This relies on the behavior that faker seeds a
    instance of random that is shared globally across
    instances of the Faker class, so seeding _any_
    instance of Faker will seed _every_ instance of
    Faker.
    """

    enabled = False
    name = 'seed-faker'

    def options(self, parser, env):
        super(SeedFaker, self).options(parser, env)

    def configure(self, options, conf):
        super(SeedFaker, self).configure(options, conf)

    @staticmethod
    def beforeTest(test):
        test_path = test.id()
        _fake.seed(test_path)
