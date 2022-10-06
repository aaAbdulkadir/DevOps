#! /bin/bash

# go in each folder and make a txt file
for i in {1..20}
do
	mkdir folder$i
	cd folder$i
	touch text$i.txt
	cd ..
done

# start..stop..increment