import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Page config
st.set_page_config(
    page_title="AI Accelerator Toolkit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dummy_enterprise_data.csv')
        return df
    except:
        # Generate dummy data if file doesn't exist
        import random
        data = []
        regions = ['US-East', 'US-West', 'EMEA', 'APAC', 'LATAM']
        industries = ['Insurance', 'Healthcare', 'Retail', 'Banking']
        
        for i in range(100):
            data.append({
                'Business_Unit': f'Unit_{i}',
                'Region': random.choice(regions),
                'Industry': random.choice(industries),
                'Cloud_Ready': random.choice([True, False]),
                'Data_Maturity_Score': random.randint(1, 10),
                'ML_Ops_Maturity_Score': random.randint(1, 10),
                'Data_Governance_Score': random.randint(1, 10),
                'Overall_Readiness_Score': random.randint(1, 10),
                'Estimated_AI_ROI_MillionUSD': round(random.uniform(1, 10), 2),
                'Models_In_Production': random.randint(0, 50),
                'Time_To_Market_Days': random.randint(30, 180)
            })
        return pd.DataFrame(data)

# Generate simple PDF
def generate_simple_pdf(title, content):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, title)
    
    # Content
    c.setFont("Helvetica", 12)
    y = height - 100
    for line in content.split('\n'):
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 20
    
    c.save()
    buffer.seek(0)
    return buffer

# Initialize data
df = load_data()

# Sidebar
with st.sidebar:
    st.markdown("### 🚀 AI Accelerator Toolkit")
    st.markdown("**Version:** 2.0")
    st.markdown("---")
    st.markdown("**Architect:** Suman Mukherjee")
    st.markdown("**Email:** smn.mukherjee@gmail.com")
    st.markdown("---")
    
    # Filters
    selected_regions = st.multiselect(
        "Select Regions",
        options=df['Region'].unique() if 'Region' in df.columns else [],
        default=df['Region'].unique() if 'Region' in df.columns else []
    )
    
    if selected_regions:
        filtered_df = df[df['Region'].isin(selected_regions)]
    else:
        filtered_df = df

# Main content
st.markdown('<h1 class="main-header">🚀 AI Accelerator Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Enterprise AI Transformation Platform | $45M+ Proven Impact</p>', unsafe_allow_html=True)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Business Units", len(filtered_df), "+15%")

with col2:
    avg_roi = filtered_df['Estimated_AI_ROI_MillionUSD'].mean() if 'Estimated_AI_ROI_MillionUSD' in filtered_df.columns else 5.5
    st.metric("Avg ROI", f"${avg_roi:.1f}M", "+23%")

with col3:
    cloud_ready = len(filtered_df[filtered_df['Cloud_Ready']]) if 'Cloud_Ready' in filtered_df.columns else 72
    st.metric("Cloud Ready", f"{cloud_ready}%", "+12%")

with col4:
    models = filtered_df['Models_In_Production'].sum() if 'Models_In_Production' in filtered_df.columns else 3247
    st.metric("Models in Production", f"{models:,}", "+45")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Change Readiness", "🏗️ Blueprint Generator", "💰 ROI Estimator", "📚 MLOps Toolkit"])

