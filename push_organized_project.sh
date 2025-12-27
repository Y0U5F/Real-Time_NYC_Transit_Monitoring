#!/bin/bash

cd "/home/joo/New Folder/Real-Time_NYC_Transit_Monitoring"

echo "🚀 Starting Git setup and push..."

# Initialize git if needed
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
fi

# Set remote
echo "🔗 Setting up remote..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/Y0U5F/Real-Time_NYC_Transit_Monitoring.git

# Add all files
echo "📝 Adding all files..."
git add -A

# Show what will be committed
echo ""
echo "📋 Files to be committed:"
git status --short

# Commit
echo ""
echo "💾 Creating commit..."
git commit -m "Initial commit: Organized project structure

- Organized code into src/pipeline with proper structure
- Separated ingestion, bronze, silver, and gold layers  
- Moved documentation to docs/ folder
- Added requirements.txt and .gitignore
- Updated all file paths to work with new structure
- All original code logic preserved"

# Set main branch
git branch -M main

# Push to GitHub
echo ""
echo "☁️  Pushing to GitHub..."
echo "⚠️  Note: You may need to authenticate with GitHub"
git push -u origin main --force

echo ""
echo "✅ Done! Check your repository at:"
echo "   https://github.com/Y0U5F/Real-Time_NYC_Transit_Monitoring"

