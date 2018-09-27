from setuptools import setup, Extension, find_packages

module_a_compiler = Extension('iamanextension',
                              sources = ['iamanextension/extension.c'])

setup(
    ext_modules = [module_a_compiler],
)