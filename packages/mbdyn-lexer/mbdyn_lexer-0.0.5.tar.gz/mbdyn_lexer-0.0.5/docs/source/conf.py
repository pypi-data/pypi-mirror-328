# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from pathlib import Path

#sys.path.append(str(Path('examples').resolve()))
#sys.path.append(str(Path('src/mbdyn_lexer').resolve()))
#sys.path.append(str(Path('tests').resolve()))

#from src.mbdyn_lexer import __about__

#import mbdynlexer

project = 'mbdyn-lexer'
copyright = '2025, Andre Zettel'
author = 'musipadcom'
#release = __about__.__version__
#version = __about__.__version__
release = '0.0.4'
version = '0.0.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_index = 'index.html'
#lexers = {'mbdyn' : mbdynlexer.MBDynLexer}
