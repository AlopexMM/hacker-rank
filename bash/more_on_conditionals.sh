#!/usr/bin/env bash

read x
read y
read z

if [[ $x -eq $y && $x -eq $z ]]; then
    echo "EQUILATERAL"
elif [[ $x -eq $y && $x != $z ]]; then 
    echo "ISOSCELES"
elif [[ $x -eq $z && $x != $y ]]; then
    echo "ISOSCELES"
elif [[ $y -eq $z && $y != $x ]]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi