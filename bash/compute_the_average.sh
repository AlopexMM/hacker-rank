#!/usr/bin/env bash

sum=0
read divider

for ((i=0; i<divider; i++))
do
    read input
    sum=`expr $sum + $input`
done

printf "%.3f" $(echo "scale=10;  $sum / $divider" | bc) 
