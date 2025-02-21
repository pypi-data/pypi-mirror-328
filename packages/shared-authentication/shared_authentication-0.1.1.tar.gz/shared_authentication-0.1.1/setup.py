from setuptools import setup, find_packages

setup(
    name='shared_authentication',
    version='0.1.1',  # Increment the version number
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'djangorestframework>=3.11',
    ],
)