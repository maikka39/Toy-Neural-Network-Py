from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Toy-Neural-Network-Py',
    version='0.1.0',
    description='Neural Network Python library for experimenting with Machine Learning',
    long_description=readme,
    author='Maik de Kruif',
    author_email='maikka39@gmail.com',
    url='https://github.com/maikka39/Toy-Neural-Network-Py',
    license=license,
    packages=find_packages(exclude=('docs'))
)
