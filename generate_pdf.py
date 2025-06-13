import markdown
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
import os

def create_product_overview_pdf():
    """Generate a professional PDF from the Product Overview markdown"""
    
    # Create PDF
    pdf_filename = "AI_Accelerator_Toolkit_Product_Overview.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1E88E5'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1565C0'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    # Title Page
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("Global AI-Accelerator Toolkit", title_style))
    elements.append(Paragraph("Product Overview", heading_style))
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Enterprise AI Transformation Platform", body_style))
    elements.append(Paragraph("$45M+ Proven Impact | 350+ Business Units", body_style))
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("Version 2.0 | 2024", body_style))
    elements.append(PageBreak())
    
    # Executive Summary
    elements.append(Paragraph("Executive Summary", heading_style))
    elements.append(Paragraph(
        "The Global AI-Accelerator Toolkit is an enterprise-ready platform designed to rapidly assess, "
        "architect, and deploy AI solutions at scale. Built from real-world experience transforming "
        "350+ business units with $45M+ in realized ROI, this toolkit provides organizations with "
        "the frameworks, templates, and calculators needed to accelerate their AI journey.",
        body_style
    ))
    elements.append(Spacer(1, 0.3*inch))
    
    # Value Proposition
    elements.append(Paragraph("Value Proposition", heading_style))
    elements.append(Paragraph("Transform AI from Concept to Production 40% Faster", subheading_style))
    
    value_props = [
        ["Reduce Time-to-Market", "From 6 months to 3.5 months average"],
        ["Increase Success Rate", "From 35% to 78% for AI initiatives"],
        ["Maximize ROI", "Average 23% ROI improvement year-over-year"],
        ["Scale Efficiently", "Deploy across multiple business units simultaneously"]
    ]
    
    t = Table(value_props, colWidths=[3*inch, 3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.white)
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    # Core Modules
    elements.append(Paragraph("Core Modules", heading_style))
    
    modules = [
        {
            "name": "1. Change-Readiness Dashboard",
            "purpose": "Assess organizational AI maturity across dimensions",
            "impact": "Identify high-potential units, reduce risks by 45%"
        },
        {
            "name": "2. Blueprint Generator",
            "purpose": "Auto-generate enterprise architecture patterns",
            "impact": "Accelerate design by 60%, ensure compliance"
        },
        {
            "name": "3. ROI Estimator",
            "purpose": "Calculate and forecast AI investment returns",
            "impact": "Data-driven decisions, accelerate stakeholder buy-in"
        },
        {
            "name": "4. MLOps Starter Kit",
            "purpose": "Production-ready templates and pipelines",
            "impact": "Reduce setup time by 70%, standardize practices"
        }
    ]
    
    for module in modules:
        elements.append(Paragraph(module["name"], subheading_style))
        elements.append(Paragraph(f"Purpose: {module['purpose']}", body_style))
        elements.append(Paragraph(f"Business Impact: {module['impact']}", body_style))
        elements.append(Spacer(1, 0.2*inch))
    
    elements.append(PageBreak())
    
    # Success Stories
    elements.append(Paragraph("Proven Results", heading_style))
    
    results = [
        ["Leading Insurance Provider", "$5M+ impact, 30% increase in conversions"],
        ["Global Retail Chain", "25% operational cost reduction"],
        ["Healthcare Technology Company", "40% improvement in patient outcomes"],
        ["Financial Services Firm", "92% fraud detection, $8M saved"]
    ]
    
    t2 = Table(results, colWidths=[2*inch, 4*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1E88E5')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (1, -1), colors.beige),
    ]))
    elements.append(t2)
    elements.append(Spacer(1, 0.5*inch))
    
    # Contact Information
    elements.append(Paragraph("Get Started Today", heading_style))
    elements.append(Paragraph("Contact: Suman Mukherjee", body_style))
    elements.append(Paragraph("Email: smn.mukherjee@gmail.com", body_style))
    elements.append(Paragraph("Website: www.mukherjeesuman.com", body_style))
    elements.append(Paragraph("Live Demo: https://ai-accelerator-toolkit.streamlit.app", body_style))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF created successfully: {pdf_filename}")
    
    return pdf_filename

def create_simple_text_pdf():
    """Create a simpler PDF version without dependencies"""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    
    pdf_filename = "AI_Accelerator_Toolkit_Overview_Simple.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    # Title page
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0.12, 0.53, 0.90)  # Blue color
    c.drawCentredString(width/2, height-100, "Global AI-Accelerator Toolkit")
    
    c.setFont("Helvetica", 16)
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(width/2, height-150, "Product Overview")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height-250, "Enterprise AI Transformation Platform")
    c.drawCentredString(width/2, height-280, "$45M+ Proven Impact | 350+ Business Units")
    
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, 100, "Version 2.0 | 2024")
    c.drawCentredString(width/2, 70, "Suman Mukherjee | smn.mukherjee@gmail.com")
    
    # New page - content
    c.showPage()
    
    # Executive Summary
    c.setFont("Helvetica-Bold", 18)
    c.setFillColorRGB(0.08, 0.40, 0.75)
    c.drawString(50, height-50, "Executive Summary")
    
    c.setFont("Helvetica", 11)
    c.setFillColorRGB(0, 0, 0)
    y = height - 80
    
    text_lines = [
        "The Global AI-Accelerator Toolkit is an enterprise-ready platform designed to rapidly",
        "assess, architect, and deploy AI solutions at scale. Built from real-world experience",
        "transforming 350+ business units with $45M+ in realized ROI.",
        "",
        "Key Features:",
        "• Change-Readiness Dashboard - Assess AI maturity instantly",
        "• Blueprint Generator - Industry-specific architectures",
        "• ROI Estimator - Data-driven business cases",
        "• MLOps Starter Kit - Production-ready templates",
        "",
        "Proven Results:",
        "• 40% faster time-to-market",
        "• 78% project success rate",
        "• 23% average ROI improvement",
        "• 70% reduction in MLOps setup time"
    ]
    
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 20
    
    # Contact section
    y = 150
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Get Started Today")
    
    c.setFont("Helvetica", 11)
    y -= 25
    c.drawString(50, y, "Contact: Suman Mukherjee")
    y -= 20
    c.drawString(50, y, "Email: smn.mukherjee@gmail.com")
    y -= 20
    c.drawString(50, y, "Website: www.mukherjeesuman.com")
    y -= 20
    c.drawString(50, y, "Live Demo: https://ai-accelerator-toolkit.streamlit.app")
    
    c.save()
    print(f"Simple PDF created successfully: {pdf_filename}")
    
    return pdf_filename

if __name__ == "__main__":
    # Try to create the full PDF, fall back to simple if dependencies missing
    try:
        create_product_overview_pdf()
    except ImportError:
        print("Some dependencies missing, creating simple PDF instead...")
        create_simple_text_pdf()