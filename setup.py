from setuptools import setup

# Save people like Pat from themselves:
import sys
if sys.version_info < (3,0):
    sys.exit('Sorry, Python < 3.0 is not supported')

import re
VERSIONFILE="tockci/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='tock-ci',
      version=verstr,
      description='TockOS Continuous Integration Testing Tool',
      long_description='Please visit `Github <https://github.com/tock/tock-ci>`_ for more information.',
      author='Tock Project Developers',
      author_email='tock-dev@googlegroups.com',
      url='https://github.com/tock/tock-ci',
      packages=['tockci'],
      package_data = {
          'tests': ['tests/*.toml']
      },
      entry_points={
        'console_scripts': [
          'tock-ci = tockci.main:main'
        ]
      },
      install_requires=[
          "argcomplete >= 1.8.2",
          # "colorama >= 0.3.7",
          # "crcmod >= 1.7",
          "pyserial >= 3.0.1",
          "pytoml >= 0.1.20",
          "sh >= 1.12.13",
          ],
     )
