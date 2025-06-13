# 🚀 Deployment Instructions for AI Accelerator Toolkit

**Email:** smn.mukherjee@gmail.com

## Step 1: Create GitHub Repository

1. **Go to GitHub:**
   - Open https://github.com
   - Sign in with smn.mukherjee@gmail.com

2. **Create New Repository:**
   - Click the "+" icon → "New repository"
   - Repository name: `ai-accelerator-toolkit`
   - Description: "Enterprise AI Transformation Platform - $45M+ Proven Impact"
   - Set to **Public** (required for free Streamlit hosting)
   - DO NOT initialize with README (we already have one)
   - Click "Create repository"

3. **Copy your repository URL:**
   - It will look like: `https://github.com/YOUR_USERNAME/ai-accelerator-toolkit.git`

## Step 2: Push to GitHub

Run these commands in Terminal:

```bash
cd /Users/sumanmukherjee_admin/Library/Mobile\ Documents/com\~apple\~CloudDocs/ML\ my\ work\ /AI\ Tool\ kit\ poc/ai-accelerator-toolkit

# Add your GitHub repository (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ai-accelerator-toolkit.git

# Push to GitHub
git push -u origin master
```

**If prompted for credentials:**
- Username: YOUR_GITHUB_USERNAME
- Password: Use a Personal Access Token (not your password)
  - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Generate new token with 'repo' scope
  - Use this token as password

## Step 3: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit https://share.streamlit.io
   - Click "Sign in with GitHub"
   - Authorize Streamlit

2. **Create New App:**
   - Click "New app"
   - Fill in:
     - Repository: `YOUR_USERNAME/ai-accelerator-toolkit`
     - Branch: `master` (or `main` if that's your default)
     - Main file path: `main.py`
   - Click "Deploy"

3. **Wait for Deployment:**
   - Takes 2-5 minutes
   - You'll get a URL like: `https://YOUR_USERNAME-ai-accelerator-toolkit.streamlit.app`

## Step 4: Your App URLs

Once deployed, you'll have:

- **GitHub Repository:** `https://github.com/YOUR_USERNAME/ai-accelerator-toolkit`
- **Live App:** `https://YOUR_USERNAME-ai-accelerator-toolkit.streamlit.app`

## 📧 Sharing Your Success

Once deployed, you can:

1. **Update LinkedIn:**
   - Add the live app URL to your profile
   - Post using the LinkedIn draft provided

2. **Email Signature:**
   - Add: "🚀 Check out my AI Accelerator Toolkit: [your-app-url]"

3. **Resume/CV:**
   - Include the GitHub and live app URLs

## 🆘 Troubleshooting

**If GitHub push fails:**
```bash
# Check if remote is set correctly
git remote -v

# If needed, remove and re-add
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/ai-accelerator-toolkit.git
```

**If Streamlit deployment fails:**
- Check that your repo is public
- Verify main.py is in the root directory
- Check requirements.txt has all dependencies

## 📞 Need Help?

If you encounter any issues:
1. Check the error messages carefully
2. Ensure all file paths are correct
3. Verify your GitHub repository is public

---

**Ready to deploy! Follow these steps and your AI Accelerator Toolkit will be live in minutes.**