#!/bin/bash
if [ "$#" -eq 2 ]
then
	python encoder.py $1 $2
else
	python encoder.py $1
fi