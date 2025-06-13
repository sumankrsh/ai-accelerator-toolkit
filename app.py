import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="AI Accelerator Toolkit | Choose Your Version",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(45deg, #00D4FF, #0066FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 2rem 0;
    }
    .version-card {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid #333;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .version-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #00D4FF;
    }
    .feature-list {
        color: #B0B0B0;
        line-height: 1.8;
    }
    .launch-button {
        background: linear-gradient(45deg, #00D4FF, #0066FF);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        margin-top: 1.5rem;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .launch-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 AI Accelerator Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #888; margin-bottom: 3rem;">Choose your preferred version to get started</p>', unsafe_allow_html=True)

# Version selection
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="version-card">
        <h2 class="version-title">🏢 Enterprise Edition</h2>
        <div class="feature-list">
            <p><strong>Classic AI Accelerator Features:</strong></p>
            <ul>
                <li>📊 Change Readiness Dashboard</li>
                <li>🏗️ Architecture Blueprint Generator</li>
                <li>💰 ROI Calculator & Business Case</li>
                <li>🛠️ MLOps Starter Kit</li>
                <li>📈 Enterprise Analytics</li>
                <li>🎯 Industry-Specific Templates</li>
            </ul>
            <p style="margin-top: 1rem;"><strong>Best for:</strong> Traditional ML implementations, enterprise assessments, and ROI calculations</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Launch Enterprise Edition", key="enterprise", use_container_width=True):
        st.switch_page("pages/1_Enterprise_Edition.py")

with col2:
    st.markdown("""
    <div class="version-card">
        <h2 class="version-title">🤖 GenAI Edition</h2>
        <div class="feature-list">
            <p><strong>Advanced GenAI Features:</strong></p>
            <ul>
                <li>🎮 Interactive AI Playground</li>
                <li>📄 Document Q&A System</li>
                <li>📊 Real-time Analytics</li>
                <li>🔧 Multi-Model Support</li>
                <li>💬 Conversation Management</li>
                <li>🚀 GenAI Ops Toolkit</li>
            </ul>
            <p style="margin-top: 1rem;"><strong>Best for:</strong> LLM implementations, prompt engineering, and GenAI operations</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🤖 Launch GenAI Edition", key="genai", use_container_width=True):
        st.switch_page("pages/2_GenAI_Edition.py")

# Comparison section
st.markdown("---")
st.markdown("### 📊 Feature Comparison")

comparison_data = {
    "Feature": [
        "AI Readiness Assessment",
        "Blueprint Generator",
        "ROI Calculator",
        "MLOps Toolkit",
        "Interactive AI Playground",
        "Document Q&A",
        "Multi-Model Support",
        "Token Usage Tracking",
        "Prompt Engineering Tools",
        "Cost Analytics"
    ],
    "Enterprise Edition": ["✅", "✅", "✅", "✅", "❌", "❌", "❌", "❌", "❌", "✅"],
    "GenAI Edition": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"]
}

import pandas as pd
df_comparison = pd.DataFrame(comparison_data)

# Style the dataframe
st.dataframe(
    df_comparison,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Feature": st.column_config.TextColumn("Feature", width=300),
        "Enterprise Edition": st.column_config.TextColumn("Enterprise", width=150),
        "GenAI Edition": st.column_config.TextColumn("GenAI", width=150)
    }
)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>🚀 AI Accelerator Toolkit | Built by Suman Mukherjee | © 2024</p>
    <p>📧 smn.mukherjee@gmail.com | 🌐 www.mukherjeesuman.com</p>
    <p>Choose the right tools for your AI transformation journey</p>
</div>
""", unsafe_allow_html=True)