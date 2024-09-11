#!/bin/bash

# Define 'floating' using bc with scale set to 3 decimal places
floating=$(echo "scale=3; 4.5 / 1.7" | bc)

# Display the result
echo "Our floating variable is $floating"
