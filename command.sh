#!/bin/bash

cd p2_cicd

python3 -m venv ~/.p2_cicd

source ~/.p2_cicd/bin/activate

make install

az webapp up -n cjvp2app