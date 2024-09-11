#!/bin/bash

# Define mathvar1 as 1 + 5
mathvar1=$((1 + 5))

# Calculate mathvar2 as mathvar1 * 20
mathvar2=$((mathvar1 * 20))

# Define mathvar3 as 10
mathvar3=10

# Calculate mathvar4 as mathvar1 * (mathvar2 + mathvar3)
mathvar4=$((mathvar1 * (mathvar2 + mathvar3)))

# Display the results in the desired format
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."



