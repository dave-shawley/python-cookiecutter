{{cookiecutter.package_name}}
{{ '=' * (cookiecutter.package_name|length) }}

{{cookiecutter.description}}

Getting Started
---------------
Use Python 3 if you can.

- ``pyvenv env`` to create a new virtual environment to work in
- ``./env/bin/pip install -r dev-requirements.txt`` to set up basic requirements
- ``. ./env/bin/activate`` to activate the virtual environment
- ``./setup.py nosetests`` to run the tests
- ``./setup.py build_sphinx`` to generate documentation
- ``./setup.py sdist`` to create a source distribution
