#!/bin/bash

echo -e "\n\t\t4Anime Downlader Script.\t\n"
echo -e "====================================================\n"


if [[ "$1" == "-g" ]]
then
    python src/main.py $2 $3 $4 $5 
elif [[ "$1" == "-d" ]]
then
    python src/download.py
else
    echo -e "\t[1] Generate\t\t[2] Download"
    read choice
    if [ "$choice" == '1' ]
    then
        python src/main.py $2 $3 $4 $5 
    else
        python src/download.py
    fi
fi
