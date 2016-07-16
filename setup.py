from distutils.core import setup
import setuptools

setup(
    name='NameGen',
    version='0.0.1',
    description='Python tool for random name generation',
    author='George Nagel',
    author_email='',
    url='https://github.com/GeorgeNagel/name-gen.git',
    packages=setuptools.find_packages(exclude=['*.tests']),
    package_data={
        '""': "*.txt",
    },
)
