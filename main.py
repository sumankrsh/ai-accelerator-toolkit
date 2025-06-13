import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import io
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Page configuration
st.set_page_config(
    page_title="AI Accelerator Toolkit | Enterprise AI Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper functions for PDF generation
def generate_mlops_checklist_pdf():
    """Generate MLOps Checklist PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-50, "MLOps Implementation Checklist")
    
    # Content
    y = height - 100
    categories = [
        ("Data Pipeline", [
            "Data versioning system implemented",
            "Automated data quality checks",
            "Feature store established"
        ]),
        ("Model Development", [
            "Experiment tracking system",
            "Model registry configured",
            "Automated hyperparameter tuning"
        ]),
        ("Deployment", [
            "CI/CD pipeline established",
            "A/B testing framework",
            "Model drift detection"
        ])
    ]
    
    c.setFont("Helvetica-Bold", 14)
    for category, items in categories:
        c.drawString(50, y, category)
        y -= 25
        
        c.setFont("Helvetica", 11)
        for item in items:
            c.drawString(70, y, f"□ {item}")
            y -= 20
        y -= 10
    
    c.save()
    buffer.seek(0)
    return buffer

def generate_roi_template_pdf():
    """Generate ROI Template PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-50, "AI ROI Calculation Template")
    
    y = height - 100
    sections = [
        "1. Cost Savings",
        "   - Labor cost reduction: $_______",
        "   - Process automation savings: $_______",
        "",
        "2. Revenue Generation",
        "   - New revenue streams: $_______",
        "   - Customer retention value: $_______",
        "",
        "3. Implementation Costs",
        "   - Initial development: $_______",
        "   - Annual operations: $_______",
        "",
        "4. ROI Calculation",
        "   - Total Benefits: $_______",
        "   - Total Costs: $_______",
        "   - ROI Percentage: _____%"
    ]
    
    c.setFont("Helvetica", 12)
    for line in sections:
        c.drawString(50, y, line)
        y -= 20
    
    c.save()
    buffer.seek(0)
    return buffer

