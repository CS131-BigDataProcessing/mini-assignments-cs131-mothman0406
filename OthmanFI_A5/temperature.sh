#!/bin/bash
temp=$1

if [ "$temp" -lt 55 ]; then
    echo "freezing"
elif [ "$temp" -le 67 ]; then
    echo "cold"
elif [ "$temp" -le 85 ]; then
    echo "nice"
else
    echo "hot"
fi
