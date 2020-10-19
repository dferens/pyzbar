#!/usr/bin/env python
import sys

import pyzbar


# Optional dependency
PILLOW = 'Pillow>=3.2.0'

URL = 'https://github.com/dferens/pyzbar/'


def readme():
    # TODO IOError on Python 2.x. FileNotFoundError on Python 3.x.
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        return 'Visit {0} for more details.'.format(URL)


setup_data = {
    'name': 'pyzbar-x',
    'version': pyzbar.__version__,
    'author': 'Lawrence Hudson',
    'author_email': 'quicklizard@googlemail.com',
    'url': URL,
    'license': 'MIT',
    'description': pyzbar.__doc__,
    'long_description': readme(),
    'long_description_content_type': 'text/x-rst',
    'packages': ['pyzbar', 'pyzbar.tests'],
    'test_suite': 'pyzbar.tests',
    'tests_require': [
        # TODO How to specify OpenCV? 'cv2>=2.4.8',
        'numpy>=1.8.2',
        PILLOW,
    ],
    'include_package_data': True,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
}


def setuptools_setup():
    from setuptools import setup
    setup(**setup_data)


if (3, 5) <= sys.version_info:
    setuptools_setup()
else:
    sys.exit('Python versions >= 3.5 are supported')
