#!/bin/bash

set -e

python3 --version
./example.py
python3 -m unittest example_test

echo Вроде всё неплохо
