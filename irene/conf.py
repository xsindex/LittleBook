# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = 'Little Book'
copyright = 'Little Book'
author = 'xsindex'
release = '0.0.1'
language = 'zh_CH'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}


# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,
    # 'prev_next_buttons_location': 'both'
}
html_static_path = ['static']
html_title = "Auto Book"
html_logo = os.path.normpath(os.path.join(html_static_path[0], r'images/logo.png'))
html_favicon = os.path.normpath(os.path.join(html_static_path[0], r'images/favicon-32x32.png'))

html_last_updated_fmt = "%b %d %H:%M:%S, %Y"
# the ref links are self-managed
html_permalinks = False

html_copy_source = False
html_use_index = True
html_domain_indices = False

html_js_files = [
    'js/mermaid.min.js'     # current version 10.9.1
]
# Options for HTML output


# extensions and options
extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinx_design',
    'sphinx_toolbox.assets',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
]

# mermaid
mermaid_version = ""
# extensions and options

# downloadable documents path
assets_dir = r"document/"

