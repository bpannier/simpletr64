
import re
import sys
import os
from distutils.core import setup
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'simpletr64',
    'simpletr64.actions',
    'simpletr64.tools'
]

version = ''
with open('simpletr64/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='simpleTR64',
    version=version,
    packages=['simpletr64', 'simpletr64.tools', 'simpletr64.actions', 'tests'],
    scripts=['bin/simpletr64_discover'],
    install_requires=['requests'],
    url='http://bpannier.github.io/simpletr64/',
    license='Apache 2.0',
    author='Benjamin Pannier',
    author_email='sourcecode@ka.ro',
    description='An easy to use UPnP TR64 protocol library',
    long_description=readme + '\n\n' + history,

     # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        'Topic :: Home Automation',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Software Development :: Libraries',
    ],

    keywords='TR64 protocol network UPnP',

)
