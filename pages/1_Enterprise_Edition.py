import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import io
import base64

# Page configuration
st.set_page_config(
    page_title="AI Accelerator Toolkit | Enterprise AI Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper functions for PDF generation
def generate_pdf_download_link(content, filename, link_text):
    """Generate a download link for text content as PDF"""
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

# Initialize session state
if 'generated_blueprint' not in st.session_state:
    st.session_state.generated_blueprint = False

# Load data with error handling
@st.cache_data
def load_data():
    try:
        if os.path.exists('dummy_enterprise_data.csv'):
            df = pd.read_csv('dummy_enterprise_data.csv')
            df['Implementation_Date'] = pd.to_datetime(df['Implementation_Date'])
            return df
    except Exception as e:
        st.warning(f"Could not load data file: {e}")
    
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
            'Cloud_Provider': random.choice(['Azure', 'AWS', 'GCP']),
            'Implementation_Date': pd.Timestamp('2023-01-01') + pd.Timedelta(days=random.randint(0, 365))
        })
    return pd.DataFrame(data)

# Load data
df = load_data()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 1rem;
    }
    .download-button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        text-decoration: none;
        border-radius: 5px;
        display: inline-block;
        margin: 0.5rem 0;
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
        options=df['Region'].unique() if not df.empty else [],
        default=df['Region'].unique() if not df.empty else []
    )
    
    selected_industries = st.multiselect(
        "Select Industries",
        options=df['Industry'].unique() if not df.empty else [],
        default=df['Industry'].unique()[:3] if not df.empty else []
    )
    
    # Filter data
    if selected_regions and selected_industries:
        filtered_df = df[
            (df['Region'].isin(selected_regions)) &
            (df['Industry'].isin(selected_industries))
        ]
    else:
        filtered_df = df
    
    st.markdown("---")
    
    st.markdown("### 📊 Quick Stats")
    if not filtered_df.empty:
        st.metric("Total Units", len(filtered_df))
        st.metric("Avg Readiness", f"{filtered_df['Overall_Readiness_Score'].mean():.1f}/10")
        st.metric("Total ROI", f"${filtered_df['Estimated_AI_ROI_MillionUSD'].sum():.1f}M")

# Main content
st.markdown('<h1 class="main-header">🚀 AI Accelerator Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enterprise AI Transformation Platform | $45M+ Proven Impact</p>', unsafe_allow_html=True)

# Error handling for empty dataframe
if filtered_df.empty:
    st.warning("No data available. Using sample data for demonstration.")
    filtered_df = df

# Top KPI Metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Business Units", len(filtered_df), f"+{int(len(filtered_df)*0.15)}")

with col2:
    avg_roi = filtered_df['Estimated_AI_ROI_MillionUSD'].mean() if not filtered_df.empty else 5.5
    st.metric("Avg ROI", f"${avg_roi:.1f}M", "+23%")

with col3:
    cloud_ready_pct = (len(filtered_df[filtered_df['Cloud_Ready']]) / len(filtered_df) * 100) if not filtered_df.empty else 72
    st.metric("Cloud Ready", f"{cloud_ready_pct:.0f}%", "+12%")

with col4:
    total_models = filtered_df['Models_In_Production'].sum() if not filtered_df.empty else 3247
    st.metric("Models in Prod", f"{total_models:,}", "+45")

