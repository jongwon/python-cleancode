#!/bin/bash

N=$1
if [[ "$N" == "" ]]; then
    N=1;
fi

pytest \
    --cov-report term-missing \
    --cov=ch8.coverage.coverage_$N \
    test_coverage_$N.py
