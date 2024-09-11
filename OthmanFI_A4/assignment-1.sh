#!/bin/bash

echo "The time and date are: "
Date


echo "Let's see who is logged into the system: "
who

user=$(whoami)
home_dir=$HOME
echo "For $user, the home directory is $home_dir"
