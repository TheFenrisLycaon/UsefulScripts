#!/bin/bash
while read file; do
    wget ${file} -cbP ~/Downloads/Anime/
done < k.txt
