# 🚀 How to Run Your AI Accelerator Toolkit

## 📱 Option 1: Run Locally (Immediate Testing)

### Step 1: Navigate to the project directory
```bash
cd /Users/sumanmukherjee_admin/Library/Mobile\ Documents/com\~apple\~CloudDocs/ML\ my\ work\ /AI\ Tool\ kit\ poc/ai-accelerator-toolkit
```

### Step 2: Run the Streamlit app
```bash
streamlit run main.py
```

### Step 3: Access the app
The app will automatically open in your browser at:
- **Local URL:** http://localhost:8501
- **Network URL:** http://192.168.29.234:8501 (accessible from other devices on your network)

---

## 🌐 Option 2: Deploy to Streamlit Cloud (FREE Public URL)

### Step 1: Push to GitHub
```bash
# First, create a repository on GitHub.com
# Then run:
./deploy_to_github.sh
```

### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub (use smn.mukherjee@gmail.com)
3. Click "New app"
4. Fill in:
   - Repository: `your-github-username/ai-accelerator-toolkit`
   - Branch: `main`
   - Main file path: `main.py`
5. Click "Deploy"

### Step 3: Your Public URL
Once deployed, your app will be available at:
```
https://[your-github-username]-ai-accelerator-toolkit.streamlit.app
```

Example: If your GitHub username is `smukherjee`, your URL would be:
```
https://smukherjee-ai-accelerator-toolkit.streamlit.app
```

---

## 🔗 Share Your App

### For Local Development:
- **URL to share on same network:** http://192.168.29.234:8501
- **For demo purposes:** Take screenshots or record screen

### For Public Access:
- **Streamlit Cloud URL:** https://[username]-ai-accelerator-toolkit.streamlit.app
- **Custom Domain:** Can be configured in Streamlit Cloud settings (optional)

---

## 📊 What Your App Includes:

1. **Change Readiness Dashboard** - Interactive visualizations
2. **Blueprint Generator** - Click to generate architectures
3. **ROI Estimator** - Calculate business value
4. **MLOps Starter Kit** - Download templates

---

## 🛠️ Troubleshooting

### If streamlit command not found:
```bash
pip install streamlit
```

### If port 8501 is already in use:
```bash
streamlit run main.py --server.port 8502
```

### To stop the app:
Press `Ctrl + C` in the terminal

---

## 💡 Quick Tips

1. **Keep the app running** while demonstrating
2. **Use Chrome or Firefox** for best compatibility
3. **The app is responsive** - works on mobile too
4. **Data is included** - no additional setup needed

---

## 📞 Need Help?

- Your email: smn.mukherjee@gmail.com
- The app is ready to run immediately
- All data is pre-generated
- No cloud costs - runs locally or free on Streamlit Cloud