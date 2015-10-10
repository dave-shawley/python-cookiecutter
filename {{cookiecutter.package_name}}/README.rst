{{cookiecutter.package_name}}
{{ '=' * (cookiecutter.package_name|length) }}

{{cookiecutter.description}}

Getting Started
---------------
Use Python 3 if you can.

- ``pyvenv env`` to create a new virtual environment to work in
- ``./env/bin/python setup.py develop`` to set up basic requirements
- ``./env/bin/pip install nose`` to install the test runner
- ``./env/bin/nosetests`` to run the tests
