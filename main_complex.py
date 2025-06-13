import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from utils import (
    generate_mlops_checklist_pdf, 
    generate_roi_template_pdf, 
    generate_architecture_pdf,
    get_download_link
)

# Page configuration
st.set_page_config(
    page_title="AI Accelerator Toolkit | Enterprise AI Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
<style>
    /* Main theme */
    .stApp {
        background: linear-gradient(135deg, #0a0f1c 0%, #1a1f2e 100%);
    }
    
    /* Headers */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(120deg, #00d4ff 0%, #0099ff 50%, #0066ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 1rem;
        letter-spacing: -1px;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #8892b0;
        text-align: center;
        margin-bottom: 3rem;
    }
    
    /* Metric cards */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 153, 255, 0.1) 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(0, 212, 255, 0.2);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(30, 41, 59, 0.5);
        border-radius: 12px;
        padding: 0.5rem;
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: #8892b0;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.4);
    }
    
    /* Info boxes */
    .info-box {
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Download links */
    .download-box {
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        text-align: center;
    }
    
    /* Plotly charts */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0a0f1c;
        border-right: 1px solid rgba(0, 212, 255, 0.2);
    }
    
    /* Success messages */
    .success-message {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 255, 136, 0.2) 100%);
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    if os.path.exists('dummy_enterprise_data.csv'):
        df = pd.read_csv('dummy_enterprise_data.csv')
        df['Implementation_Date'] = pd.to_datetime(df['Implementation_Date'])
        return df
    else:
        st.error("Data file not found. Please run generate_dummy_data.py first.")
        return pd.DataFrame()

# Initialize session state
if 'generated_blueprint' not in st.session_state:
    st.session_state.generated_blueprint = False

df = load_data()

# Sidebar
with st.sidebar:
    st.markdown("### 🚀 AI Accelerator Toolkit")
    st.markdown("**Version:** 2.0 Enterprise")
    st.markdown("**Last Updated:** " + datetime.now().strftime("%B %Y"))
    
    st.markdown("---")
    
    # Professional branding
    st.markdown("### 👤 Solution Architect")
    st.markdown("**Suman Mukherjee**")
    st.markdown("Global AI Strategy Lead")
    st.markdown("📧 smn.mukherjee@gmail.com")
    
    st.markdown("---")
    
    # Filters
    st.markdown("### 🎛️ Global Filters")
    
    if not df.empty:
        selected_regions = st.multiselect(
            "Select Regions",
            options=df['Region'].unique(),
            default=df['Region'].unique()
        )
        
        selected_industries = st.multiselect(
            "Select Industries",
            options=df['Industry'].unique(),
            default=df['Industry'].unique()[:4]
        )
        
        maturity_range = st.slider(
            "Maturity Score Range",
            min_value=1,
            max_value=10,
            value=(3, 10),
            step=1
        )
        
        # Filter data
        filtered_df = df[
            (df['Region'].isin(selected_regions)) &
            (df['Industry'].isin(selected_industries)) &
            (df['Overall_Readiness_Score'] >= maturity_range[0]) &
            (df['Overall_Readiness_Score'] <= maturity_range[1])
        ]
    else:
        filtered_df = df
    
    st.markdown("---")
    
    # Quick stats
    if not filtered_df.empty:
        st.markdown("### 📊 Quick Stats")
        st.metric("Total Units", len(filtered_df))
        st.metric("Avg Readiness", f"{filtered_df['Overall_Readiness_Score'].mean():.1f}/10")
        st.metric("Total ROI", f"${filtered_df['Estimated_AI_ROI_MillionUSD'].sum():.1f}M")

# Main content
st.markdown('<h1 class="main-header">AI Accelerator Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enterprise AI Transformation Platform | $45M+ Proven Impact</p>', unsafe_allow_html=True)

# Top KPI Metrics
if not filtered_df.empty:
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_units = len(filtered_df)
        delta = int(total_units * 0.15)
        st.metric("Business Units", total_units, f"+{delta}")
    
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

# Main tabs with icons
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Change Readiness",
    "🏗️ Blueprint Generator",
    "💰 ROI Estimator",
    "📚 MLOps Toolkit"
])

