# -*- coding: utf-8 -*-
#
import os
import sys

import sphinx_bootstrap_theme
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bede Documentation'
copyright = u'2020, N8 CIR'
author = u'N8 CIR'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

## Added by CA to get MathJax rendering loaded
extensions = ['sphinx.ext.mathjax']
mathjax_path='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'



# -- Options for HTML output ----------------------------------------------

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'navbar_title': " ",
    'navbar_site_name': "Contents",
    'navbar_links': [
        ("Usage", "usage/index"),
        ("Hardware", "hardware/index"),
        ("Software", "software/index"),
        ("Profiling", "profiling/index"),
        ("Training", "training/index"),
        ("User Group", "bug/index"),
        ("FAQ", "faq/index"),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,
    'source_link_position': "footer",
    'bootswatch_theme': "flatly",
}
html_static_path = ['_static']

# Belt and braces: use both old and new sphinx syntax for custom CSS to make sure it loads
html_css_files = [
    'css/custom.css',
]
html_context = {
    'css_files': [
        '_static/css/custom.css'
    ]
}

html_js_files = [
    'https://use.fontawesome.com/c79ff27dd1.js',
    'js/rtd-versions.js',
]


# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = '_static/images/logo-cmyk.png'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BedeDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'BedeDoc.tex', u'BedeDoc Documentation',
     u'Mozhgan K. Chimeh', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'BedeDoc', u'BedeDoc Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BedeDoc', u'BedeDoc Documentation',
     author, 'BedeDoc', 'One line description of project.',
     'Miscellaneous'),
]


html_sidebars = {
    '**': ['localtoc.html', 'relations.html'],
    'index': [],
    'search': []
}

def setup(app):
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    if on_rtd:
        app.add_javascript('https://use.fontawesome.com/c79ff27dd1.js')
        app.add_javascript('js/rtd-versions.js')
