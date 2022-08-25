#!/usr/bin/env bash

read e

printf "%.3f" $(echo  "scale=10; $e" | bc)
