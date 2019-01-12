.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

============
Installation
============

Docker Installation
-------------------

1. Download the docker image

.. code-block:: sh

    $ docker pull acostapazo/bob.chapter.hobpad2.facepadprotocols:latest

2. Check your installation out.


.. code-block:: sh

    $ docker run -v $(pwd):/bob.chapter.hobpad2.facepadprotocols acostapazo/bob.chapter.hobpad2.facepadprotocols:latest bin/bash -c "cd bob.chapter.hobpad2.facepadprotocols; ./ci.sh; ./rr.sh"


Local Installation
------------------

1. Install conda -> https://conda.io/docs/user-guide/install/index.html

2. Create the conda env

.. code-block:: sh

    $ conda create --name hobpad2_chapter14_env python=2.7

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

6. Reproduce the results

.. code-block:: sh

    $ bin/reproducible_research.py

