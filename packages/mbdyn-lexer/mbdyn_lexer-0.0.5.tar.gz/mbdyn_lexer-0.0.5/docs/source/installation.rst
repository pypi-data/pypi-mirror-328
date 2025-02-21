.. _installation:
Installation
============

Install **mbdyn-lexer** plugin from `Python Package Index <https://pypi.org/project/mbdyn-lexer/>`_ (PyPi). The preferred tool for installing packages from PyPI is **pip**, which is included in all modern versions of Python.

**Run** the following command to install the **plugin** and the required `Pygments <https://pygments.org/>`_ Package:

.. code-block:: console

   (.venv) $ pip install mbdyn-lexer


.. note::
   It is recommended to use a virtual environment when working with third party packages. Documentation can be found at `Create and Use Virtual Environments <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments>`_.

   
**Check** installation with:

.. code-block:: console

   (.venv) $ pygmentize -H lexer mbdyn

**Output** below shows successful installation. See :ref:`examples` for usage scenarios.

.. code-block:: console

   Help on the MBDyn lexer:

   A MBDyn input file lexer.
