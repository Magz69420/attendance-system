#!/usr/bin/env bash

# Set the remote URL to use SSH authentication
git remote set-url origin git@github.com:Magz69420/attendance-system.git

# Navigate to the directory containing the script
cd "$(dirname "${BASH_SOURCE[0]}")"

# Check if there are any changes in the repository
if [[ -n $(git status -s) ]]; then
    echo "Changes found. Pushing changes..."
    git add -A && git commit -m 'update' && git push
else
    echo "No changes found. Skip pushing."
fi