def generate_architecture_pdf(industry, cloud_provider, use_case):
    """Generate Architecture Blueprint PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height-50, f"{industry} AI Architecture Blueprint")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height-75, f"{cloud_provider} | {use_case}")
    
    y = height - 120
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Architecture Components:")
    
    y -= 30
    components = [
        "1. Data Layer",
        f"   - Storage: {cloud_provider} Data Lake",
        "   - Processing: Distributed compute",
        "",
        "2. ML Platform",
        "   - Training: GPU-enabled compute",
        "   - Registry: Model versioning",
        "",
        "3. Serving Layer",
        "   - API Gateway: REST endpoints",
        "   - Monitoring: Real-time metrics",
        "",
        "4. Estimated Cost",
        "   - Development: $5,000-$8,000/month",
        "   - Production: $15,000-$25,000/month"
    ]
    
    c.setFont("Helvetica", 11)
    for line in components:
        c.drawString(50, y, line)
        y -= 18
    
    c.save()
    buffer.seek(0)
    return buffer

# Load data
@st.cache_data
def load_data():
    if os.path.exists('dummy_enterprise_data.csv'):
        df = pd.read_csv('dummy_enterprise_data.csv')
        df['Implementation_Date'] = pd.to_datetime(df['Implementation_Date'])
        return df
    else:
        # Generate sample data if file doesn't exist
        import random
        data = []
        regions = ['US-East', 'US-West', 'EMEA', 'APAC', 'LATAM']
        industries = ['Insurance', 'Healthcare', 'Retail', 'Banking']
        
        for i in range(350):
            data.append({
                'Business_Unit': f'Unit_{i}',
                'Region': random.choice(regions),
                'Industry': random.choice(industries),
                'Cloud_Ready': random.choice([True, False]),
                'Data_Maturity_Score': random.randint(1, 10),
                'ML_Ops_Maturity_Score': random.randint(1, 10),
                'Data_Governance_Score': random.randint(1, 10),
                'Overall_Readiness_Score': round(random.uniform(1, 10), 1),
                'Estimated_AI_ROI_MillionUSD': round(random.uniform(1, 10), 2),
                'Models_In_Production': random.randint(0, 50),
                'Time_To_Market_Days': random.randint(30, 180),
                'AI_Investment_Percentage': random.uniform(5, 25),
                'Cloud_Provider': random.choice(['Azure', 'AWS', 'GCP'])
            })
        return pd.DataFrame(data)

# Initialize session state
if 'generated_blueprint' not in st.session_state:
    st.session_state.generated_blueprint = False

# Load data
df = load_data()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        padding: 2rem 0;
    }
    .sub-header {
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    div[data-testid="metric-container"] {
        background-color: #f0f2f6;
        border: 1px solid #ddd;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🚀 AI Accelerator Toolkit")
    st.markdown("**Version:** 2.0 Enterprise")
    st.markdown("**Last Updated:** " + datetime.now().strftime("%B %Y"))
    
    st.markdown("---")
    
    st.markdown("### 👤 Solution Architect")
    st.markdown("**Suman Mukherjee**")
    st.markdown("Global AI Strategy Lead")
    st.markdown("📧 smn.mukherjee@gmail.com")
    
    st.markdown("---")
    
    st.markdown("### 🎛️ Global Filters")
    
    selected_regions = st.multiselect(
        "Select Regions",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )
    
    selected_industries = st.multiselect(
        "Select Industries",
        options=df['Industry'].unique(),
        default=df['Industry'].unique()[:3]
    )
    
    # Filter data
    filtered_df = df[
        (df['Region'].isin(selected_regions)) &
        (df['Industry'].isin(selected_industries))
    ]
    
    st.markdown("---")
    
    st.markdown("### 📊 Quick Stats")
    st.metric("Total Units", len(filtered_df))
    st.metric("Avg Readiness", f"{filtered_df['Overall_Readiness_Score'].mean():.1f}/10")
    st.metric("Total ROI", f"${filtered_df['Estimated_AI_ROI_MillionUSD'].sum():.1f}M")

# Main content
st.markdown('<h1 class="main-header">🚀 AI Accelerator Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enterprise AI Transformation Platform | $45M+ Proven Impact</p>', unsafe_allow_html=True)

# Top KPI Metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Business Units", len(filtered_df), f"+{int(len(filtered_df)*0.15)}")

with col2:
    avg_roi = filtered_df['Estimated_AI_ROI_MillionUSD'].mean()
    st.metric("Avg ROI", f"${avg_roi:.1f}M", "+23%")

with col3:
    cloud_ready = len(filtered_df[filtered_df['Cloud_Ready']]) / len(filtered_df) * 100
    st.metric("Cloud Ready", f"{cloud_ready:.0f}%", "+12%")

with col4:
    total_models = filtered_df['Models_In_Production'].sum()
    st.metric("Models in Prod", f"{total_models:,}", "+45")

with col5:
    avg_time = filtered_df['Time_To_Market_Days'].mean()
    st.metric("Avg Time to Market", f"{avg_time:.0f}d", "-30d")

st.markdown("---")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Change Readiness",
    "🏗️ Blueprint Generator",
    "💰 ROI Estimator",
    "📚 MLOps Toolkit"
])

with tab1:
    st.header("Enterprise AI Readiness Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Global Readiness Heatmap")
        
        pivot_data = filtered_df.pivot_table(
            values='Overall_Readiness_Score',
            index='Industry',
            columns='Region',
            aggfunc='mean'
        ).round(1)
        
        fig = px.imshow(
            pivot_data,
            labels=dict(x="Region", y="Industry", color="Readiness Score"),
            color_continuous_scale="RdBu",
            title="AI Readiness by Industry and Region"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Maturity Score Distribution")
        
        fig = go.Figure()
        fig.add_trace(go.Box(y=filtered_df['Data_Maturity_Score'], name='Data Maturity'))
        fig.add_trace(go.Box(y=filtered_df['ML_Ops_Maturity_Score'], name='MLOps Maturity'))
        fig.add_trace(go.Box(y=filtered_df['Data_Governance_Score'], name='Governance'))
        
        fig.update_layout(title="Maturity Score Components", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    st.subheader("🔍 Key Insights")
    
    avg_readiness = filtered_df['Overall_Readiness_Score'].mean()
    if avg_readiness < 5:
        st.warning("**Low Readiness**: Focus on foundational capabilities before advanced AI initiatives.")
    elif avg_readiness < 7:
        st.info("**Moderate Readiness**: Ready for targeted AI initiatives with proper planning.")
    else:
        st.success("**High Readiness**: Prepared for enterprise-wide AI transformation.")

with tab2:
    st.header("AI Architecture Blueprint Generator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🛠️ Configuration")
        
        selected_industry = st.selectbox(
            "Industry",
            options=['Insurance', 'Healthcare', 'Retail', 'Banking', 'Manufacturing']
        )
        
        selected_cloud = st.selectbox(
            "Cloud Provider",
            options=['Azure', 'AWS', 'GCP', 'Multi-Cloud']
        )
        
        selected_use_case = st.selectbox(
            "Primary Use Case",
            options=['Customer Intelligence', 'Fraud Detection', 'Demand Forecasting', 
                    'Predictive Maintenance', 'Document Processing']
        )
        
        include_mlops = st.checkbox("Include MLOps Pipeline", value=True)
        include_governance = st.checkbox("Include Data Governance", value=True)
        
        if st.button("🚀 Generate Blueprint", type="primary", use_container_width=True):
            st.session_state.generated_blueprint = True
    
    with col2:
        st.subheader("📐 Generated Architecture")
        
        if st.session_state.generated_blueprint:
            st.markdown(f"### {selected_cloud} Reference Architecture for {selected_industry}")
            st.markdown(f"**Use Case:** {selected_use_case}")
            
            # Architecture visualization
            st.markdown("#### Architecture Layers:")
            
            components = {
                "Data Sources": ["Operational Systems", "External APIs", "IoT Devices", "Third-party Data"],
                "Ingestion": ["Event Streaming", "Batch ETL", "Change Data Capture", "API Gateway"],
                "Storage": ["Data Lake", "Data Warehouse", "Feature Store", "Object Storage"],
                "Processing": ["Stream Processing", "Batch Processing", "ML Pipeline", "Data Quality"],
                "ML Platform": ["Model Training", "Model Registry", "Experiment Tracking", "Model Serving"],
                "Serving": ["REST APIs", "GraphQL", "gRPC", "Edge Deployment"]
            }
            
            for layer, items in components.items():
                st.markdown(f"**{layer}:** {', '.join(items)}")
            
            # Cost estimate
            st.markdown("#### 💰 Cost Estimate")
            st.info(f"""
            - **Development Environment:** $5,000 - $8,000/month
            - **Production Environment:** $15,000 - $25,000/month
            - **Total Annual Estimate:** $240,000 - $396,000
            """)
            
            # Generate PDF
            blueprint_pdf = generate_architecture_pdf(selected_industry, selected_cloud, selected_use_case)
            
            st.download_button(
                label="📥 Download Architecture Blueprint (PDF)",
                data=blueprint_pdf,
                file_name=f"{selected_industry}_{selected_cloud}_Architecture.pdf",
                mime="application/pdf",
                type="primary"
            )
            
            st.success("✅ Blueprint generated successfully!")
        else:
            st.info("👈 Configure your requirements and click 'Generate Blueprint'")

with tab3:
    st.header("ROI Estimation & Business Case Builder")
    
    # ROI Calculator
    st.subheader("🧮 Custom ROI Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📊 Business Metrics")
        annual_revenue = st.number_input("Annual Revenue ($M)", min_value=10.0, value=500.0)
        num_employees = st.number_input("Number of Employees", min_value=100, value=5000)
        current_efficiency = st.slider("Current Efficiency (%)", 30, 90, 60)
    
    with col2:
        st.markdown("#### 🎯 AI Impact")
        efficiency_gain = st.slider("Expected Efficiency Gain (%)", 5, 50, 25)
        revenue_uplift = st.slider("Revenue Uplift (%)", 0, 30, 10)
        cost_reduction = st.slider("Cost Reduction (%)", 5, 40, 20)
    
    with col3:
        st.markdown("#### 💰 Investment")
        implementation_cost = st.number_input("Implementation Cost ($K)", min_value=100, value=1000)
        annual_operating_cost = st.number_input("Annual Operating Cost ($K)", min_value=50, value=300)
        implementation_time = st.slider("Implementation Time (months)", 3, 24, 9)
    
    if st.button("💵 Calculate ROI", type="primary", use_container_width=True):
        # ROI Calculations
        revenue_benefit = annual_revenue * (revenue_uplift / 100) * 1000000
        cost_savings = (annual_revenue * 0.7) * (cost_reduction / 100) * 1000000
        total_annual_benefit = revenue_benefit + cost_savings
        
        total_3year_benefit = total_annual_benefit * 2.3  # Accounting for ramp-up
        total_3year_cost = (implementation_cost * 1000) + (annual_operating_cost * 1000 * 3)
        net_benefit = total_3year_benefit - total_3year_cost
        roi_percentage = (net_benefit / total_3year_cost) * 100
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 ROI Analysis Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("3-Year Net Benefit", f"${net_benefit/1000000:.1f}M")
        with col2:
            st.metric("Annual Benefit", f"${total_annual_benefit/1000000:.1f}M")
        with col3:
            st.metric("ROI Percentage", f"{roi_percentage:.0f}%")
        with col4:
            st.metric("Payback Period", f"{int(total_3year_cost/total_annual_benefit*12)} months")
        
        st.success(f"✅ {'Proceed with implementation' if roi_percentage > 100 else 'Review parameters'}")
    
    # Download ROI template
    st.markdown("---")
    roi_template = generate_roi_template_pdf()
    st.download_button(
        label="📥 Download ROI Template (PDF)",
        data=roi_template,
        file_name="AI_ROI_Template.pdf",
        mime="application/pdf"
    )

with tab4:
    st.header("MLOps Starter Kit & Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🚀 Quick Start")
        st.code("""
