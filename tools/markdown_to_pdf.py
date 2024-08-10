import os
import logging
import markdown
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def get_styles():
    styles = getSampleStyleSheet()
    if 'Code' not in styles:
        styles.add(ParagraphStyle(name='Code',
                                  parent=styles['BodyText'],
                                  fontName='Courier',
                                  fontSize=8,
                                  backgroundColor='#f4f4f4',
                                  spaceAfter=6))
    return styles

def markdown_to_pdf(markdown_file, source_folder, output_folder):
    try:
        input_path = os.path.join(source_folder, markdown_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(markdown_file)[0]}.pdf")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content, extensions=['extra', 'codehilite'])
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Create a PDF document
        doc = SimpleDocTemplate(output_path, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        
        # Get styles
        styles = get_styles()
        
        # Parse HTML and create PDF content
        story = []
        for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'pre']):
            if element.name == 'h1':
                story.append(Paragraph(element.text, styles['Heading1']))
            elif element.name == 'h2':
                story.append(Paragraph(element.text, styles['Heading2']))
            elif element.name == 'h3':
                story.append(Paragraph(element.text, styles['Heading3']))
            elif element.name == 'p':
                if element.find('code'):
                    story.append(Paragraph(element.text, styles['Code']))
                else:
                    story.append(Paragraph(element.text, styles['BodyText']))
            elif element.name == 'pre':
                code_text = element.text.strip()
                story.append(Preformatted(code_text, styles['Code']))
            story.append(Spacer(1, 0.2*inch))
        
        # Build PDF
        doc.build(story)
        
        logging.info(f"Converted {markdown_file} to PDF")
        return f"Converted {markdown_file} to PDF"
    except Exception as e:
        logging.error(f"Error converting {markdown_file} to PDF: {str(e)}")
        raise