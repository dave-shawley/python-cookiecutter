FROM python:3.5
MAINTAINER {{cookiecutter.author}} <{{cookiecutter.author_email}}>

ADD . /source
WORKDIR /source
RUN ./setup.py install
CMD python -c 'import {{cookiecutter.package_name}}; {{cookiecutter.package_name}}.run()'
