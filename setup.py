from setuptools import setup
import sys

setup(
    # Basic package information.
    name = 'zdgen',
    author = 'Brent Woodruff',
    version = '1.0.0',
    scripts = ['bin/zdgen'],
    author_email = 'brent@fprimex.com',
    packages = ['zdgen'],
    include_package_data = True,
    install_requires = ['requests', 'inflection', 'beautifulsoup4'],
    license='LICENSE.txt',
    url = 'https://github.com/fprimex/zdesk_apigen',
    keywords = 'zendesk api helpdesk',
    description = 'Zendesk API generator which uses developer.zendesk.com',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 3',
    ],
)

