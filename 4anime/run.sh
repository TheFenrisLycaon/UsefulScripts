#!/bin/bash
if [[ "$1" == "-g" ]]
then
    python src/main.py $2 $3 $4 $5 
elif [[ "$1" == "-d" ]]
then
    python src/download.py
fi