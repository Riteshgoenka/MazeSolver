#!/bin/bash
if [ "$#" -eq 3 ]
then
	python decoder.py $1 $2 $3
else
	python decoder.py $1 $2
fi