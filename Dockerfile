FROM conda/miniconda3:latest

MAINTAINER acosta@gradiant.org || acosta@alicebiometrics.com

RUN apt-get update && apt-get install -y wget unzip git libboost-all-dev pkg-config

COPY envs/ubuntu_environment.yml /envs/
RUN conda env create -f envs/ubuntu_environment.yml
RUN git clone https://github.com/Gradiant/bob.chapter.hobpad2.facepadprotocols.git
WORKDIR bob.chapter.hobpad2.facepadprotocols
RUN . activate bob.chapter.hobpad2.facepadprotocols && ./ci.sh

ENTRYPOINT [". activate bob.chapter.hobpad2.facepadprotocols && /rr.sh"]

ENV LANG C.UTF-8
