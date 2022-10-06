#! /bin/bash

list=('A', 'B', 'C')

echo "${list[@]}"

# index
echo "${!list[@]}"

# len
echo "${#list[@]}"