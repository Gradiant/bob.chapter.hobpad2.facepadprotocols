#!/usr/bin/env bash

function main(){
    install_package
    reproducible_research
}

function install_package(){
    python bootstrap-buildout.py
    bin/buildout
}

function reproducible_research(){
    bin/reproducible_research.py
}

main