ai-project/
├── data/
├── models/
├── src/
├── tests/
├── configs/
└── docs/
        """, language='text')
    
    with col2:
        st.markdown("### 📋 Best Practices")
        st.markdown("""
        - ✅ Version Control
        - ✅ Automated Testing
        - ✅ Model Registry
        - ✅ Monitoring
        - ✅ Documentation
        """)
    
    with col3:
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        - **Orchestration:** Airflow
        - **Tracking:** MLflow
        - **Registry:** MLflow
        - **Monitoring:** Evidently
        - **Feature Store:** Feast
        """)
    
    # Downloadable resources
    st.markdown("---")
    st.markdown("### 📥 Downloadable Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mlops_checklist = generate_mlops_checklist_pdf()
        st.download_button(
            label="📋 MLOps Checklist (PDF)",
            data=mlops_checklist,
            file_name="MLOps_Checklist.pdf",
            mime="application/pdf"
        )
    
    with col2:
        st.button("🏗️ Architecture Templates", disabled=True, help="Coming soon")
    
    with col3:
        st.button("📚 Best Practices Guide", disabled=True, help="Coming soon")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>🚀 AI Accelerator Toolkit v2.0 | Built by Suman Mukherjee | © 2024</p>
</div>
""", unsafe_allow_html=True)