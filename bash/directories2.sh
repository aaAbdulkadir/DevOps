#! /bin/bash

echo "Enter a directory name to check: "
read directory # saves echo as a variable


if [ -d "$direct" ]
then
    echo "$direct exists"
else
    echo "$directory does not exist, creating directory..."
    mkdir $directory
    echo "$directory created!"
fi
