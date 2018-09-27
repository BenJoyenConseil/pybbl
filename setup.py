from setuptools import setup, Extension, find_packages

setup(
    name='pybbl',
    version='1.0.0.dev0',
    install_requires=['colored', 'pandas', 'numpy'],
    packages=find_packages(),
)