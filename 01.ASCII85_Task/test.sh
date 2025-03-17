#!/bin/bash

set -xe

./ascii85.py
python3 -m unittest ascii85_test

echo Вроде всё неплохо
