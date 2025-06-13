import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from leadership_case_study import show_leadership_page, get_case_study_content

st.set_page_config(
    page_title="Global AI-Accelerator Toolkit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #1E88E5 0%, #1565C0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 2rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E88E5;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dummy_enterprise_data.csv')
    df['Implementation_Date'] = pd.to_datetime(df['Implementation_Date'])
    return df

df = load_data()

# Sidebar for filters and branding
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/1E88E5/FFFFFF?text=AI+Accelerator", width=300)
    st.markdown("### 🎯 Enterprise AI Transformation Suite")
    st.markdown("**Version:** 2.0")
    st.markdown("**Last Updated:** " + datetime.now().strftime("%B %Y"))
    
    st.markdown("---")
    st.markdown("### 🏢 Leadership")
    st.markdown("**Solution Architect:** Suman Mukherjee")
    st.markdown("**Role:** Global AI Strategy Lead")
    st.markdown("**Impact:** $45M+ ROI | 350+ Business Units")
    st.markdown("**Contact:** smn.mukherjee@gmail.com")
    
    if st.button("📄 View Leadership Impact", use_container_width=True):
        show_leadership_page()
    
    st.markdown("---")
    st.markdown("### 📊 Global Filters")
    
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
    
    maturity_threshold = st.slider(
        "Minimum Maturity Score",
        min_value=1,
        max_value=10,
        value=5
    )
    
    # Filter data
    filtered_df = df[
        (df['Region'].isin(selected_regions)) &
        (df['Industry'].isin(selected_industries)) &
        (df['Overall_Readiness_Score'] >= maturity_threshold)
    ]
    
    st.markdown("---")
    st.markdown("### 📥 Downloads")
    
    case_study = get_case_study_content()
    leadership_content = f"""
LEADERSHIP IMPACT SUMMARY
========================

Role: Global AI Strategy Lead & Solution Architect
Impact: Led enterprise-wide AI transformation

KEY ACHIEVEMENTS:
• $45M+ in realized ROI (Year 1)
• 350+ business units transformed
• 150+ ML models in production
• 40% improvement in time-to-market
• 500+ employees trained

TECHNICAL LEADERSHIP:
• Designed multi-cloud AI platform
• Implemented enterprise MLOps framework
• Built real-time ML serving (10M+ predictions/day)
• Created reusable AI accelerators

BUSINESS TRANSFORMATION:
• Customer Intelligence: $12M retained revenue
• Risk & Compliance: $8M fraud prevented
• Operations: 30% inventory cost reduction

Technologies: {', '.join(case_study['technologies'][:6])}
    """
    
    st.download_button(
        label="📄 Leadership One-Pager",
        data=leadership_content,
        file_name="leadership_impact_summary.txt",
        mime="text/plain"
    )

# Main content
st.markdown('<h1 class="main-header">🚀 Global AI-Accelerator Toolkit</h1>', unsafe_allow_html=True)

# KPI metrics at the top
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_units = len(filtered_df)
    st.metric("Business Units", total_units, f"+{int(total_units*0.15)} QoQ")
with col2:
    avg_roi = filtered_df['Estimated_AI_ROI_MillionUSD'].mean()
    st.metric("Avg ROI", f"${avg_roi:.1f}M", "+23%")
with col3:
    ready_units = len(filtered_df[filtered_df['Cloud_Ready']])
    st.metric("Cloud Ready", f"{ready_units/total_units*100:.0f}%", "+12%")
with col4:
    total_models = filtered_df['Models_In_Production'].sum()
    st.metric("Models in Production", total_models, "+45")

st.markdown("---")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Change Readiness Dashboard",
    "🏗️ Blueprint Generator",
    "💰 ROI Estimator",
    "📚 MLOps Starter Kit"
])

