#!/bin/bash
while read file; do
    wget ${file} -b
done < k.txt