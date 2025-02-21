.. mbdyn-lexer documentation master file, created by
   sphinx-quickstart on Sun Feb 16 22:47:33 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Mbdyn-Lexer Documentation!
=====================================

Version: |version|

**Mbdyn-lexer** is a `Pygments <https://pygments.org/>`_ lexer plugin for processing `MBDyn <https://www.mbdyn.org>`_ input files. It enables:

 - more user-friendly expierence exploring MBDyn input files
 - colorful formatting to html, pdf, latex, css, for documentation
 - easier scripting via `Tokens <https://en.wikipedia.org/wiki/Lexical_analysis>`_, instead `regexp <https://en.wikipedia.org/wiki/Regular_expression>`_.

.. code-block:: mbdyn
		
   /* processed by MBDynLexer
   it supports multiline c-style comments
   */
   
   begin: block name;
    description: arglist;
   end: block name;
   
   # definition examples:
   set: const real x = -1.e-3;
   set: integer N;
   set: bool boo = TRUE
   set: string str_name = "strings
   can be multiline, contain \" and
   unicode ⛈️";
   set: [element,VARNAME,ELEMLABEL,joint,string="Fz"];

   #beginpreprocess  # from here use PythonLexer
   import MBDynPreprocess

   @fun(arg = {'set:': all, 2: True})
   class Foo: pass
   #endpreprocess  # back to MBDynLexer

   gravity: uniform, 0., 0., -1., const, 9.81;
   end: elements;
   
   
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   examples

	     