with col5:
    avg_time = filtered_df['Time_To_Market_Days'].mean() if not filtered_df.empty else 90
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
    
    if not filtered_df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌍 Global Readiness Heatmap")
            
            try:
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
            except:
                st.info("Insufficient data for heatmap visualization")
        
        with col2:
            st.subheader("📈 Maturity Score Distribution")
            
            try:
                fig = go.Figure()
                fig.add_trace(go.Box(y=filtered_df['Data_Maturity_Score'], name='Data Maturity'))
                fig.add_trace(go.Box(y=filtered_df['ML_Ops_Maturity_Score'], name='MLOps Maturity'))
                fig.add_trace(go.Box(y=filtered_df['Data_Governance_Score'], name='Governance'))
                
                fig.update_layout(title="Maturity Score Components", showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.info("Unable to display maturity scores")
        
        # Key insights
        st.subheader("🔍 Key Insights")
        
        avg_readiness = filtered_df['Overall_Readiness_Score'].mean()
        if avg_readiness < 5:
            st.warning("**Low Readiness**: Focus on foundational capabilities before advanced AI initiatives.")
        elif avg_readiness < 7:
            st.info("**Moderate Readiness**: Ready for targeted AI initiatives with proper planning.")
        else:
            st.success("**High Readiness**: Prepared for enterprise-wide AI transformation.")
    else:
        st.info("No data available for visualization")

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
            
            # Generate blueprint content
            blueprint_content = f"""
{selected_industry} AI Architecture Blueprint
==========================================

Cloud Provider: {selected_cloud}
Use Case: {selected_use_case}

Architecture Components:
-----------------------
1. Data Layer
   - Storage: {selected_cloud} Data Lake
   - Processing: Distributed compute
   - Governance: Data catalog and lineage

2. ML Platform
   - Training: GPU-enabled compute
   - Registry: Model versioning
   - Monitoring: Drift detection

3. Serving Layer
   - API Gateway: REST endpoints
   - Monitoring: Real-time metrics
   - Scaling: Auto-scaling enabled

Cost Estimate:
--------------
- Development: $5,000-$8,000/month
- Production: $15,000-$25,000/month
- Annual Total: $240,000-$396,000

Generated by AI Accelerator Toolkit
© 2024 Suman Mukherjee
            """
            
            # Download button
            st.download_button(
                label="📥 Download Architecture Blueprint (TXT)",
                data=blueprint_content,
                file_name=f"{selected_industry}_{selected_cloud}_Architecture.txt",
                mime="text/plain"
            )
            
            st.success("✅ Blueprint generated successfully!")
        else:
            st.info("👈 Configure your requirements and click 'Generate Blueprint'")

with tab3:
    st.header("ROI Estimation & Business Case Builder")
    
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
        roi_percentage = (net_benefit / total_3year_cost) * 100 if total_3year_cost > 0 else 0
        
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
            payback = int(total_3year_cost/total_annual_benefit*12) if total_annual_benefit > 0 else 999
            st.metric("Payback Period", f"{payback} months")
        
        if roi_percentage > 100:
            st.success("✅ Strong business case - Proceed with implementation")
        else:
            st.warning("⚠️ Review parameters for better ROI")
    
    # ROI Template
    roi_template = """
AI ROI Calculation Template
==========================

1. Cost Savings
   - Labor cost reduction: $_______
   - Process automation savings: $_______
   - Error reduction value: $_______

2. Revenue Generation
   - New revenue streams: $_______
   - Customer retention value: $_______
   - Market expansion: $_______

3. Implementation Costs
   - Initial development: $_______
   - Annual operations: $_______
   - Training costs: $_______

4. ROI Calculation
   - Total Benefits: $_______
   - Total Costs: $_______
   - ROI Percentage: _____%
   - Payback Period: _____ months

Generated by AI Accelerator Toolkit
    """
    
    st.download_button(
        label="📥 Download ROI Template (TXT)",
        data=roi_template,
        file_name="AI_ROI_Template.txt",
        mime="text/plain"
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
        - ✅ Security First
        """)
    
    with col3:
        st.markdown("### 🛠️ Tech Stack")
        st.markdown("""
        - **Orchestration:** Airflow
        - **Tracking:** MLflow
        - **Registry:** MLflow
        - **Monitoring:** Evidently
        - **Feature Store:** Feast
        - **Validation:** Great Expectations
        """)
    
    # MLOps Checklist
    mlops_checklist = """
MLOps Implementation Checklist
==============================

Data Pipeline:
□ Data versioning system implemented
□ Automated data quality checks
□ Feature store established
□ Data lineage tracking

Model Development:
□ Experiment tracking system
□ Model registry configured
□ Automated hyperparameter tuning
□ Version control for code

Deployment:
□ CI/CD pipeline established
□ A/B testing framework
□ Model drift detection
□ Rollback procedures

Governance:
□ Model documentation
□ Approval workflows
□ Audit trails
□ Compliance checks

Generated by AI Accelerator Toolkit
© 2024 Suman Mukherjee
    """
    
    st.download_button(
        label="📋 Download MLOps Checklist (TXT)",
        data=mlops_checklist,
        file_name="MLOps_Checklist.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>🚀 AI Accelerator Toolkit v2.0 | Built by Suman Mukherjee | © 2024</p>
    <p>📧 smn.mukherjee@gmail.com | 🌐 www.mukherjeesuman.com</p>
</div>
""", unsafe_allow_html=True)