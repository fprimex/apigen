from setuptools import setup
import sys

setup(
    # Basic package information.
    name = 'apigen',
    author = 'Brent Woodruff',
    version = '2.0.0',
    scripts = ['bin/apigen'],
    author_email = 'brent@fprimex.com',
    packages = ['apigen'],
    include_package_data = True,
    install_requires = ['plac', 'requests', 'inflection', 'beautifulsoup4'],
    license='LICENSE.txt',
    url = 'https://github.com/fprimex/apigen',
    keywords = 'zendesk api terraform helpdesk',
    description = 'API generator for multiple popular REST APIs',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 3',
    ],
    zip_safe = False,
)