with tab1:
    st.header("Enterprise AI Readiness Assessment")
    
    if not filtered_df.empty:
        # Create two columns for main visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Readiness Heatmap
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
                aspect="auto",
                title="AI Readiness by Industry and Region"
            )
            fig.update_layout(
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Maturity Components
            st.subheader("📈 Maturity Score Distribution")
            
            maturity_scores = pd.DataFrame({
                'Data Maturity': filtered_df['Data_Maturity_Score'],
                'MLOps Maturity': filtered_df['ML_Ops_Maturity_Score'],
                'Governance': filtered_df['Data_Governance_Score']
            })
            
            fig = go.Figure()
            for column in maturity_scores.columns:
                fig.add_trace(go.Box(
                    y=maturity_scores[column],
                    name=column,
                    boxpoints='outliers',
                    marker_color='rgb(0, 212, 255)' if column == 'Data Maturity' else 
                               'rgb(0, 153, 255)' if column == 'MLOps Maturity' else 
                               'rgb(0, 102, 255)'
                ))
            
            fig.update_layout(
                title="Maturity Score Components",
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0'),
                yaxis=dict(range=[0, 10])
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Additional insights
        st.subheader("🔍 Key Insights")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Top performing regions
            top_regions = filtered_df.groupby('Region')['Overall_Readiness_Score'].mean().sort_values(ascending=False).head(3)
            
            fig = go.Figure(go.Bar(
                x=top_regions.values,
                y=top_regions.index,
                orientation='h',
                marker_color='rgb(0, 212, 255)'
            ))
            fig.update_layout(
                title="Top Performing Regions",
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cloud readiness by industry
            cloud_by_industry = filtered_df.groupby('Industry')['Cloud_Ready'].mean() * 100
            
            fig = px.bar(
                x=cloud_by_industry.index,
                y=cloud_by_industry.values,
                title="Cloud Readiness by Industry (%)",
                color_discrete_sequence=['#00d4ff']
            )
            fig.update_layout(
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0'),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            # AI Investment Distribution
            fig = px.pie(
                filtered_df,
                values='AI_Investment_Percentage',
                names='Industry',
                title="AI Investment Distribution",
                color_discrete_sequence=px.colors.sequential.Blues_r
            )
            fig.update_layout(
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### 💡 Recommendations Based on Assessment")
        
        avg_readiness = filtered_df['Overall_Readiness_Score'].mean()
        if avg_readiness < 5:
            st.warning("**Low Readiness Detected**: Focus on foundational capabilities before advanced AI initiatives.")
            st.markdown("- Invest in data infrastructure and governance")
            st.markdown("- Build MLOps capabilities through training")
            st.markdown("- Start with pilot projects in high-readiness units")
        elif avg_readiness < 7:
            st.info("**Moderate Readiness**: Ready for targeted AI initiatives with proper planning.")
            st.markdown("- Standardize MLOps practices across units")
            st.markdown("- Focus on high-ROI use cases")
            st.markdown("- Establish Centers of Excellence")
        else:
            st.success("**High Readiness**: Prepared for enterprise-wide AI transformation.")
            st.markdown("- Scale successful pilots across regions")
            st.markdown("- Invest in advanced AI capabilities")
            st.markdown("- Lead industry innovation")
        
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.header("AI Architecture Blueprint Generator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🛠️ Configuration Panel")
        
        # Input fields
        selected_industry = st.selectbox(
            "Industry Vertical",
            options=['Insurance', 'Healthcare', 'Retail', 'Banking', 'Manufacturing', 'Technology'],
            help="Select your industry for tailored architecture"
        )
        
        selected_cloud = st.selectbox(
            "Cloud Platform",
            options=['Azure', 'AWS', 'GCP', 'Multi-Cloud'],
            help="Choose your preferred cloud provider"
        )
        
        selected_use_case = st.selectbox(
            "Primary Use Case",
            options=[
                'Customer Intelligence',
                'Fraud Detection',
                'Demand Forecasting',
                'Predictive Maintenance',
                'Document Processing',
                'Risk Assessment',
                'Quality Control',
                'Personalization'
            ]
        )
        
        architecture_pattern = st.radio(
            "Architecture Pattern",
            options=['Batch Processing', 'Real-time Streaming', 'Hybrid', 'Edge Computing'],
            help="Select based on your latency requirements"
        )
        
        st.markdown("### 🔧 Additional Components")
        
        include_mlops = st.checkbox("MLOps Pipeline", value=True)
        include_governance = st.checkbox("Data Governance Layer", value=True)
        include_security = st.checkbox("Advanced Security", value=True)
        include_monitoring = st.checkbox("Monitoring & Alerting", value=True)
        
        generate_btn = st.button("🚀 Generate Blueprint", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("📐 Generated Architecture")
        
        if generate_btn or st.session_state.generated_blueprint:
            st.session_state.generated_blueprint = True
            
            # Display architecture details
            st.markdown(f"### {selected_cloud} Reference Architecture for {selected_industry}")
            st.markdown(f"**Use Case:** {selected_use_case} | **Pattern:** {architecture_pattern}")
            
            # Architecture diagram placeholder
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.markdown("#### 📊 Architecture Diagram")
            
            # Create a visual representation
            components = {
                "Data Sources": ["Operational Systems", "External APIs", "IoT Devices", "Third-party Data"],
                "Ingestion Layer": ["Event Streaming", "Batch ETL", "Change Data Capture", "API Gateway"],
                "Storage Layer": ["Data Lake", "Data Warehouse", "Feature Store", "Object Storage"],
                "Processing Layer": ["Stream Processing", "Batch Processing", "ML Pipeline", "Data Quality"],
                "ML Platform": ["Model Training", "Model Registry", "Experiment Tracking", "Model Serving"],
                "Serving Layer": ["REST APIs", "GraphQL", "gRPC", "Edge Deployment"],
                "Monitoring": ["Performance Metrics", "Data Quality", "Model Drift", "Cost Tracking"]
            }
            
            # Display components
            for layer, items in components.items():
                st.markdown(f"**{layer}**")
                cols = st.columns(len(items))
                for i, item in enumerate(items):
                    with cols[i]:
                        st.info(item)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Technical specifications
            st.markdown("#### 📋 Technical Specifications")
            
            specs_col1, specs_col2 = st.columns(2)
            
            with specs_col1:
                st.markdown("**Infrastructure**")
                st.markdown(f"- Cloud Provider: {selected_cloud}")
                st.markdown(f"- Compute: Auto-scaling clusters")
                st.markdown(f"- Storage: Tiered storage strategy")
                st.markdown(f"- Network: Private endpoints")
                
                st.markdown("**Data Pipeline**")
                st.markdown(f"- Ingestion: {'Real-time' if 'Streaming' in architecture_pattern else 'Batch'}")
                st.markdown(f"- Processing: Distributed computing")
                st.markdown(f"- Orchestration: Workflow automation")
            
            with specs_col2:
                st.markdown("**ML Infrastructure**")
                st.markdown(f"- Training: GPU-enabled compute")
                st.markdown(f"- Serving: Container orchestration")
                st.markdown(f"- Registry: Centralized model store")
                
                st.markdown("**Cost Estimate**")
                dev_cost = 5000 if selected_cloud == 'Azure' else 6000
                prod_cost = 15000 if selected_cloud == 'Azure' else 18000
                st.markdown(f"- Development: ${dev_cost:,} - ${dev_cost+3000:,}/month")
                st.markdown(f"- Production: ${prod_cost:,} - ${prod_cost+10000:,}/month")
            
            # Download blueprint
            st.markdown("---")
            
            blueprint_pdf = generate_architecture_pdf(
                selected_industry,
                selected_cloud,
                selected_use_case,
                architecture_pattern
            )
            
            st.markdown('<div class="download-box">', unsafe_allow_html=True)
            st.markdown("### 📥 Download Your Blueprint")
            download_link = get_download_link(
                blueprint_pdf,
                f"{selected_industry}_{selected_cloud}_Architecture.pdf",
                "⬇️ Download Architecture Blueprint (PDF)"
            )
            st.markdown(download_link, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Success message
            st.markdown('<div class="success-message">✅ Blueprint generated successfully! Download your customized architecture above.</div>', unsafe_allow_html=True)
        
        else:
            st.info("👈 Configure your requirements and click 'Generate Blueprint' to create a customized architecture")

with tab3:
    st.header("ROI Estimation & Business Case Builder")
    
    if not filtered_df.empty:
        # ROI Overview Dashboard
        col1, col2 = st.columns(2)
        
        with col1:
            # ROI by Region
            roi_by_region = filtered_df.groupby('Region')['Estimated_AI_ROI_MillionUSD'].sum().sort_values(ascending=True)
            
            fig = go.Figure(go.Bar(
                x=roi_by_region.values,
                y=roi_by_region.index,
                orientation='h',
                text=[f'${x:.1f}M' for x in roi_by_region.values],
                textposition='outside',
                marker=dict(
                    color=roi_by_region.values,
                    colorscale='Blues',
                    showscale=True,
                    colorbar=dict(title="ROI ($M)")
                )
            ))
            fig.update_layout(
                title="Total AI ROI by Region",
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0'),
                xaxis_title="ROI (Million USD)"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # ROI by Industry
            roi_by_industry = filtered_df.groupby('Industry')['Estimated_AI_ROI_MillionUSD'].mean()
            
            fig = px.treemap(
                names=roi_by_industry.index,
                values=roi_by_industry.values,
                title="Average ROI by Industry",
                color=roi_by_industry.values,
                color_continuous_scale='Blues',
                hover_data={'ROI': [f'${x:.2f}M' for x in roi_by_industry.values]}
            )
            fig.update_layout(
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#8892b0')
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Custom ROI Calculator
    st.markdown("---")
    st.subheader("🧮 Custom ROI Calculator")
    
    calc_col1, calc_col2, calc_col3 = st.columns(3)
    
    with calc_col1:
        st.markdown("#### 📊 Business Metrics")
        annual_revenue = st.number_input(
            "Annual Revenue ($M)",
            min_value=10.0,
            max_value=10000.0,
            value=500.0,
            step=10.0
        )
        
        num_employees = st.number_input(
            "Number of Employees",
            min_value=100,
            max_value=100000,
            value=5000,
            step=100
        )
        
        current_efficiency = st.slider(
            "Current Process Efficiency (%)",
            min_value=30,
            max_value=90,
            value=60,
            step=5
        )
    
    with calc_col2:
        st.markdown("#### 🎯 AI Impact Projections")
        
        efficiency_gain = st.slider(
            "Expected Efficiency Gain (%)",
            min_value=5,
            max_value=50,
            value=25,
            step=5
        )
        
        revenue_uplift = st.slider(
            "Revenue Uplift (%)",
            min_value=0,
            max_value=30,
            value=10,
            step=1
        )
        
        cost_reduction = st.slider(
            "Cost Reduction (%)",
            min_value=5,
            max_value=40,
            value=20,
            step=5
        )
    
    with calc_col3:
        st.markdown("#### 💰 Investment Parameters")
        
        implementation_cost = st.number_input(
            "Implementation Cost ($K)",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100
        )
        
        annual_operating_cost = st.number_input(
            "Annual Operating Cost ($K)",
            min_value=50,
            max_value=2000,
            value=300,
            step=50
        )
        
        implementation_time = st.slider(
            "Implementation Time (months)",
            min_value=3,
            max_value=24,
            value=9,
            step=3
        )
    
    # Calculate ROI
    if st.button("💵 Calculate ROI", type="primary", use_container_width=True):
        # Calculations
        revenue_benefit = annual_revenue * (revenue_uplift / 100) * 1000000  # Convert to dollars
        cost_savings = (annual_revenue * 0.7) * (cost_reduction / 100) * 1000000  # Assume 70% is cost
        total_annual_benefit = revenue_benefit + cost_savings
        
        # 3-year projection
        year1_benefit = total_annual_benefit * 0.5  # Ramp up
        year2_benefit = total_annual_benefit * 0.8
        year3_benefit = total_annual_benefit * 1.0
        
        total_3year_benefit = year1_benefit + year2_benefit + year3_benefit
        total_3year_cost = (implementation_cost * 1000) + (annual_operating_cost * 1000 * 3)
        net_benefit = total_3year_benefit - total_3year_cost
        roi_percentage = (net_benefit / total_3year_cost) * 100
        payback_months = (implementation_cost * 1000) / (total_annual_benefit / 12) if total_annual_benefit > 0 else 999
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 ROI Analysis Results")
        
        result_col1, result_col2, result_col3, result_col4 = st.columns(4)
        
        with result_col1:
            st.metric(
                "3-Year Net Benefit",
                f"${net_benefit/1000000:.1f}M",
                f"{roi_percentage:.0f}% ROI"
            )
        
        with result_col2:
            st.metric(
                "Annual Benefit",
                f"${total_annual_benefit/1000000:.1f}M",
                "After full deployment"
            )
        
        with result_col3:
            st.metric(
                "Payback Period",
                f"{min(payback_months, 999):.0f} months",
                "Time to break even"
            )
        
        with result_col4:
            st.metric(
                "ROI Percentage",
                f"{roi_percentage:.0f}%",
                "3-year return"
            )
        
        # Benefit breakdown chart
        benefit_data = pd.DataFrame({
            'Year': ['Year 1', 'Year 2', 'Year 3'],
            'Revenue Increase': [year1_benefit/1000000 * 0.4, year2_benefit/1000000 * 0.4, year3_benefit/1000000 * 0.4],
            'Cost Savings': [year1_benefit/1000000 * 0.6, year2_benefit/1000000 * 0.6, year3_benefit/1000000 * 0.6]
        })
        
        fig = px.bar(
            benefit_data,
            x='Year',
            y=['Revenue Increase', 'Cost Savings'],
            title='Projected Benefits Over Time',
            color_discrete_sequence=['#00d4ff', '#0099ff']
        )
        fig.update_layout(
            height=300,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#8892b0'),
            yaxis_title="Benefit ($M)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Executive summary
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### 📋 Executive Summary")
        st.markdown(f"""
        Based on the provided parameters, implementing AI across your organization will:
        
        - Generate **${total_annual_benefit/1000000:.1f}M** in annual benefits after full deployment
        - Deliver a **{roi_percentage:.0f}%** return on investment over 3 years
        - Achieve payback in **{min(payback_months, 999):.0f} months**
        - Create **${net_benefit/1000000:.1f}M** in net value
        
        **Recommendation:** {'✅ Proceed with implementation' if roi_percentage > 100 else '⚠️ Optimize parameters for better ROI'}
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Download ROI template
    st.markdown("---")
    roi_template = generate_roi_template_pdf()
    
    st.markdown('<div class="download-box">', unsafe_allow_html=True)
    st.markdown("### 📥 ROI Planning Resources")
    download_link = get_download_link(
        roi_template,
        "AI_ROI_Template.pdf",
        "⬇️ Download ROI Calculation Template (PDF)"
    )
    st.markdown(download_link, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.header("MLOps Starter Kit & Resources")
    
    # Create three columns for resources
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.markdown("### 🚀 Quick Start Templates")
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("#### Project Structure")
        st.code("""
ai-project/
├── .github/workflows/  # CI/CD
├── data/
│   ├── raw/           # Original data
│   ├── processed/     # Feature data
│   └── external/      # Third-party
├── models/
│   ├── experiments/   # Development
│   └── production/    # Deployed
├── src/
│   ├── data/          # Processing
│   ├── features/      # Engineering
│   ├── models/        # Training
│   └── api/           # Serving
├── tests/             # Unit tests
├── configs/           # Parameters
└── docs/              # Documentation
        """, language='text')
        st.markdown('</div>', unsafe_allow_html=True)
    
    with res_col2:
        st.markdown("### 📋 Best Practices")
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        
        with st.expander("✅ Data Engineering"):
            st.markdown("""
            - **Version Control**: Use DVC or Delta Lake
            - **Quality Checks**: Great Expectations
            - **Feature Store**: Centralized features
            - **Lineage**: Track data flow
            - **Privacy**: PII detection & masking
            """)
        
        with st.expander("🤖 Model Development"):
            st.markdown("""
            - **Experiments**: Track with MLflow
            - **Registry**: Centralize models
            - **Testing**: Unit & integration tests
            - **Documentation**: Model cards
            - **Validation**: Cross-validation
            """)
        
        with st.expander("🚀 Deployment"):
            st.markdown("""
            - **CI/CD**: Automated pipelines
            - **Containers**: Docker/Kubernetes
            - **Monitoring**: Real-time metrics
            - **A/B Testing**: Gradual rollout
            - **Rollback**: Quick recovery
            """)
        
        with st.expander("🔒 Governance"):
            st.markdown("""
            - **Compliance**: GDPR/CCPA ready
            - **Audit Trail**: Complete history
            - **Access Control**: Role-based
            - **Model Cards**: Documentation
            - **Bias Detection**: Fairness checks
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with res_col3:
        st.markdown("### 🛠️ Technology Stack")
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("#### Recommended Tools")
        
        tools = {
            "Orchestration": ["Airflow", "Kubeflow", "Prefect"],
            "Experiment Tracking": ["MLflow", "W&B", "Neptune"],
            "Model Registry": ["MLflow", "Seldon", "BentoML"],
            "Monitoring": ["Evidently", "Grafana", "Datadog"],
            "Feature Store": ["Feast", "Tecton", "Databricks"],
            "Data Validation": ["Great Expectations", "Deequ", "TFX"]
        }
        
        for category, tool_list in tools.items():
            st.markdown(f"**{category}**")
            st.markdown(" • ".join(tool_list))
            st.markdown("")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # MLOps Pipeline Example
    st.markdown("---")
    st.subheader("📊 MLOps Pipeline Architecture")
    
    pipeline_stages = {
        "1. Data Pipeline": {
            "Input": "Raw data sources",
            "Process": "ETL, validation, feature engineering",
            "Output": "Feature store",
            "Tools": "Airflow, Spark, dbt"
        },
        "2. Training Pipeline": {
            "Input": "Features + labels",
            "Process": "Model training, hyperparameter tuning",
            "Output": "Trained models",
            "Tools": "MLflow, Kubeflow, Ray"
        },
        "3. Deployment Pipeline": {
            "Input": "Validated models",
            "Process": "Containerization, deployment",
            "Output": "Model endpoints",
            "Tools": "Docker, Kubernetes, Seldon"
        },
        "4. Monitoring Pipeline": {
            "Input": "Production metrics",
            "Process": "Drift detection, performance tracking",
            "Output": "Alerts & dashboards",
            "Tools": "Evidently, Prometheus, Grafana"
        }
    }
    
    pipe_col1, pipe_col2 = st.columns(2)
    
    for i, (stage, details) in enumerate(pipeline_stages.items()):
        col = pipe_col1 if i % 2 == 0 else pipe_col2
        with col:
            st.markdown(f'<div class="info-box">', unsafe_allow_html=True)
            st.markdown(f"#### {stage}")
            for key, value in details.items():
                st.markdown(f"**{key}:** {value}")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Downloadable resources
    st.markdown("---")
    st.markdown("### 📥 Downloadable Resources")
    
    download_col1, download_col2, download_col3 = st.columns(3)
    
    with download_col1:
        mlops_checklist = generate_mlops_checklist_pdf()
        st.markdown('<div class="download-box">', unsafe_allow_html=True)
        download_link = get_download_link(
            mlops_checklist,
            "MLOps_Implementation_Checklist.pdf",
            "📋 MLOps Checklist (PDF)"
        )
        st.markdown(download_link, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with download_col2:
        st.markdown('<div class="download-box">', unsafe_allow_html=True)
        st.markdown("🏗️ **Architecture Templates**")
        st.markdown("Coming soon...")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with download_col3:
        st.markdown('<div class="download-box">', unsafe_allow_html=True)
        st.markdown("📚 **Best Practices Guide**")
        st.markdown("Coming soon...")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #8892b0; padding: 2rem 0;'>
    <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>
        🚀 AI Accelerator Toolkit v2.0 Enterprise | Built with Streamlit
    </p>
    <p style='font-size: 0.9rem;'>
        Accelerating Enterprise AI Transformation | © 2024 Suman Mukherjee
    </p>
</div>
""", unsafe_allow_html=True)