#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import alabaster

from {{cookiecutter.package_name}} import __version__, version_info


project = '{{cookiecutter.package_name}}'
copyright = '{{cookiecutter.year}}, {{cookiecutter.author}}'
version = __version__
release = '.'.join(str(x) for x in version_info[:2])

needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]
templates_path = []
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_static_path = []
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ],
}
html_theme_options = {
    'description': '{{cookiecutter.description}}',
    'github_user': '{{cookiecutter.github_org}}',
    'github_repo': '{{cookiecutter.package}}',
}

intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
}
