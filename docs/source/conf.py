# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OC-listings'
copyright = '2023, Sandy'
author = 'Sandy'
# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Support for docstrings
    # Add other Sphinx extensions as needed
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'