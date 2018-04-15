from setuptools import setup, find_packages

setup(
    name='sorter',
    author_email='brettecurrie@gmail.com',
    author='becurrie',
    version='0.1.7',
    description='sort integers with different sorting algorithms.',
    packages=find_packages(),
    py_modules=['sorter.sorter'],
    entry_points={'console_scripts': ['sorter = sorter.sorter:main']},
    license='MIT',
    url='https://github.com/becurrie/sorters-py',
    keywords=['sorting', 'algorithm', 'console', 'application'],
)
