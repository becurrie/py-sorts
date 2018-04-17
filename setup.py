"""setup.py: setuptools control."""

import re
from setuptools import setup


version = re.search('^__version__\s*=\s*"(.*)"',
                    open('py_sorter/sorter.py').read(),
                    re.M
                    ).group(1)

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")


setup(
    name='py-sorts',
    packages=['py_sorter'],
    entry_points={'console_scripts': ['py_sorter = py_sorter.sorter.main']},
    version=version,
    description="Sort integer lists using python in the command line.",
    long_description=long_description,
    author='Brett Currie',
    author_email='brettecurrie@gmail.com',
    url='http://www.github.com/becurrie/py-sorts'
)
