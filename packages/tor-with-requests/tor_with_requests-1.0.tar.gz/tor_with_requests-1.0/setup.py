from setuptools import setup

setup(
    name='tor_with_requests',
    version='1.0',
    packages=['tor_with_requests'],
    package_dir={'tor_with_requests': '.'},
    py_modules=['tor_with_requests'],
    author='Mathias Bochet (aka Zen)',
    description='A wrapper for the requests package that proxies all traffic through Tor.',
    long_description="A wrapper for the requests package that proxies all traffic through Tor.",
    url='https://github.com/42zen/tor_requests'
)