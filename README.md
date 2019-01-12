# bob.chapter.hobpad2.facepadprotocols
 
[Bob](https://www.idiap.ch/software/bob/) package to reproduce the work carried out in chapter [Challenges of Face Presentation Attack Detection in Real Scenarios](https://link.springer.com/chapter/10.1007/978-3-319-92627-8_12) in the [Handbook of Biometric Anti-Spoofing](https://link.springer.com/book/10.1007/978-3-319-92627-8).


## Abstract 

_In the current context of digital transformation, the increasing trend in the use of personal devices for accessing online services has fostered the necessity of secure cyberphysical solutions. Biometric technologies for mobile devices, and face recognition specifically, have emerged as a secure and convenient approach. However, such a mobile scenario also brings some specific threats, and spoofing attack detection is, without any doubt, one of the most challenging. Although much effort has been devoted in anti-spoofing techniques over the past few years, there are still many challenges to be solved when implementing these systems in real use cases. This chapter analyses some of the gaps between research and real scenario deployments, including generalisation, usability, and performance. More specifically, we will focus on how to select and configure an algorithm for real scenario deployments, paying special attention to use cases involving limited processing capacity devices (e.g., mobile devices), and we will present a publicly available evaluation framework for this purpose._

## Acknowledgements

If you use this framework, please cite the following publication:

~~~
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
~~~

## Reproducible Research

The easiest way to reproduce the result presented in the chapter is using docker.

~~~
docker pull acostapazo/bob.chapter.hobpad2.facepadprotocols:latest 
~~~

Once you have downloaded the docker image, you can type:

~~~
docker run -v $(pwd):/bob.chapter.hobpad2.facepadprotocols acostapazo/bob.chapter.hobpad2.facepadprotocols:latest bin/bash -c "cd bob.chapter.hobpad2.facepadprotocols; ./ci.sh; ./rr.sh"
~~~

Then, the results will be available on the folder result/chapter

~~~
result/chapter/
├── results
│   ├── fig_5_a_iqm.png
│   ├── fig_5_b_gradiant.png
│   ├── fig_6_a_iqm.png
│   ├── fig_6_b_gradiant.png
│   ├── table_1_gradiant.html
│   └── table_1_iqm.html
└── summary.html
~~~

For more info, please check out the [Doc](https://gradiant.github.io/bob.chapter.hobpad2.facepadprotocols/).


## Installation (Local)


1. Install conda -> https://conda.io/docs/user-guide/install/index.html

2. Create the conda env

~~~
    conda create --name bob.gradiant python=2.7
~~~

3. Activate the environment and add some channels

~~~
   source activate bob.gradiant
   conda config --env --add channels defaults
   conda config --env --add channels https://www.idiap.ch/software/bob/conda
~~~

4. Install dependencies

~~~
    conda install gitpython h5py pillow scikit-learn mock sphinx_rtd_theme bob.extension bob.ip.qualitymeasure
    pip install enum34
    conda install bob.ip.qualitymeasure
    pip install py-cpuinfo
    pip install dill==0.2.7.1
    pip install coloredlogs
    apt-get install -y wget unzip
~~~


4. Buildout the bob package

~~~
    #You should be inside the activated conda env (bob.gradiant.pipelines)
    python bootstrap-buildout.py
    bin/buildout
~~

## Test

~~~
  bin/nosetests -v
~~~

## Clean

~~~
  python clean.py
~~~

## Coverage

~~~  
  bin/coverage run -m unittest discover
  bin/coverage html -i
  bin/coverage xml -i
~~~

Coverage result will be store on htmlcov/.

## Doc

~~~
bin/sphinx-build -b html doc/ doc/html/
~~~

## Update Docker 

You can build your own docker image with

~~~
docker build --no-cache -t your.user/your.image:latest  .
~~~

To check if everything is alright you can run the ci.sh script with:

~~~
docker run -v $(pwd):/bob.chapter.hobpad2.facepadprotocols your.user/your.image:latest bin/bash -c "cd bob.chapter.hobpad2.facepadprotocols; ./ci.sh"
~~~
