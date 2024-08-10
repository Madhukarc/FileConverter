import os
import logging
import pdfplumber

def pdf_to_txt(pdf_file, source_folder, output_folder):
    try:
        input_path = os.path.join(source_folder, pdf_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}.txt")
        
        with pdfplumber.open(input_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        logging.info(f"Converted {pdf_file} to TXT")
        return f"Converted {pdf_file} to TXT"
    except Exception as e:
        logging.error(f"Error converting {pdf_file} to TXT: {str(e)}")
        raise