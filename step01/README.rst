Step 1: Installation
====================

In order to build an API with Flask_, first you need to be sure that Python
and Flask are both installed and working properly on your computer. You should
also set up a `virtual environment`_ for your API.

Check Python
------------

Flask is implemented in the Python_ programming language, so you should first
check to see if you have Python installed and runnable on your computer.
To do that, open the command line and try to run the Python interpreter,
like this:

.. code-block:: bash

    $ python

If that works, you should now be inside the Python interpreter, which looks
something like this:

.. code-block::

    Python 3.5.1 (default, Dec  7 2015, 21:59:10)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

If you are running a different version of Python, that's fine. If you get an
error, you'll need to install Python, which is outside the scope of this
tutorial.

Once you've verified that you can run the Python interpreter, quit it by
typing ``quit()`` and pressing enter. Quitting the interpreter will return
you to the command line shell, where you were before.

In addition to checking the Python interpreter, you should also check
that you can run Pip, which is the tool used for installing Python packages.
Try running it like this:

.. code-block:: bash

    $ pip --version

If that works, you should see output that looks something like this:

.. code-block::

    pip 8.1.1 from /usr/local/lib/python3.5/site-packages (python 3.5)

If you are running a different version of Pip, that's fine. If you get an
error, you'll need to fix it, which is outside the scope of this tutorial.

Create a Virtual Environment
----------------------------

A `virtual environment`_ is an isolated area where you can install Python
packages without those packages affecting any others on your computer.
Python 3 comes with a tool called ``pyvenv`` that can make
virtual environments. To make a virtual environment on Python 3, run it
like this:

.. code-block:: bash

    $ pyvenv venv

If you are using Python 2, you'll need to install the virtualenv_ package
with Pip, and use the ``virtualenv`` command that it installs.
Install the package like this:

.. code-block:: bash

    $ pip install virtualenv

When the installation is complete, run the command like this:

.. code-block:: bash

    $ virtualenv venv

Once you've created your virtural environment, you'll need to activate it any
time you want to use it. To activate it, use the following command:

.. code-block:: bash

    $ source venv/bin/activate

You'll need to re-activate the virtual environment every time you run a new
command line window or tab. For more information about creating and using
virtual enviornments,
`see the Python documentation on virtual environments`_.

Install Flask
-------------
In order to use Flask, you must install it. Since you are using a virtual
environment, it must be installed *into* that virtual environment. Once you
have a virtual environment and you've activated it, install Flask with
the following command:

.. code-block:: bash

    $ pip install flask

Once the installation is complete, double-check that it was successfully
installed by trying to import it, like this:

.. code-block:: bash

    $ python
    Python 3.5.1 (default, Dec  7 2015, 21:59:10)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import flask
    >>>

If you do not get any errors, then you imported Flask successfully.

`Step 2: Hello World <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step02>`_
======================

.. _Flask: http://flask.pocoo.org/
.. _Python: https://www.python.org/
.. _virtual environment: https://virtualenv.pypa.io
.. _virtualenv: https://virtualenv.pypa.io
.. _see the Python documentation on virtual environments: https://packaging.python.org/en/latest/installing/#creating-virtual-environments
