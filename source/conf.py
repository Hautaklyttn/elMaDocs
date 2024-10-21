# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sphinx_pdj_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'elMaDocs'
copyright = '2024, Hautaklyttn'
author = 'Hautaklyttn'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax', 'myst_parser']

# MathJax library 
mathjax_path = "mathJax_v3.js"

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_pdj_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
html_title = "elMaDocs"

myst_enable_extensions = {
    "attrs_block"
}

html_css_files = [
    'styleConfig.css',
    'hacks.css',
]

html_theme_options = {
	'home_link': 'hide',  
}

rst_prolog = "\n.. include:: .specialStyles.rst\n"