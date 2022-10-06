#! /bin/bash

function funcName()
{
    echo "Hello function"
}
# calls function
funcName

function second()
{
    echo $@
}
second this one is weird

function realtype()
{
    variable="This is the functinoal way"
    echo "$variable"
}
realtype