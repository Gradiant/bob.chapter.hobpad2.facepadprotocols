.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

============
Installation
============

Linux Installation
------------------

1. Install conda -> https://conda.io/docs/user-guide/install/index.html

2. Create the conda env from file (environment_linux.yml)

Note: You should be inside the package directory (bob.chapter.hobpad2.facepadprotocols)

.. code-block:: sh

    $ conda env create -f enviroments/environment_linux.yml

3. Activate the environment

.. code-block:: sh

    $ source activate hobpad2_chapter14_env


4. Buildout the bob package

.. code-block:: sh

    $ #You should be inside the activated conda env (hobpad2_chapter14_env)
    $ python bootstrap-buildout.py
    $ bin/buildout

5. Clone the bob package

.. code-block:: sh
    
    $ git clone https://github.com/Gradiant/bob.chapter.hobpad2.facepadprotocols 

6. Buildout the bob package

.. code-block:: sh

    $ #You should be inside the package directory (bob.chapter.hobpad2.facepadprotocols)
    $ cd bob.chapter.hobpad2.facepadprotocols
    $ python bootstrap-buildout.py
    $ bin/buildout


Mac OS x Installation
---------------------
not yet supported.

