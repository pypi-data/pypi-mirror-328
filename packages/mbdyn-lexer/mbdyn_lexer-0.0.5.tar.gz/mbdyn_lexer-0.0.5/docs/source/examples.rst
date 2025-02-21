.. _examples:

Examples
========

Preparations
------------

Download the Source Package from `mbdyn_lexer-0.0.4.tar.gz <https://pypi.org/project/mbdyn-lexer/#files>`_ , unpack and change to examples folder:

.. code-block:: console

   (.venv) $ cd examples/
   (.venv) $ ls
   exam17_body.sub
   exam17_joint.sub
   exam17_nlink_pendulum.html
   exam17_nlink_pendulum.mbd
   exam17_node.sub
   exam17.py




Command line interface
---------------------

**Pygmentize** exam17_nlink_pendulum.mbd, **overwrite** the existing file with a newly **generated** stand-alone html document:

.. code-block:: bash

   (.venv) $ pygmentize -O full,linenos="table",debug_token_types -o exam17_nlink_pendulum.html exam17_nlink_pendulum.mbd 



**Pygmentize** exam17_node.sub and show it in terminal. With suffix other than mbd, the lexer must be forced, option *-l*:

.. code-block:: bash

   (.venv) $ pygmentize -l mbdyn exam17_node.sub  # -l because suffix is not mbd

**Outputs** a highlighted version of the sub file:
   
.. code-block:: mbdyn
		
   set: Nodelabel_n = Index;
   
   structural: Nodelabel_n, dynamic,
   position,         (Index-1)*Length_Full+Length_Half, 0., 0.,
   orientation,      eye,
   velocity,         null,
   angular velocity, null;
   
See `Pygments <https://pygments.org/docs/>`_ for full documentation and/or try the `demo <https://pygments.org/demo/>`_.

Python interface
----------------

Start a python console from the virtuel environment from installation :

.. code-block:: bash

   (.venv) $ python

The prompt changes to something like this (put in here following snippets):

.. code-block:: pycon

   Type "help", "copyright", "credits" or "license" for more information.
   >>> 

Import a function that can return a lexer instance. Create the instance *LEXER*:

.. code-block:: python

   from pygments.lexers import get_lexer_by_name
   LEXER = get_lexer_by_name('mbdyn')

Define some input. Create token `generator <https://docs.python.org/3/glossary.html#term-generator>`_. Run it in a for-loop. Just print the tokens:

.. code-block:: python
  
   some_input = '''
   /* drop input below  */
   

   
   ''' # close string with triple quotes
   
   tokengenerator = LEXER.get_tokens(some_input)
   for token in tokengenerator:
     print(token)

**Output** are printed tokens. These are `tuples <https://docs.python.org/3/library/stdtypes.html#tuples>`_.

.. code-block:: python
		
   (Token.Comment.Multiline, '/*')
   (Token.Comment.Multiline, ' drop input below  ')
   (Token.Comment.Multiline, '*/')
   (Token.Text.Whitespace, '\n')

**Exit** python console and run script example exam17.py:

.. code-block:: console

   >>> exit()
   (.venv) $ python exam17.py checkfiles

The script looks for include statements in *exam17_nlink_pendulum.mbd*. If they contain a double quote string, it is assumed to be a filepath. Then its a filepath, it checks for its existence and prints the result. For more advanced usage of token processing see `Pygments API <https://pygments.org/docs/api/>`_.
