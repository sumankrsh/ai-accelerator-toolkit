import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
import base64

def generate_mlops_checklist_pdf():
    """Generate MLOps Checklist PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-50, "MLOps Implementation Checklist")
    
    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height-80, "Enterprise AI Deployment Guide")
    
    # Content
    y = height - 120
    categories = [
        ("Data Pipeline", [
            "Data versioning system implemented",
            "Automated data quality checks",
            "Feature store established",
            "Data lineage tracking"
        ]),
        ("Model Development", [
            "Experiment tracking system",
            "Model registry configured",
            "Automated hyperparameter tuning",
            "Code versioning (Git)"
        ]),
        ("Deployment & Monitoring", [
            "CI/CD pipeline established",
            "A/B testing framework",
            "Model drift detection",
            "Performance monitoring dashboard"
        ]),
        ("Governance", [
            "Model documentation standards",
            "Approval workflow defined",
            "Audit trail maintained",
            "Compliance checks automated"
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
    
    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, 50, "© 2024 AI Accelerator Toolkit | Enterprise AI Solutions")
    
    c.save()
    buffer.seek(0)
    return buffer

def generate_roi_template_pdf():
    """Generate ROI Template PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-50, "AI ROI Calculation Template")
    
    # Content sections
    y = height - 100
    
    sections = [
        ("1. Cost Savings", [
            "Labor cost reduction: $_______",
            "Process automation savings: $_______",
            "Error reduction value: $_______",
            "Efficiency gains: $_______"
        ]),
        ("2. Revenue Generation", [
            "New revenue streams: $_______",
            "Upsell/Cross-sell improvement: $_______",
            "Customer retention value: $_______",
            "Market expansion: $_______"
        ]),
        ("3. Implementation Costs", [
            "Initial development: $_______",
            "Infrastructure: $_______",
            "Training & change management: $_______",
            "Ongoing operations: $_______"
        ]),
        ("4. ROI Calculation", [
            "Total Benefits (Year 1): $_______",
            "Total Costs (Year 1): $_______",
            "Net Benefit: $_______",
            "ROI Percentage: _____%"
        ])
    ]
    
    c.setFont("Helvetica-Bold", 14)
    for section, items in sections:
        c.drawString(50, y, section)
        y -= 25
        
        c.setFont("Helvetica", 11)
        for item in items:
            c.drawString(70, y, item)
            y -= 20
        y -= 15
    
    c.save()
    buffer.seek(0)
    return buffer

def generate_architecture_pdf(industry, cloud_provider, use_case, pattern):
    """Generate Architecture Blueprint PDF"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height-50, f"{industry} AI Architecture Blueprint")
    
    # Subtitle
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height-75, f"{cloud_provider} | {use_case}")
    
    # Architecture Components
    y = height - 120
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Architecture Components")
    y -= 30
    
    components = {
        "Data Layer": [
            f"Data Lake: {cloud_provider} Storage",
            "Data Warehouse: Enterprise DW",
            "Stream Processing: Real-time ingestion",
            "Data Catalog: Metadata management"
        ],
        "Processing Layer": [
            "Batch Processing: Distributed compute",
            "Stream Processing: Event streaming",
            "Feature Engineering: Automated pipelines",
            "Data Quality: Validation framework"
        ],
        "ML Platform": [
            "Model Training: Distributed training",
            "Model Registry: Version control",
            "Feature Store: Centralized features",
            "Experiment Tracking: MLflow"
        ],
        "Serving Layer": [
            "API Gateway: REST/gRPC endpoints",
            "Model Serving: Container orchestration",
            "Edge Deployment: IoT integration",
            "Caching: Performance optimization"
        ]
    }
    
    for component, details in components.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, y, component)
        y -= 20
        
        c.setFont("Helvetica", 10)
        for detail in details:
            c.drawString(80, y, f"• {detail}")
            y -= 15
        y -= 10
    
    # Cost Estimate
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 150, "Estimated Monthly Cost")
    c.setFont("Helvetica", 10)
    c.drawString(60, 130, f"Development Environment: $5,000 - $8,000")
    c.drawString(60, 115, f"Production Environment: $15,000 - $25,000")
    c.drawString(60, 100, f"Total Annual Estimate: $240,000 - $396,000")
    
    # Footer
    c.setFont("Helvetica", 8)
    c.drawString(50, 40, f"Generated on: {c._date} | AI Accelerator Toolkit")
    
    c.save()
    buffer.seek(0)
    return buffer

def get_download_link(buffer, filename, link_text):
    """Generate download link for PDF"""
    b64 = base64.b64encode(buffer.read()).decode()
    return f'<a href="data:application/pdf;base64,{b64}" download="{filename}" style="text-decoration: none; color: #1E88E5; font-weight: bold;">{link_text}</a>'