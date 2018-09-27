from setuptools import setup, Extension, find_packages

setup(
    name='pybbl',
    version='1.0.0.dev0',
    install_requires=['colored', 'pandas', 'numpy'],
    packages=find_packages(),
    py_modules=['iamamodule'],
    scripts=['bin/iamascript'],
    include_package_data=True, # https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
    package_data={
            '': ['data/*.csv'], # https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
        }
)