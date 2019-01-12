.. vim: set fileencoding=utf-8 :
.. Gradiant's Biometrics Team <biometrics.support@gradiant.org>
.. Copyright (C) 2017 Gradiant, Vigo, Spain

==================================================================
Challenges of Face Presentation Attack Detection in Real Scenarios
==================================================================


Bob package to reproduce the work carried out in chapter Challenges of Face Presentation Attack Detection in Real Scenarios in the Handbook of Biometric Anti-Spoofing.

Abstract
--------

In the current context of digital transformation, the increasing trend in the use of personal devices for accessing online services has fostered the necessity of secure cyberphysical solutions. Biometric technologies for mobile devices, and face recognition specifically, have emerged as a secure and convenient approach. However, such a mobile scenario also brings some specific threats, and spoofing attack detection is, without any doubt, one of the most challenging. Although much effort has been devoted in anti-spoofing techniques over the past few years, there are still many challenges to be solved when implementing these systems in real use cases. This chapter analyses some of the gaps between research and real scenario deployments, including generalisation, usability, and performance. More specifically, we will focus on how to select and configure an algorithm for real scenario deployments, paying special attention to use cases involving limited processing capacity devices (e.g., mobile devices), and we will present a publicly available evaluation framework for this purpose.


Acknowledgements
----------------

If you use this framework, please cite the following publication::

    @Inbook{Costa-Pazo2019,
        author="Costa-Pazo, Artur and Vazquez-Fernandez, Esteban and Alba-Castro, Jos{\'e} Luis and Gonz{\'a}lez-Jim{\'e}nez, Daniel",
        editor="Marcel, S{\'e}bastien and Nixon, Mark S. and Fierrez, Julian and Evans, Nicholas",
        title="Challenges of Face Presentation Attack Detection in Real Scenarios",
        bookTitle="Handbook of Biometric Anti-Spoofing: Presentation Attack Detection",
        year="2019",
        publisher="Springer International Publishing",
        address="Cham",
        pages="247--266",
        isbn="978-3-319-92627-8",
        doi="10.1007/978-3-319-92627-8_12",
        url="https://doi.org/10.1007/978-3-319-92627-8_12"
    }


This package contains scripts to reproduce the results from the paper. The package also provides score files for IQM and GRADIANT PAD algorithms, the systems reported in the chapter.

Reproducible Research
---------------------

The easiest way to reproduce the result presented in the chapter is using docker.

.. code-block:: sh

    $ docker pull acostapazo/bob.chapter.hobpad2.facepadprotocols:latest

Once you have downloaded the docker image, you can type:

.. code-block:: sh

    $ docker run -v $(pwd):/bob.chapter.hobpad2.facepadprotocols acostapazo/bob.chapter.hobpad2.facepadprotocols:latest bin/bash -c "cd bob.chapter.hobpad2.facepadprotocols; ./ci.sh; ./rr.sh"

Then, the results will be available on the folder result/chapter

.. code-block:: sh

    result/chapter/
    ├── results
    │   ├── fig_5_a_iqm.png
    │   ├── fig_5_b_gradiant.png
    │   ├── fig_6_a_iqm.png
    │   ├── fig_6_b_gradiant.png
    │   ├── table_1_gradiant.html
    │   └── table_1_iqm.html
    └── summary.html



Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   reproducible_research
   user_guide
   acknowledgements

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`





