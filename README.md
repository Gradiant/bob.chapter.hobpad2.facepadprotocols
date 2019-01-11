# bob.chapter.hobpad2.facepadprotocols
 
[Bob](https://www.idiap.ch/software/bob/) package for reproducing the results of chapter on [Challenges of Face Presentation Attack Detection in Real Scenarios](https://link.springer.com/chapter/10.1007/978-3-319-92627-8_12).

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

## Docker 

The fastest way to contact the package is to use docker. 

You can download the docker image from dockerhub

~~~
docker pull acostapazo/bob.gradiant:latest 
~~~

or build it from Dockerfile

~~~
docker build --no-cache -t acostapazo/bob.gradiant:latest  .
~~~

To check if everything is alright you can run the ci.sh script with:

~~~
docker run -v $(pwd):/bob.chapter.hobpad2.facepadprotocols acostapazo/bob.gradiant:latest bin/bash -c "cd bob.chapter.hobpad2.facepadprotocols; ./ci.sh"
~~~

## Installation (Manual)


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


## Reproducible Research

Follow the [Doc](https://gradiant.github.io/bob.chapter.hobpad2.facepadprotocols/) gerenated with sphinx. If it is not generated yet, please be patient and create it with the instruction above. 

