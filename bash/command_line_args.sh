#! /bin/bash

# need dollar sign. when running script, put in 2 arguments. 0 indicates file name
# echo $0 $1 $2

# method 2: as array
args=("$@")

# echo ${args[0]} ${args[1]} ${args[2]}

# prints array
echo $@

# prints length of array
echo $#