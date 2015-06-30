try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = [
    'fake-factory',
]

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

# Get version number from the package without importing it.
# This puts __version__ (and anything else defined in
# _version.py) in our namespace.
version_filepath = 'seedfaker/_version.py'
with open(version_filepath) as version_file:
    exec(compile(version_file.read(), version_filepath, 'exec'))

setup(
    name='nose-seed-faker',
    maintainer='Amy Hanlon',
    maintainer_email='amy@venmo.com',
    url='https://github.com/venmo/nose-seed-faker',
    version=__version__,    # noqa
    description=('A Nose plugin that seeds the faker package.'),
    long_description=readme + '\n\n' + history,
    packages=['seedfaker'],
    entry_points={
        'nose.plugins.0.10': [
            'seed-faker = seedfaker:SeedFaker',
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
