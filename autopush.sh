#!/bin/bash

# Change directory to your Git repository
cd /home/Denji/attendance-system

# Add all changes to the staging area
git add .

# Commit changes with a default message
git commit -m "Automatic commit by autopush script"

# Push changes to the remote repository
git push origin master
