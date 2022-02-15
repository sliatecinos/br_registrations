# Configuration file for the Sphinx documentation builder.
# -- Path setup information -------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
autodoc_mock_imports = ['br_registrations']

# -- Project information ----------------------------------------
project = 'br-registrations'
copyright = '2022, sliatecinos'
author = 'Sliatecinos'

release = '0.1'
version = '0.0.0.9'

# -- General configuration -------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -----------------------------------
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output -----------------------------------
epub_show_urls = 'footnote'
