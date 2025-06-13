# 🚀 Deploy Your AI Accelerator Toolkit NOW

## Option 1: GitHub + Streamlit Cloud (Recommended) - 100% FREE

### Step 1: Push to GitHub
```bash
cd /Users/sumanmukherjee_admin/Library/Mobile\ Documents/com\~apple\~CloudDocs/ML\ my\ work\ /AI\ Tool\ kit\ poc/ai-accelerator-toolkit

# Run the deployment script
./deploy_to_github.sh
```

The script will guide you through:
1. Creating a GitHub repository
2. Pushing your code
3. Setting up Streamlit deployment

### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub (use smn.mukherjee@gmail.com)
3. Click "New app"
4. Select your repo: `ai-accelerator-toolkit`
5. Main file: `main.py`
6. Deploy!

**Your app URL**: `https://[username]-ai-accelerator-toolkit.streamlit.app`

---

## Option 2: Vercel Landing Page (Optional)

If you want a landing page on Vercel that links to your Streamlit app:

### Prerequisites
```bash
# Install Vercel CLI
npm i -g vercel
```

### Deploy to Vercel
```bash
cd /Users/sumanmukherjee_admin/Library/Mobile\ Documents/com\~apple\~CloudDocs/ML\ my\ work\ /AI\ Tool\ kit\ poc/ai-accelerator-toolkit

# Deploy
vercel

# Follow prompts:
# - Set up and deploy: Y
# - Which scope: Select your account
# - Link to existing project: N
# - Project name: ai-accelerator-toolkit
# - Directory: ./
# - Override settings: N
```

**Your Vercel URL**: `https://ai-accelerator-toolkit.vercel.app`

---

## 🎯 What You Get

### With Streamlit Cloud:
- ✅ Full interactive web application
- ✅ All 4 modules working
- ✅ Real-time dashboards
- ✅ Data processing
- ✅ 100% FREE forever

### With Vercel:
- ✅ Professional landing page
- ✅ Fast loading
- ✅ Custom domain support
- ✅ Links to your Streamlit app
- ✅ Also FREE

---

## 📱 Manual GitHub Push (if script doesn't work)

1. **Create repository** at https://github.com/new
   - Name: `ai-accelerator-toolkit`
   - Public repository
   - Don't initialize with README

2. **Push your code**:
```bash
cd /Users/sumanmukherjee_admin/Library/Mobile\ Documents/com\~apple\~CloudDocs/ML\ my\ work\ /AI\ Tool\ kit\ poc/ai-accelerator-toolkit

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/ai-accelerator-toolkit.git

# Push
git push -u origin main
```

3. **If authentication fails**:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select 'repo' scope
   - Use token as password

---

## 🔗 Important URLs

- **GitHub**: https://github.com/YOUR_USERNAME/ai-accelerator-toolkit
- **Streamlit App**: https://YOUR_USERNAME-ai-accelerator-toolkit.streamlit.app
- **Vercel Landing**: https://ai-accelerator-toolkit.vercel.app

---

## ⚡ Quick Commands

```bash
# View your app locally
streamlit run main.py

# Push updates to GitHub (auto-deploys to Streamlit)
git add .
git commit -m "Update"
git push

# Deploy to Vercel
vercel --prod
```

---

**Need help?** Email: smn.mukherjee@gmail.com