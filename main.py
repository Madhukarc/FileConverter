import os
import logging
from document_converter import convert_documents

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        source_folder = "source_files"
        output_folder = "converted_files"
        
        if not os.path.exists(source_folder):
            raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")
        
        os.makedirs(output_folder, exist_ok=True)
        
        converted_files = convert_documents(source_folder, output_folder)
        if converted_files:
            logging.info("Conversion process completed successfully.")
            for file in converted_files:
                print(file)
        else:
            logging.warning("No files were converted.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()