# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
project = 'McFit'
copyright = '2025, Andrés Cook'
author = 'Andrés Cook'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = []

# Courtesy of https://stackoverflow.com/questions/17927741/exclude-module-docstring-in-autodoc
def remove_module_docstring(app, what, name, obj, options, lines):
    if what == "module" and name == "McFit":
        del lines[:]

def setup(app):
    app.connect("autodoc-process-docstring", remove_module_docstring)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
