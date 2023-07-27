from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime

def generate_will():
    # Capture personal information
    full_name = input("Full Name: ")
    address = input("Address: ")
    date_of_birth = input("Date of Birth (DD/MM/YYYY): ")
    
    # Specify beneficiaries and items
    beneficiaries = []
    add_beneficiary = True
    
    while add_beneficiary:
        beneficiary_name = input("Beneficiary Name: ")
        beneficiary_relationship = input("Relationship: ")
        beneficiary_items = input("Items to leave to beneficiary: ")
        beneficiaries.append((beneficiary_name, beneficiary_relationship, beneficiary_items))
        
        choice = input("Add another beneficiary? (y/n): ")
        add_beneficiary = True if choice.lower() == "y" else False
    
    # Create a PDF document
    filename = f"{full_name.replace(' ', '-')}-WILL.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    signature_style = ParagraphStyle(
        'SignatureStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        spaceAfter=30
    )
    elements = []
    
    # Add content to the PDF document
    elements.append(Paragraph("<u>Last Will and Testament</u>", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"I, {full_name}, of {address}, born on {date_of_birth}, declare this to be my Last Will and Testament.", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("I hereby revoke all previous wills and codicils.", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Beneficiaries:</b>", styles['Heading2']))
    
    for beneficiary in beneficiaries:
        beneficiary_name, beneficiary_relationship, beneficiary_items = beneficiary
        elements.append(Paragraph(f"- {beneficiary_name}, {beneficiary_relationship}", styles['Normal']))
        elements.append(Paragraph(f"  Items: {beneficiary_items}", styles['Normal']))
    
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Executor:</b>", styles['Heading2']))
    elements.append(Paragraph("I appoint ____________________ as the executor of this will.", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Signature:</b>", styles['Heading2']))
    elements.append(Paragraph("____________________", signature_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"{full_name}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Build the PDF document and save it
    doc.build(elements)

    print(f"Will generated and exported as {filename}")

# Generate the will and export as PDF
generate_will()