with tab1:
    st.header("Enterprise AI Readiness Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Readiness heatmap
        st.subheader("🎯 Regional Readiness Heatmap")
        pivot_data = filtered_df.pivot_table(
            values='Overall_Readiness_Score',
            index='Industry',
            columns='Region',
            aggfunc='mean'
        )
        
        fig = px.imshow(
            pivot_data,
            labels=dict(x="Region", y="Industry", color="Readiness Score"),
            color_continuous_scale="RdYlBu",
            aspect="auto"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Maturity distribution
        st.subheader("📈 Maturity Score Distribution")
        fig = go.Figure()
        fig.add_trace(go.Box(y=filtered_df['Data_Maturity_Score'], name='Data Maturity'))
        fig.add_trace(go.Box(y=filtered_df['ML_Ops_Maturity_Score'], name='MLOps Maturity'))
        fig.add_trace(go.Box(y=filtered_df['Data_Governance_Score'], name='Data Governance'))
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed metrics
    st.subheader("🔍 Detailed Readiness Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Cloud provider distribution
        cloud_dist = filtered_df['Cloud_Provider'].value_counts()
        fig = px.pie(
            values=cloud_dist.values,
            names=cloud_dist.index,
            title="Cloud Provider Distribution",
            hole=0.4
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Time to market analysis
        fig = px.histogram(
            filtered_df,
            x='Time_To_Market_Days',
            nbins=20,
            title="Time to Market Distribution"
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # AI investment vs budget
        fig = px.scatter(
            filtered_df,
            x='Annual_IT_Budget_Million',
            y='AI_Investment_Percentage',
            size='Estimated_AI_ROI_MillionUSD',
            color='Industry',
            title="AI Investment Analysis"
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("AI Architecture Blueprint Generator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🔧 Configuration")
        
        selected_industry = st.selectbox(
            "Select Industry",
            options=filtered_df['Industry'].unique()
        )
        
        selected_cloud = st.selectbox(
            "Cloud Provider",
            options=['Azure', 'AWS', 'GCP', 'Multi-Cloud']
        )
        
        selected_use_case = st.selectbox(
            "Primary Use Case",
            options=filtered_df['Primary_AI_Use_Case'].unique()
        )
        
        architecture_type = st.radio(
            "Architecture Pattern",
            options=['Batch Processing', 'Real-time Streaming', 'Hybrid']
        )
        
        include_mlops = st.checkbox("Include MLOps Pipeline", value=True)
        include_governance = st.checkbox("Include Data Governance", value=True)
        
        generate_button = st.button("🚀 Generate Blueprint", type="primary")
    
    with col2:
        st.subheader("📐 Generated Architecture")
        
        if generate_button:
            # Dynamic architecture based on selections
            if selected_cloud == "Azure":
                st.markdown(f"### Azure Reference Architecture for {selected_industry}")
                st.markdown(f"**Use Case:** {selected_use_case}")
                st.markdown(f"**Pattern:** {architecture_type}")
                
                # Mermaid diagram
                mermaid_code = """
                graph TB
                    subgraph "Data Sources"
                        A[On-premise Systems]
                        B[Cloud Applications]
                        C[IoT Devices]
                    end
                    
                    subgraph "Ingestion Layer"
                        D[Azure Data Factory]
                        E[Event Hubs]
                    end
                    
                    subgraph "Storage Layer"
                        F[Data Lake Gen2]
                        G[Cosmos DB]
                    end
                    
                    subgraph "Processing Layer"
                        H[Databricks]
                        I[Synapse Analytics]
                    end
                    
                    subgraph "ML Platform"
                        J[Azure ML]
                        K[Model Registry]
                    end
                    
                    subgraph "Serving Layer"
                        L[API Management]
                        M[Container Instances]
                    end
                    
                    A --> D
                    B --> D
                    C --> E
                    D --> F
                    E --> F
                    F --> H
                    F --> I
                    H --> J
                    I --> J
                    J --> K
                    K --> L
                    K --> M
                """
                
                if include_mlops:
                    mermaid_code += """
                    
                    subgraph "MLOps Pipeline"
                        N[Azure DevOps]
                        O[Model Monitoring]
                    end
                    
                    J --> N
                    M --> O
                    O --> J
                """
                
                if include_governance:
                    mermaid_code += """
                    
                    subgraph "Governance"
                        P[Purview]
                        Q[Key Vault]
                    end
                    
                    F --> P
                    Q --> L
                """
                
                st.code(mermaid_code, language='mermaid')
                
                # Technical specifications
                st.markdown("### 📋 Technical Specifications")
                
                specs = {
                    "Data Ingestion": "Azure Data Factory with 15-min batch intervals",
                    "Storage": "ADLS Gen2 with hierarchical namespace",
                    "Compute": "Databricks with auto-scaling (4-16 nodes)",
                    "ML Framework": "MLflow on Azure ML",
                    "Deployment": "AKS with GPU nodes for inference",
                    "Monitoring": "Application Insights + Custom dashboards",
                    "Security": "Private endpoints, managed identities",
                    "Estimated Cost": "$15,000 - $25,000/month"
                }
                
                for key, value in specs.items():
                    st.markdown(f"**{key}:** {value}")
        else:
            st.info("👆 Configure your requirements and click 'Generate Blueprint' to create a custom architecture")

with tab3:
    st.header("ROI Estimation & Business Case Builder")
    
    # ROI Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 ROI by Region")
        roi_by_region = filtered_df.groupby('Region').agg({
            'Estimated_AI_ROI_MillionUSD': 'sum',
            'Annual_IT_Budget_Million': 'sum'
        }).reset_index()
        roi_by_region['ROI_Percentage'] = (
            roi_by_region['Estimated_AI_ROI_MillionUSD'] / 
            roi_by_region['Annual_IT_Budget_Million'] * 100
        )
        
        fig = px.bar(
            roi_by_region,
            x='Region',
            y='Estimated_AI_ROI_MillionUSD',
            text='Estimated_AI_ROI_MillionUSD',
            title='Total AI ROI by Region (Million USD)'
        )
        fig.update_traces(texttemplate='$%{text:.1f}M', textposition='outside')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 ROI by Industry")
        roi_by_industry = filtered_df.groupby('Industry')['Estimated_AI_ROI_MillionUSD'].mean().reset_index()
        roi_by_industry = roi_by_industry.sort_values('Estimated_AI_ROI_MillionUSD', ascending=True)
        
        fig = px.bar(
            roi_by_industry,
            x='Estimated_AI_ROI_MillionUSD',
            y='Industry',
            orientation='h',
            text='Estimated_AI_ROI_MillionUSD',
            title='Average AI ROI by Industry (Million USD)'
        )
        fig.update_traces(texttemplate='$%{text:.1f}M', textposition='outside')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # ROI Calculator
    st.markdown("---")
    st.subheader("🧮 Custom ROI Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Input Parameters**")
        team_size = st.number_input("Team Size", min_value=5, max_value=500, value=50)
        current_productivity = st.slider("Current Productivity (%)", 0, 100, 60)
        ai_productivity_gain = st.slider("Expected AI Productivity Gain (%)", 0, 50, 25)
        avg_salary = st.number_input("Average Annual Salary ($)", min_value=50000, max_value=300000, value=120000)
    
    with col2:
        st.markdown("**Cost Parameters**")
        implementation_cost = st.number_input("Implementation Cost ($)", min_value=50000, max_value=5000000, value=500000)
        annual_operating_cost = st.number_input("Annual Operating Cost ($)", min_value=10000, max_value=1000000, value=150000)
        implementation_months = st.slider("Implementation Timeline (months)", 3, 24, 9)
    
    with col3:
        st.markdown("**Calculated ROI**")
        
        # Calculate ROI
        productivity_value = (team_size * avg_salary * (ai_productivity_gain / 100))
        annual_benefit = productivity_value - annual_operating_cost
        total_3year_benefit = (annual_benefit * 3) - implementation_cost
        roi_percentage = (total_3year_benefit / implementation_cost) * 100
        payback_months = implementation_cost / (annual_benefit / 12) if annual_benefit > 0 else 0
        
        st.metric("Annual Benefit", f"${annual_benefit:,.0f}")
        st.metric("3-Year Net Benefit", f"${total_3year_benefit:,.0f}")
        st.metric("ROI Percentage", f"{roi_percentage:.1f}%")
        st.metric("Payback Period", f"{payback_months:.1f} months")
    
    # Business case summary
    st.markdown("---")
    st.subheader("📋 Executive Summary")
    
    st.info(f"""
    **Business Case for AI Implementation**
    
    Based on the analysis of {len(filtered_df)} business units across {len(selected_regions)} regions:
    
    • **Total Potential ROI:** ${filtered_df['Estimated_AI_ROI_MillionUSD'].sum():.1f}M
    • **Average Time to Market:** {filtered_df['Time_To_Market_Days'].mean():.0f} days
    • **Cloud-Ready Units:** {len(filtered_df[filtered_df['Cloud_Ready']]) / len(filtered_df) * 100:.0f}%
    • **High-Maturity Units (>7):** {len(filtered_df[filtered_df['Overall_Readiness_Score'] > 7]) / len(filtered_df) * 100:.0f}%
    
    **Recommended Next Steps:**
    1. Prioritize high-maturity units for immediate AI implementation
    2. Establish Center of Excellence for knowledge sharing
    3. Standardize on {filtered_df['Cloud_Provider'].mode()[0]} as primary cloud platform
    4. Focus on {filtered_df['Primary_AI_Use_Case'].mode()[0]} as initial use case
    """)

with tab4:
    st.header("MLOps Starter Kit & Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 Quick Start Templates")
        
        st.markdown("### 1. Project Structure Template")
        st.code("""
        ai-project/
        ├── data/
        │   ├── raw/
        │   ├── processed/
        │   └── external/
        ├── models/
        │   ├── experiments/
        │   └── production/
        ├── notebooks/
        │   ├── exploratory/
        │   └── reports/
        ├── src/
        │   ├── data/
        │   ├── features/
        │   ├── models/
        │   └── visualization/
        ├── tests/
        ├── configs/
        ├── requirements.txt
        └── README.md
        """, language='text')
        
        st.markdown("### 2. MLOps Pipeline Template")
        st.code("""
        # Azure DevOps Pipeline
        trigger:
          branches:
            include:
            - main
            - develop
        
        stages:
        - stage: Build
          jobs:
          - job: TestAndBuild
            steps:
            - task: Python@3
              inputs:
                command: 'test'
            - task: Docker@2
              inputs:
                command: 'build'
        
        - stage: Deploy
          jobs:
          - deployment: DeployModel
            environment: 'production'
            strategy:
              runOnce:
                deploy:
                  steps:
                  - task: AzureML@1
                    inputs:
                      modelName: '$(Build.DefinitionName)'
                      modelVersion: '$(Build.BuildId)'
        """, language='yaml')
    
    with col2:
        st.subheader("📚 Best Practices & Guidelines")
        
        with st.expander("✅ Data Engineering Best Practices"):
            st.markdown("""
            - **Data Versioning:** Use DVC or Delta Lake for data versioning
            - **Data Quality:** Implement Great Expectations for data validation
            - **Feature Store:** Centralize feature engineering with Feast or Databricks Feature Store
            - **Data Lineage:** Track data flow with Apache Atlas or Azure Purview
            """)
        
        with st.expander("🤖 Model Development Guidelines"):
            st.markdown("""
            - **Experiment Tracking:** Use MLflow or Weights & Biases
            - **Model Registry:** Centralize model artifacts and metadata
            - **A/B Testing:** Implement gradual rollout with feature flags
            - **Model Monitoring:** Track drift with Evidently AI or Azure ML
            """)
        
        with st.expander("🔧 Infrastructure Recommendations"):
            st.markdown("""
            - **Compute:** Use spot instances for training, reserved for inference
            - **Storage:** Implement tiered storage (hot/cold) for cost optimization
            - **Networking:** Use private endpoints for security
            - **Monitoring:** Implement comprehensive logging and alerting
            """)
        
        with st.expander("📊 Governance Framework"):
            st.markdown("""
            - **Model Cards:** Document model purpose, limitations, and biases
            - **Approval Process:** Implement multi-stage approval for production
            - **Audit Trail:** Maintain complete history of model changes
            - **Compliance:** Ensure GDPR/CCPA compliance in data handling
            """)
    
    st.markdown("---")
    st.subheader("📥 Downloadable Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            label="📄 MLOps Checklist",
            data="MLOps Implementation Checklist",
            file_name="mlops_checklist.pdf",
            mime="application/pdf"
        )
    
    with col2:
        st.download_button(
            label="📊 ROI Template",
            data="AI ROI Calculation Template",
            file_name="roi_template.xlsx",
            mime="application/vnd.ms-excel"
        )
    
    with col3:
        st.download_button(
            label="🏗️ Architecture Templates",
            data="Cloud Architecture Templates",
            file_name="architecture_templates.zip",
            mime="application/zip"
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Global AI-Accelerator Toolkit v2.0 | Built with Streamlit | © 2024</p>
    <p>🚀 Accelerating Enterprise AI Transformation</p>
</div>
""", unsafe_allow_html=True)