with tab1:
    st.header("Change Readiness Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Readiness by Region")
        if not filtered_df.empty and 'Overall_Readiness_Score' in filtered_df.columns:
            fig = px.bar(
                filtered_df.groupby('Region')['Overall_Readiness_Score'].mean().reset_index(),
                x='Region',
                y='Overall_Readiness_Score',
                title='Average Readiness Score by Region'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available")
    
    with col2:
        st.subheader("Maturity Distribution")
        if not filtered_df.empty and 'Data_Maturity_Score' in filtered_df.columns:
            fig = px.box(
                filtered_df,
                y=['Data_Maturity_Score', 'ML_Ops_Maturity_Score', 'Data_Governance_Score'],
                title='Maturity Score Distribution'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available")

with tab2:
    st.header("Blueprint Generator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Configuration")
        
        industry = st.selectbox("Industry", ["Insurance", "Healthcare", "Retail", "Banking"])
        cloud = st.selectbox("Cloud Provider", ["Azure", "AWS", "GCP", "Multi-Cloud"])
        use_case = st.selectbox("Use Case", ["Customer Intelligence", "Fraud Detection", "Demand Forecasting"])
        
        if st.button("🚀 Generate Blueprint", type="primary"):
            st.session_state['blueprint_generated'] = True
    
    with col2:
        st.subheader("Generated Architecture")
        
        if st.session_state.get('blueprint_generated', False):
            st.success("✅ Blueprint generated successfully!")
            
            st.markdown(f"### {cloud} Architecture for {industry}")
            st.markdown(f"**Use Case:** {use_case}")
            
            # Simple architecture visualization
            st.markdown("""
            ```
            Data Sources → Ingestion → Storage → Processing → ML Platform → Serving
            ```
            """)
            
            # Generate PDF
            pdf_content = f"""
{cloud} Architecture Blueprint
Industry: {industry}
Use Case: {use_case}

Architecture Components:
1. Data Sources
2. Ingestion Layer
3. Storage Layer
4. Processing Layer
5. ML Platform
6. Serving Layer

Estimated Cost: $15,000 - $25,000/month
            """
            
            pdf_buffer = generate_simple_pdf(f"{industry} Architecture Blueprint", pdf_content)
            
            st.download_button(
                label="📥 Download Blueprint (PDF)",
                data=pdf_buffer,
                file_name=f"{industry}_{cloud}_Blueprint.pdf",
                mime="application/pdf"
            )
        else:
            st.info("👈 Configure and click 'Generate Blueprint'")

with tab3:
    st.header("ROI Estimator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        revenue = st.number_input("Annual Revenue ($M)", value=500.0)
        employees = st.number_input("Number of Employees", value=5000)
    
    with col2:
        efficiency_gain = st.slider("Efficiency Gain (%)", 5, 50, 25)
        revenue_uplift = st.slider("Revenue Uplift (%)", 0, 30, 10)
    
    with col3:
        implementation_cost = st.number_input("Implementation Cost ($K)", value=1000)
        operating_cost = st.number_input("Annual Operating Cost ($K)", value=300)
    
    if st.button("Calculate ROI", type="primary"):
        # Simple ROI calculation
        annual_benefit = (revenue * revenue_uplift / 100 + revenue * 0.7 * efficiency_gain / 100) * 1000000
        total_cost = implementation_cost * 1000 + operating_cost * 1000 * 3
        net_benefit = annual_benefit * 3 - total_cost
        roi = (net_benefit / total_cost) * 100
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("3-Year Net Benefit", f"${net_benefit/1000000:.1f}M")
        with col2:
            st.metric("ROI Percentage", f"{roi:.0f}%")
        with col3:
            st.metric("Payback Period", f"{int(total_cost/annual_benefit*12)} months")
        
        st.success("✅ ROI calculation complete!")

with tab4:
    st.header("MLOps Starter Kit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project Structure")
        st.code("""
ai-project/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
└── configs/
        """)
    
    with col2:
        st.subheader("Best Practices")
        st.markdown("""
        - ✅ Version control everything
        - ✅ Automated testing
        - ✅ Model monitoring
        - ✅ Documentation
        - ✅ Security first
        """)
    
    # Download buttons
    st.markdown("### 📥 Downloads")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        checklist_pdf = generate_simple_pdf(
            "MLOps Checklist",
            "MLOps Implementation Checklist\n\n" +
            "□ Data versioning\n□ Model registry\n□ CI/CD pipeline\n□ Monitoring\n□ Documentation"
        )
        st.download_button(
            "📋 MLOps Checklist",
            data=checklist_pdf,
            file_name="MLOps_Checklist.pdf",
            mime="application/pdf"
        )
    
    with col2:
        roi_pdf = generate_simple_pdf(
            "ROI Template",
            "AI ROI Calculation Template\n\n" +
            "1. Cost Savings: $____\n2. Revenue Increase: $____\n3. Implementation Cost: $____\n4. ROI: ____%"
        )
        st.download_button(
            "💰 ROI Template",
            data=roi_pdf,
            file_name="ROI_Template.pdf",
            mime="application/pdf"
        )
    
    with col3:
        st.button("🏗️ Architecture Templates", disabled=True, help="Coming soon")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>AI Accelerator Toolkit v2.0 | Built by Suman Mukherjee | smn.mukherjee@gmail.com</p>
</div>
""", unsafe_allow_html=True)