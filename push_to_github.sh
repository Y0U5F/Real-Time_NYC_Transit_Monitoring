#!/bin/bash

cd "/home/joo/New Folder/Real-Time_NYC_Transit_Monitoring"

# Check if .git exists, if not initialize
if [ ! -d .git ]; then
    git init
fi

# Remove existing origin if exists and add new one
git remote remove origin 2>/dev/null
git remote add origin https://github.com/Y0U5F/Real-Time_NYC_Transit_Monitoring.git

# Add all files
git add -A

# Commit
git commit -m "Initial commit: Complete Real-Time NYC Transit Monitoring project" 2>/dev/null || git commit -m "Update: Real-Time NYC Transit Monitoring project"

# Set main branch
git branch -M main

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main

echo "Done!"

