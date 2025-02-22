from setuptools import setup, find_packages

setup(
    name='shared_authentication',
    version='0.1.2',
    packages=find_packages(include=['shared_authentication', 'shared_authentication.*']),
    install_requires=[
        'Django>=3.0',
        'djangorestframework>=3.11',
    ],
    include_package_data=True,
    description='A shared authentication package for Django microservices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shahroze Butt',
    author_email='shahroze@techjkc.ca',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)