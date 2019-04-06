from setuptools import setup

import codecs
import os.path as path

# where this file is located
cwd = path.dirname(__file__)

version = '0.0.0'
# read version file to get version
with codecs.open(path.join(cwd, 'mlbstat/version.py'), 'r', 'ascii') as f:
    exec(f.read())
    version = __version__
# make sure version is not default
# make sure file reading worked
assert version != '0.0.0'

setup(name='mlbstat',
      version=version,
      description='Client library for the MLB statsapi',
      url='https://github.com/dreamforth/mlbstat',
      author='Andre Guerlain',
      author_email='apguerlain+dreamforth@gmail.com',
      license='MIT',
      packages=['mlbstat'],
      zip_safe=False)
