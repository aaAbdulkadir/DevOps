#! /bin/bash

echo "Enter a file name to check: "
read file # saves echo as a variable


if [ -f $file ]
then
    echo "$file exists"
else
    echo "$file does not exist."
fi