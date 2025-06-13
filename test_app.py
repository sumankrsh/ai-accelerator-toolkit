import streamlit as st

st.set_page_config(page_title="Test App", layout="wide")

st.title("🚀 AI Accelerator Toolkit Test")
st.write("If you can see this, Streamlit is working!")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Test Metric 1", "100", "+10")
with col2:
    st.metric("Test Metric 2", "$5M", "+23%")
with col3:
    st.metric("Test Metric 3", "72%", "+12%")

if st.button("Test Button"):
    st.success("✅ Button works!")
    
st.info("Try accessing the main app at http://localhost:8502")