import os
from setuptools import setup, find_packages

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read())

setup(
    name='babel-dustjs',
    version='0.1.0',
    description='DustJS Template message extractor for Babel',
    long_description=long_description,
    author='Simon Zimmermann',
    author_email='simon@insmo.com',
    packages=['babeldustjs'],
    include_package_data = True,
    zip_safe=False,
    license='BSD',
    install_requires=[],
    extras_require=dict(
        test=['pytest >= 2.0'],
        ),
    entry_points="""
    [babel.extractors]
    dustjs = babeldustjs.dustjs:extractor
    """,
    )
