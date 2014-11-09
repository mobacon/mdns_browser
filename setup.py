#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

if sys.version_info[0] != 2 and sys.version_info[1] != 7:
    print "Sorry, only Python 2.7.x is supported (yet)."
    exit()

setup(name='mdns_browser',
      version='1.0',
      description='GUI for MDNS discovering of HTTP services in a LAN.',
      author='Sven Schlender',
      author_email='kontakt@mobacon.de',
      url='http://www.mobacon.de',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
               'snappy_generator = mdns_browser:main']},
      install_requires = ['zeroconf'],
     )
