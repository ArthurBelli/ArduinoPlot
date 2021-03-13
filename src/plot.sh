#!/bin/bash

python3 Plot.py
while [ $? -ne 0 ]
do
    echo "An error occured, restarting the program"
    python3 Plot.py
done
octave plotting.m
