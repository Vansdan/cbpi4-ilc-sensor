from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-ilc-sensor',
      version='0.0.1',
      description='Generic CraftBeerPi HTTP Sensor Plugin',
      author='Daniel Lauterbach',
      author_email='vansdan@web.de',
      url='https://github.com/Vansdan/cbpi4-ilc-sensor',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-ilc-sensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-ilc-sensor'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
