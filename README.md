# bob.chapter.hobpad2.facepadprotocols
 
[Bob](https://www.idiap.ch/software/bob/) package for reproducing the results of chapter on Challenges of Face Presentation Attack Detection in Real Scenarios.


## Installation

1. Install conda -> https://conda.io/docs/user-guide/install/index.html

2. Create the conda env from file (environment_linux.yml)

Note: You should be inside the package directory (bob.chapter.hobpad2.facepadprotocols)

~~~
    conda env create -f enviroments/environment_linux.yml
~~~

3. Activate the environment

~~~
   source activate hobpad2_chapter14_env
~~~

4. Buildout the bob package

~~~
    #You should be inside the activated conda env (hobpad2_chapter14_env)
    python bootstrap-buildout.py
    bin/buildout
~~~

Note it is only tested on linux platforms.

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


## Console scripts

~~~
  bin/reproducible_research.py
~~~

## Reproducible Research

Follow the[Doc](https://gradiant.github.io/bob.chapter.hobpad2.facepadprotocols/) gerenated with sphinx. If it is not generated yet, please be patient and create it with the instruction above. 

