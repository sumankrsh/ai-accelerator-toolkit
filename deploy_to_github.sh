#!/bin/bash

echo "🚀 AI Accelerator Toolkit - GitHub Deployment Script"
echo "=================================================="

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "\n${YELLOW}Step 1: Create a new repository on GitHub${NC}"
echo "1. Go to: https://github.com/new"
echo "2. Repository name: ai-accelerator-toolkit"
echo "3. Description: Enterprise AI Transformation Platform - $45M+ ROI Impact"
echo "4. Make it PUBLIC (required for free hosting)"
echo "5. DON'T initialize with README"
echo "6. Click 'Create repository'"

echo -e "\n${GREEN}Press Enter after creating the repository...${NC}"
read

echo -e "\n${YELLOW}Step 2: Enter your GitHub username${NC}"
read -p "GitHub username: " GITHUB_USERNAME

# Set remote origin
echo -e "\n${YELLOW}Setting up GitHub remote...${NC}"
git remote add origin https://github.com/$GITHUB_USERNAME/ai-accelerator-toolkit.git 2>/dev/null || git remote set-url origin https://github.com/$GITHUB_USERNAME/ai-accelerator-toolkit.git

# Push to GitHub
echo -e "\n${YELLOW}Pushing to GitHub...${NC}"
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✅ Successfully pushed to GitHub!${NC}"
    echo -e "\nYour repository: https://github.com/$GITHUB_USERNAME/ai-accelerator-toolkit"
    
    echo -e "\n${YELLOW}Next Steps for FREE Deployment:${NC}"
    echo "1. Go to: https://share.streamlit.io"
    echo "2. Sign in with GitHub"
    echo "3. Click 'New app'"
    echo "4. Select your repository: $GITHUB_USERNAME/ai-accelerator-toolkit"
    echo "5. Main file: main.py"
    echo "6. Click 'Deploy'"
    echo -e "\n${GREEN}Your app will be live at: https://$GITHUB_USERNAME-ai-accelerator-toolkit.streamlit.app${NC}"
else
    echo -e "\n${YELLOW}If push failed, you may need to authenticate:${NC}"
    echo "1. Go to GitHub → Settings → Developer settings → Personal access tokens"
    echo "2. Generate a new token with 'repo' permissions"
    echo "3. Use the token as your password when prompted"
fi