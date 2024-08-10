import os
import logging
from tools.markdown_to_pdf import markdown_to_pdf
from tools.pdf_to_txt import pdf_to_txt
from tools.word_to_txt import word_to_txt

def convert_documents(source_folder, output_folder):
    converted_files = []
    for filename in os.listdir(source_folder):
        try:
            if filename.endswith('.md'):
                result = markdown_to_pdf(filename, source_folder, output_folder)
                converted_files.append(result)
            elif filename.endswith('.pdf'):
                result = pdf_to_txt(filename, source_folder, output_folder)
                converted_files.append(result)
            elif filename.endswith('.docx'):
                result = word_to_txt(filename, source_folder, output_folder)
                converted_files.append(result)
            else:
                logging.warning(f"Unsupported file type: {filename}")
        except Exception as e:
            logging.error(f"Error converting {filename}: {str(e)}")
    
    if not converted_files:
        logging.warning("No files were converted.")
    else:
        logging.info(f"Converted {len(converted_files)} file(s).")
    
    return converted_files