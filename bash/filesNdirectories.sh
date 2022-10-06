#! /bin/bash

mkdir -p automated_directory # -p allows the script to be ran multiple times

echo "Enter a directory name to check: "
read direct # saves echo as a variable

if [ -d "$direct" ]
then
    echo "$direct exists"
else
    echo "$directory does not exist"
fi