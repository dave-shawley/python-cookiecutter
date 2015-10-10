#!/usr/bin/env python
#

import setuptools

from {{cookiecutter.package_name}} import __version__


def read_requirements(name):
    requirements = []
    try:
        with open(name) as req_file:
            for line in req_file:
                if '#' in line:
                    line = line[:line.index('#')]
                line = line.strip()
                if line.startswith('-r'):
                    requirements.extend(read_requirements(line[2:].strip()))
                elif not line.startswith('-'):
                    requirements.append(line)
    except IOError:
        pass

    return requirements


setuptools.setup(
    name='{{cookiecutter.package_name}}',
    description='{{cookiecutter.description}}',
    long_description='\n' + open('README.rst').read(),
    packages=setuptools.find_packages(),
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.package_name}}',
    install_requires=read_requirements('requirements.txt'),
    test_require=read_requirements('test-requirements.txt'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 1 - Planning',
    ],
)
