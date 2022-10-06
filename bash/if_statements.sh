#! /bin/bash

count=1
age=10 # no spaces

if [ $count -eq 10 ]
then
    echo 'This variable is in fact 10'
else
    echo 'This variable is not 10'
fi

if [ $count -ne 10 ]
then
    echo 'This is interesting'
else
    echo 'Boring'
fi

# have to change brackets
if (( $count > 1 )) 
then
    echo 'The sapce in the bracket is important'
else
    echo 'The syntax is very particular'
fi

# and operators: has tobe "" and not ''
if [ "$age" -gt 5 ] && [ "$age" -lt 15 ]
then
    echo 'This is a kid '
else
    echo 'Most likely a grown man'
fi