import os
from setuptools import setup, find_packages
import subprocess
import logging
# from py_visuo import __version__, __doc__, __author__, __title__, __author_email__

PACKAGE_NAME = 'py_visuo'


# setup(
#     name=__title__,
#     version=__version__,
#     description=__doc__,
#     author=__author__,
#     author_email=__author_email__,
#     packages=find_packages(),
#     long_description=open('README.txt').read(),
#     install_requires=[
#                         "numpy>=1.22",
#                         "pandas>=1.4",
#                         "matplotlib>=3.5",
#                         "seaborn>=0.11.2",
#                         "tqdm>=4.64",
#     ]
# )


setup(
    name='py_visuo',
    version='0.0.1',    
    description='Collection of functions and classes for creating beautiful and informative plots in Python',
    url='https://github.com/francescapalermo/py_visuo/',
    author='Francesca Palermo',
    author_email='f.palermo@imperial.ac.uk',
    license='MIT-License',
    packages=find_packages(),
    install_requires=[  "numpy>=1.22",
                        "pandas>=1.4",
                        "matplotlib>=3.5",
                        "seaborn>=0.11.2",
                        "scipy>=1.8",]

)
