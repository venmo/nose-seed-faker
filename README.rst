nose-seed-faker
===============

A nose plugin for seeding the
`faker <https://github.com/joke2k/faker>`__ package based on test names.

::

    $ nosetests --with-seed-faker mytests/

Faker is seeded at the beginning of each test based on the test name, so
each test that uses faker will use the same fake data between test runs,
regardless of test order.

This relies on the
`behavior <https://github.com/joke2k/faker/blob/acd0de23563b69a95611406dddf9c09e04d579b3/faker/generator.py#L53>`__
that faker seeds a instance of random that is shared globally across
instances of the Faker class, so seeding *any* instance of Faker will
seed *every* instance of Faker.

For example, these two tests use faker to generate fake email addresses:

.. code:: python

    import unittest

    from faker import Faker

    fake = Faker()


    class TestEmail(unittest.TestCase):
        def test_one(self):
            email = fake.email()
            print(email)

        def test_two(self):
            email = fake.email()
            print(email)

Since faker generates random email addresses, if we run ``test_one``
multiple times, we'll use different emails for each test run:

::

    $ nosetests -v --nocapture tests.py:TestEmail.test_one tests.py:TestEmail.test_one
    test_one (tests.TestEmail) ... opouros@hermistondeckow.com
    ok
    test_one (tests.TestEmail) ... sgrady@hotmail.com
    ok

    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

While this is good for increasing the surface area of emails we use in
our tests, it can cause flaky tests -- a test could mysteriously fail,
but if you tried running it again to debug the failure, all of a sudden
it's passing again!

``nose-seed-faker`` solves this problem by seeding faker based on the
name of each test. Using the plugin, if you run the same test multiple
times, it'll use the same email address:

::

    $ nosetests --with-seed-faker -v --nocapture tests.py:TestEmail.test_one tests.py:TestEmail.test_one
    test_one (tests.TestEmail) ... mitchel07@yost.com
    ok
    test_one (tests.TestEmail) ... mitchel07@yost.com
    ok

    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

Each individual test will use a different email, so we still get a good
surface area of emails to use in our tests:

::

    $ nosetests --with-seed-faker -v --nocapture tests.py
    test_one (tests.TestEmail) ... mitchel07@yost.com
    ok
    test_two (tests.TestEmail) ... kurt.bartell@yahoo.com
    ok

    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK

Installation
============

::

    $ pip install nose-seed-faker

Warning
=======

Versions ``0.5.2`` and lower of faker will seed the ``random`` module
globally.

Version ``0.5.3`` `fixes <https://github.com/joke2k/faker/pull/259>`__
this issue by seeding an instance of the ``random.Random`` class, but at
the time of this writing, this fix hasn't been released to PyPI yet.

Until version ``0.5.3`` is released on PyPI, you can install it like so:

::

    $ pip install git+http://github.com/joke2k/faker.git@dabf922af72783ebd9d163611ab0f4f307156443#egg=fake-factory==0.5.3
