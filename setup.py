"""Installer for talisker-flask-example
"""

import os
from setuptools import setup, find_packages


setup(
    name='talisker-flask-example',
    description='An example Hello World Talisker/Flask application',
    long_description=open('README.rst').read(),
    version='1.0.0',
    author='Wes Mason',
    author_email='wesley.mason@canonical.com',
    url='https://github.com/canonical-ols/talisker-flask-example/',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=open(
        os.path.join(os.path.dirname(__file__),
            'requirements.txt')).readlines(),
    entry_points={
        'console_scripts': [
            'helloworld = helloworld.__init__:main',
        ],
    },
    license='AGPL3'
)
