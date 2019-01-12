FROM acostapazo/bob.gradiant:latest

MAINTAINER acosta@gradiant.org

RUN conda install bob.ip.qualitymeasure
RUN pip install py-cpuinfo
RUN pip install dill==0.2.7.1
RUN pip install coloredlogs
RUN apt-get install -y wget unzip